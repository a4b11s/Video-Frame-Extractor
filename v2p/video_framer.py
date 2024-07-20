import os
import cv2

class VideoFramer(object):
    def __init__(self, video_path, frame_dir, frame_rate=1):
        self.video_path = video_path
        self.frame_dir = frame_dir
        self.frame_rate = frame_rate
        
        if not os.path.exists(self.video_path):
            raise FileNotFoundError(f'Video file not found: {self.video_path}')
        
        self._frame_dir()

    def extract_frames(self):
        video = cv2.VideoCapture(self.video_path)
        frame_count = 0
        while True:
            ret, frame = video.read()
            if not ret:
                break
            if frame_count % self.frame_rate == 0:
                frame_path = os.path.join(self.frame_dir, f'{frame_count}.jpg')
                cv2.imwrite(frame_path, frame)
            frame_count += 1
        video.release()
        cv2.destroyAllWindows()
        
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