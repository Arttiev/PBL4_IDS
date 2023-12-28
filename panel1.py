import tkinter as tk
from tkinter import ttk
import os

def show_panel(parent_frame):
    # Đọc dữ liệu từ file
    result = os.popen("sudo ufw status numbered").read() + "\n" + os.popen("sudo systemctl status snort3-nids").read()
    
    label = ttk.Label(parent_frame, text=result)
    label.pack(expand=False, fill="both")
