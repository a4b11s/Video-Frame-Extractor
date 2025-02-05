import os
import cv2
import tqdm
import zipfile


class VideoFramer(object):
    def __init__(
        self,
        video_path,
        frame_dir,
        frame_rate=1,
        verbose=False,
        compress=False,
        compress_level=9,
    ):
        self.video_path = video_path
        self.frame_dir = frame_dir
        self.frame_rate = frame_rate
        self.compress = compress
        self.compress_level = compress_level

        if not os.path.exists(self.video_path):
            raise FileNotFoundError(f"Video file not found: {self.video_path}")

        self._frame_dir()

        self.verbose = verbose

    def extract_frames(self):
        video = cv2.VideoCapture(self.video_path)
        self._on_extracting_start()
        frame_count = 0
        while True:
            self._on_iteration_start()
            ret, frame = video.read()
            if not ret:
                self._on_extracting_end()
                break
            if frame_count % self.frame_rate == 0:
                self._extract_frame(frame, frame_count)
            frame_count += 1
            self._on_iteration_end()
        video.release()
        cv2.destroyAllWindows()

    def _extract_frame(self, frame, frame_count):
        self._on_frame_start(frame_count)

        if self.compress:
            self._compress_frame(frame, frame_count)
        else:
            self._save_frame(frame, frame_count)

        self._on_frame_end(frame_count)

    def _save_frame(self, frame, frame_count):
        frame_path = os.path.join(self.frame_dir, f"{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)

    def _compress_frame(self, frame, frame_count):
        file_name = f"{frame_count}.jpg"
        self.zip_file.writestr(
            file_name,
            cv2.imencode(".jpg", frame)[1].tobytes(),
            compress_type=zipfile.ZIP_DEFLATED,
            compresslevel=self.compress_level,
        )

    def _frame_dir(self):
        if not os.path.exists(self.frame_dir):
            os.makedirs(self.frame_dir)
        return self.frame_dir

    def _frame_count(self):
        video = cv2.VideoCapture(self.video_path)
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        video.release()
        cv2.destroyAllWindows()
        return frame_count

    def _on_extracting_start(self):
        if self.verbose:
            self.pbar = tqdm.tqdm(total=self._frame_count(), unit="frames")

        if self.compress:
            zip_file_path = os.path.join(self.frame_dir, "frames.zip")
            self.zip_file = zipfile.ZipFile(
                zip_file_path,
                "w",
                compression=zipfile.ZIP_DEFLATED,
                compresslevel=self.compress_level,
            )

    def _on_extracting_end(self):
        if hasattr(self, "zip_file"):
            self.zip_file.close()

    def _on_frame_start(self, frame_count):
        pass

    def _on_frame_end(self, frame_count):
        pass

    def _on_iteration_start(self):
        pass

    def _on_iteration_end(self):
        if hasattr(self, "pbar") and self.verbose:
            self.pbar.update(1)

    def __del__(self):
        if hasattr(self, "pbar"):
            self.pbar.close()
        cv2.destroyAllWindows()
