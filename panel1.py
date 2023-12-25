import tkinter as tk
from tkinter import ttk

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Chuyển đổi dữ liệu từ file txt thành danh sách các tuple
        data = [tuple(line.strip().split(',')) for line in lines]
    return data

def show_panel(parent_frame):
    # Đọc dữ liệu từ file
    file_path = "threats.txt"
    data_from_file = read_data_from_file(file_path)

    # Tạo Treeview để hiển thị bảng
    tree = ttk.Treeview(parent_frame, columns=("Source IP", "Destination IP", "Protocol", "Size", "Success"))

    # Đặt tên cột và định dạng
    tree.heading("#0", text="Index")
    tree.column("#0", width=50)
    tree.heading("Source IP", text="Source IP")
    tree.column("Source IP", width=120)
    tree.heading("Destination IP", text="Destination IP")
    tree.column("Destination IP", width=120)
    tree.heading("Protocol", text="Protocol")
    tree.column("Protocol", width=80)
    tree.heading("Size", text="Size")
    tree.column("Size", width=80)
    tree.heading("Success", text="Success")
    tree.column("Success", width=80)

    # Đặt dữ liệu vào bảng
    for i, row in enumerate(data_from_file):
        tree.insert("", i, text=str(i), values=row)

    # Hiển thị Treeview
    tree.pack(expand=True, fill="both")

# Mở cửa sổ và hiển thị bảng
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Panel 1")

    # Chỉ cần gọi hàm show_panel với đường dẫn đến file txt
    show_panel(root, "threats.txt")

    root.mainloop()
