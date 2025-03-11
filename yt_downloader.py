# ⓒ copy left
# Made by kjh9211 
import tkinter as tk
from tkinter import messagebox
import yt_dlp

def download_video():
    video_url = url_entry.get()
    file_extension = ext_entry.get()

    if not video_url or not file_extension:
        messagebox.showwarning("입력 오류", "URL과 확장자를 모두 입력하세요.")
        return

    # yt-dlp 설정
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'%(title)s.{file_extension}',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        messagebox.showinfo("완료", "영상 다운로드가 완료되었습니다.")
    except Exception as e:
        messagebox.showerror("오류", f"다운로드 중 오류가 발생했습니다: {e}")

# GUI 설정
root = tk.Tk()
root.title("YouTube 영상 다운로드")

# URL 입력
url_label = tk.Label(root, text="유튜브 영상 URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# 확장자 입력
ext_label = tk.Label(root, text="파일 확장자 (예: mp4):")
ext_label.pack()
ext_entry = tk.Entry(root, width=10)
ext_entry.pack()

# 다운로드 버튼
download_button = tk.Button(root, text="다운로드", command=download_video)
download_button.pack()

# GUI 실행
root.mainloop()
