# YouTube Video Downloader
![YouTubeVideoDownloader](https://github.com/chevonnefernandes/YouTube-Video-Downloader/assets/161243278/4a9ebd01-32a4-422d-9a48-09c8267c654c)

## Overview

YouTube Downloader is a simple desktop application built with Python and Tkinter that allows users to download high resolution videos from YouTube. It provides a user-friendly interface for inserting YouTube video links, monitoring the download progress, and displaying download status.

## Features

- **Insert YouTube link**: Users can input the URL of the YouTube video they want to download.
- **Download progress**: Displays the progress of the download with a percentage and progress bar.
- **Download status**: Shows the status of the download process, including errors if any occur.

## Usage

1. **Insert YouTube link**: Enter the URL of the YouTube video you want to download into the input field.
2. **Click Download**: Press the "Download" button to start downloading the video.
3. **Monitor progress**: The progress bar and percentage will update as the download progresses.
4. **View download status**: The download status will be displayed in the text area.

## Installation

1. Clone the repository:

\`\`\`bash
git clone <repository-url>
\`\`\`

2. Install the required Python packages using pip:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

3. Run the application:

\`\`\`bash
python main.py
\`\`\`

## Dependencies

- `tkinter`: Python's standard GUI (Graphical User Interface) toolkit.
- `customtkinter`: A custom theme library for enhancing Tkinter GUIs.
- `pytube`: A library for downloading YouTube videos.
