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
@click.option(
    "--compress",
    "-c",
    is_flag=True,
    help="Compress the frames into a zip file.",
)
@click.option(
    "--compress-level",
    "-l",
    default=9,
    type=int,
    help="Compression level for the zip file. (0-9) Default is 9.",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Print verbose output.",
)
def extract_frames(
    video_file,
    output_dir,
    frame_rate,
    subdir,
    subdir_name,
    compress,
    compress_level,
    verbose,
):
    """
    Extract frames from a video file and save them as images in a directory.
    """
    from v2p.video_framer import VideoFramer
    import os

    if subdir:
        if subdir_name is None:
            subdir_name = os.path.splitext(os.path.basename(video_file))[0]
        output_dir = os.path.join(output_dir, subdir_name)

    video_framer = VideoFramer(
        video_file=video_file,
        output_dir=output_dir,
        frame_rate=frame_rate,
        verbose=verbose,
        compress=compress,
        compress_level=compress_level,
    )

    video_framer.extract_frames()


def init():
    extract_frames()


if __name__ == "__main__":
    init()
