import tkinter as tk
from tkinter import ttk


def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Chuyển đổi dữ liệu từ file txt thành danh sách các tuple
        data = [tuple(line.strip().split(',')) for line in lines]
    return data

def on_button1_click(tree):
    print("Button 1 clicked")
    selected_item = tree.selection()
    if selected_item:
        item_values = tree.item(selected_item, 'values')
        source_ip = item_values[0]
        print(f"Đã chọn đối tượng với Source IP: {source_ip}")
    else:
        print("No item selected")

def on_button2_click():
    print("Button 2 clicked")

def on_button3_click():
    print("Button 3 clicked")

def on_button4_click():
    print("Button 4 clicked")

def add_buttons_below_tree(parent_frame,tree):
    button_frame = ttk.Frame(parent_frame)
    button_frame.pack()

    button1 = ttk.Button(button_frame, text="Button 1", command= lambda: on_button1_click(tree))
    button1.grid(row=0, column=0, padx=5)

    button2 = ttk.Button(button_frame, text="Button 2", command=on_button2_click)
    button2.grid(row=0, column=1, padx=5)

    button3 = ttk.Button(button_frame, text="Button 3", command=on_button3_click)
    button3.grid(row=0, column=2, padx=5)

    button4 = ttk.Button(button_frame, text="Button 4", command=on_button4_click)
    button4.grid(row=0, column=3, padx=5)

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

    x_scrollbar = ttk.Scrollbar(parent_frame, orient="horizontal", command=tree.xview)
    x_scrollbar.pack(side="bottom", fill="x")

    # Tạo một cột ảo với chiều rộng lớn để tạo nút cuộn ngang

    # Kết nối thanh cuộn ngang với cột ảo
    tree.configure(xscrollcommand=x_scrollbar.set)
    # Thêm các nút dưới bảng
    add_buttons_below_tree(parent_frame,tree)

# Mở cửa sổ và hiển thị bảng
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Panel 1")

    # Chỉ cần gọi hàm show_panel với đường dẫn đến file txt
    show_panel(root)

    root.mainloop()
