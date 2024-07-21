import os
import cv2


class VideoFramer(object):
    def __init__(self, video_path, frame_dir, frame_rate=1):
        self.video_path = video_path
        self.frame_dir = frame_dir
        self.frame_rate = frame_rate

        if not os.path.exists(self.video_path):
            raise FileNotFoundError(f"Video file not found: {self.video_path}")

        self._frame_dir()

    def extract_frames(self):
        video = cv2.VideoCapture(self.video_path)
        self._on_extracting_start()
        frame_count = 0
        while True:
            ret, frame = video.read()
            if not ret:
                self._on_extracting_end()
                break
            if frame_count % self.frame_rate == 0:
                self._extract_frame(frame, frame_count)
            frame_count += 1
        video.release()
        cv2.destroyAllWindows()

    def _extract_frame(self, frame, frame_count):
        self._on_frame_start(frame_count)

        frame_path = os.path.join(self.frame_dir, f"{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)

        self._on_frame_end(frame_count)

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
        print(f"Extracting frames from {self.video_path}...")

    def _on_extracting_end(self):
        print(f"Frames extracted to {self.frame_dir}")

    def _on_frame_start(self, frame_count):
        print(f"Extracting frame {frame_count}...")

    def _on_frame_end(self, frame_count):
        print(f"Frame {frame_count} extracted.")
