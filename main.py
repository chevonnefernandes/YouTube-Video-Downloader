import tkinter
import customtkinter
from pytube import YouTube
import threading


class VideoDownloaderApp:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("720x480")
        self.root.title("YouTube Downloader")
        self.setup_ui()

    def setup_ui(self):
        self.title_label = customtkinter.CTkLabel(
            self.root, text="Insert a YouTube link"
        )
        self.title_label.pack(padx=10, pady=10)

        self.url_var = tkinter.StringVar()
        self.url_entry = customtkinter.CTkEntry(
            self.root, width=350, height=40, textvariable=self.url_var
        )
        self.url_entry.pack()

        self.finish_label = customtkinter.CTkLabel(self.root, text="")
        self.finish_label.pack()

        self.progress_label = customtkinter.CTkLabel(self.root, text="0%")
        self.progress_label.pack()

        self.progress_bar = customtkinter.CTkProgressBar(self.root, width=400)
        self.progress_bar.set(0)
        self.progress_bar.pack(padx=10, pady=10)

        self.download_button = customtkinter.CTkButton(
            self.root, text="Download", command=self.start_download
        )
        self.download_button.pack(padx=10, pady=10)

    def start_download(self):
        video_urls = self.url_var.get().split("\n")
        download_thread = threading.Thread(
            target=self.download_videos, args=(video_urls,)
        )
        download_thread.start()

    def download_videos(self, video_urls):
        for video_url in video_urls:
            try:
                yt_object = YouTube(
                    video_url, on_progress_callback=self.update_progress_bar
                )
                self.finish_label.configure(text=f"Downloading: {yt_object.title}")
                video = yt_object.streams.get_highest_resolution()
                self.progress_bar.set(0)
                video.download()
                self.finish_label.configure(
                    text=f"Download of {yt_object.title} complete!"
                )
            except Exception as e:
                self.finish_label.configure(
                    text=f"Error downloading {video_url}: {str(e)}", text_color="red"
                )

    def update_progress_bar(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        completion_percentage = int(bytes_downloaded / total_size * 100)
        self.progress_label.configure(text=f"{completion_percentage}%")
        self.progress_bar.set(completion_percentage / 100)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = VideoDownloaderApp()
    app.run()
