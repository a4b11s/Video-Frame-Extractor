import unittest
import os
import cv2
from v2p.video_framer import VideoFramer
import tempfile


class TestVideoFramer(unittest.TestCase):
    def setUp(self):
        base_dir = os.path.dirname(
            __file__
        )  # Gets the directory where the test script is located
        test_video_path = os.path.join(base_dir, "resources", "test_clip.mp4")
        self.video_path = test_video_path
        self.frame_dir = tempfile.mkdtemp()  # Use temp dir from tempfile library
        self.frame_rate = 1
        self.verbose = False
        self.framer = VideoFramer(
            self.video_path, self.frame_dir, self.frame_rate, self.verbose
        )

    def tearDown(self):
        if os.path.exists(self.frame_dir):
            for file_name in os.listdir(self.frame_dir):
                file_path = os.path.join(self.frame_dir, file_name)
                os.remove(file_path)
            os.rmdir(self.frame_dir)

    def test_extract_frames(self):
        self.framer.extract_frames()
        frame_count = self.framer._frame_count()
        self.assertEqual(len(os.listdir(self.frame_dir)), frame_count)

    def test_calling_callbacks(self):
        # Mock the callbacks
        callbacks = {
            "on_extracting_start": False,
            "on_extracting_end": False,
            "on_frame_start": False,
            "on_frame_end": False,
            "on_iteration_start": False,
            "on_iteration_end": False,
        }

        def mock_on_extracting_start():
            callbacks["on_extracting_start"] = True

        def mock_on_extracting_end():
            callbacks["on_extracting_end"] = True

        def mock_on_frame_start(frame_count):
            callbacks["on_frame_start"] = True

        def mock_on_frame_end(frame_count):
            callbacks["on_frame_end"] = True

        def mock_on_iteration_start():
            callbacks["on_iteration_start"] = True

        def mock_on_iteration_end():
            callbacks["on_iteration_end"] = True

        # Set the mock callbacks
        self.framer._on_extracting_start = mock_on_extracting_start
        self.framer._on_extracting_end = mock_on_extracting_end
        self.framer._on_frame_start = mock_on_frame_start
        self.framer._on_frame_end = mock_on_frame_end
        self.framer._on_iteration_start = mock_on_iteration_start
        self.framer._on_iteration_end = mock_on_iteration_end

        # Call the extract_frames method
        self.framer.extract_frames()

        # Check if the callbacks were called
        self.assertTrue(callbacks["on_extracting_start"])
        self.assertTrue(callbacks["on_extracting_end"])
        self.assertTrue(callbacks["on_frame_start"])
        self.assertTrue(callbacks["on_frame_end"])
        self.assertTrue(callbacks["on_iteration_start"])
        self.assertTrue(callbacks["on_iteration_end"])

    def test_frame_dir(self):
        self.assertEqual(self.framer._frame_dir(), self.frame_dir)
        self.assertTrue(os.path.exists(self.frame_dir))

    def test_frame_count(self):
        frame_count = self.framer._frame_count()
        self.assertEqual(
            frame_count, 93
        )  # The test_clip.mp4 has 93 frames, if use another video, change this value

    def test_on_extracting_start(self):
        self.framer._on_extracting_start()
        self.assertFalse(hasattr(self.framer, "pbar"))

    def test_on_extracting_end(self):
        self.framer._on_extracting_end()
        self.assertFalse(hasattr(self.framer, "pbar"))

    def test_on_frame_start(self):
        frame_count = 0
        self.framer._on_frame_start(frame_count)
        self.assertFalse(hasattr(self.framer, "pbar"))

    def test_on_frame_end(self):
        frame_count = 0
        self.framer._on_frame_end(frame_count)
        self.assertFalse(hasattr(self.framer, "pbar"))

    def test_on_iteration_start(self):
        self.framer._on_iteration_start()
        self.assertFalse(hasattr(self.framer, "pbar"))

    def test_on_iteration_end(self):
        self.framer._on_iteration_end()
        self.assertFalse(hasattr(self.framer, "pbar"))


if __name__ == "__main__":
    unittest.main()
