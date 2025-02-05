[![wakatime](https://wakatime.com/badge/user/018ed2aa-e4fd-4336-bab8-464a091e41b7/project/9370eddc-4f98-44c7-bdb3-2abb2404410c.svg)](https://wakatime.com/badge/user/018ed2aa-e4fd-4336-bab8-464a091e41b7/project/9370eddc-4f98-44c7-bdb3-2abb2404410c)

# Video Frame Extractor

A simple application designed to extract frames from videos.

## Description

This application provides a straightforward way to extract frames from video files, allowing users to capture specific moments as still images. It's particularly useful for analysis, sharing, or archiving purposes.

## Features

- Extract frames at specified intervals
- Support for multiple video formats
- Easy to use command-line interface
- Option to compress extracted frames into a zip file or save them in a folder

## Installation

To use this application, clone the repository to your local machine and navigate to the project directory:

```sh
git clone https://github.com/a4b11s/video-frame-extractor.git
cd video-frame-extractor
```

Install the required dependencies:

```sh
poetry install
```

## Usage

To extract frames from a video, run the following command:

```sh
poetry run v2p path/to/your/video.mp4 output/dir/path --frame-rate 5
```

This command will extract frames from `video.mp4` at every 5-frame interval.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is open-source and available under the MIT License.

## Authors

- Artem Bazyl <a4b11s@gmail.com>
