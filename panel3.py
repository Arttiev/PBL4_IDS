import tkinter as tk
from tkinter import ttk
from Threat_BLL import *
from read_alert_to_threat import *

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Chuyển đổi dữ liệu từ file txt thành danh sách các tuple
        data = [tuple(line.strip().split(',')) for line in lines]
    return data

def safe_button_click(tree):
    selected_items = tree.selection()
    if selected_items:
        selected_index = tree.index(selected_items[0])
        print(Threat_BLL.safe_threat(selected_index))

def ignore_button_click(tree):
    selected_items = tree.selection()
    if selected_items:
        selected_index = tree.index(selected_items[0])
        print(Threat_BLL.ignore_threat(selected_index))

def limit_button_click(tree):
    selected_items = tree.selection()
    if selected_items:
        selected_index = tree.index(selected_items[0])
        print(Threat_BLL.limit_threat(selected_index))

def block_button_click(tree):
    selected_items = tree.selection()
    if selected_items:
        selected_index = tree.index(selected_items[0])
        print(Threat_BLL.block_threat(selected_index))

def add_buttons_below_tree(parent_frame,tree):
    button_frame = ttk.Frame(parent_frame)
    button_frame.pack()

    button1 = ttk.Button(button_frame, text="Safe", command= lambda: safe_button_click(tree))
    button1.grid(row=0, column=0, padx=5)

    button2 = ttk.Button(button_frame, text="Ignore", command=lambda: ignore_button_click(tree))
    button2.grid(row=0, column=1, padx=5)

    button3 = ttk.Button(button_frame, text="Limit", command=lambda: limit_button_click(tree))
    button3.grid(row=0, column=2, padx=5)

    button4 = ttk.Button(button_frame, text="Block", command=lambda: block_button_click(tree))
    button4.grid(row=0, column=3, padx=5)

def show_panel(parent_frame):
    # Đọc dữ liệu từ file
    # Tạo Treeview để hiển thị bảng
    tree = ttk.Treeview(parent_frame, columns=("Source IP", "Destination IP", "Protocol", "Occurence"))
    # Đặt tên cột và định dạng
    tree.heading("#0", text="Index")
    tree.column("#0", width=50)
    tree.heading("Source IP", text="Source IP")
    tree.column("Source IP", width=120)
    tree.heading("Destination IP", text="Destination IP")
    tree.column("Destination IP", width=120)
    tree.heading("Protocol", text="Protocol")
    tree.column("Protocol", width=80)
    tree.heading("Occurence", text="Occurence")
    tree.column("Occurence", width=80)

    # Đặt dữ liệu vào bảng
    # for i, row in enumerate(data_from_file):
    #     tree.insert("", i, text=str(i), values=row)
    for i,threat in enumerate(Threat_BLL.to_tuples()):
        tree.insert("",i,text=str(i),values=threat)
    # Hiển thị Treeview
    tree.pack(expand=True, fill="both")

    x_scrollbar = ttk.Scrollbar(parent_frame, orient="horizontal", command=tree.xview)
    x_scrollbar.pack(side="bottom", fill="x")

    # Tạo một cột ảo với chiều rộng lớn để tạo nút cuộn ngang

    # Kết nối thanh cuộn ngang với cột ảo
    tree.configure(xscrollcommand=x_scrollbar.set)
    # Thêm các nút dưới bảng
    add_buttons_below_tree(parent_frame,tree)

# Mở cửa sổ và hiển thị bảng (không gọi)
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Panel 1")
    show_panel(root)
    root.mainloop()
