import click

@click.command(
    name="extract-frames",
)
@click.argument(
    "video-file",
    type=click.Path(exists=True),
    required=True,
)
@click.argument(
    "output-dir",
    type=click.Path(),
    required=True,
)
@click.option(
    "--frame-rate",
    "-r",
    default=1,
    type=int,
    help="Rate at which to extract frames from the video.",
)
@click.option(
    "--subdir",
    "-s",
    is_flag=True,
    help="Create a subdirectory in the output directory to save the frames.",
)
@click.option(
    "--subdir-name",
    "-n",
    default=None,
    type=str,
    help="Name of the subdirectory to save the frames. If not provided, the name of the video file will be used.",
)
def extract_frames(video_file, output_dir, frame_rate, subdir, subdir_name):
    """
    Extract frames from a video file and save them as images in a directory.
    """
    from v2p.video_framer import VideoFramer
    import os
    
    if subdir:
        if subdir_name is None:
            subdir_name = os.path.splitext(os.path.basename(video_file))[0]
        output_dir = os.path.join(output_dir, subdir_name)
    
    video_framer = VideoFramer(video_file, output_dir, frame_rate)
    
    video_framer.extract_frames()
    
    
def init():
    extract_frames()

if __name__ == "__main__":
    init()