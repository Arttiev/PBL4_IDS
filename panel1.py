import tkinter as tk
from tkinter import ttk

def show_panel(content_frame):
    # Thêm nội dung cụ thể cho Panel 1 vào content_frame
    label = ttk.Label(content_frame, text="This is Panel 1 content")
    label.pack(expand=True, fill="both")
    
    # Bạn có thể thêm các phần khác tùy thuộc vào yêu cầu cụ thể của bạn
    # Ví dụ: các widget khác, các lệnh xử lý sự kiện, v.v.
