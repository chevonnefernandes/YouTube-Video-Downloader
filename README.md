# YouTube Video Downloader

(YouTubeVideoDownloader.png)

## Overview

YouTube Downloader is a simple desktop application built with Python and Tkinter that allows users to download high resolution videos from YouTube. It provides a user-friendly interface for inserting YouTube video links, monitoring the download progress, and displaying download status.

## Features

- **Insert YouTube link**: Users can input the URL of the YouTube video they want to download.
- **Download progress**: Displays the progress of the download with a percentage and progress bar.
- **Download status**: Shows the status of the download process, including errors if any occur.

## Usage

1. Enter the URL of the YouTube video you want to download.
2. Click the "Download" button to start downloading the video.
3. The progress bar and percentage will update as the download progresses.
4. The download status will indicate when the download is complete.

## Installation

1. Clone the repository to your local machine using Git:
"""js
git clone https://github.com/your_username/YouTube-Video-Downloader.git
"""
Replace `your_username` with your GitHub username.

2. Install the required Python dependencies. You can use pip for this:
"""
pip install -r requirements.txt
"""

3. Run the application:
"""
python main.py
"""
This will launch the YouTube Video Downloader application.

## Dependencies

- `tkinter`: Python's standard GUI (Graphical User Interface) toolkit.
- `customtkinter`: A custom theme library for enhancing Tkinter GUIs.
- `pytube`: A library for downloading YouTube videos.