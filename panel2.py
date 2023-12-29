import tkinter as tk
from tkinter import ttk
from Alert_BLL import *
import plot


def read_data_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        # Chuyển đổi dữ liệu từ file txt thành danh sách các tuple
        data = [tuple(line.strip().split(",")) for line in lines]
    return data


def add_buttons_below_tree(parent_frame, child_frame):
    items = ["Treeview", "Protocol_plot", "Threats"]
    button_frame = ttk.Frame(parent_frame)
    button_frame.pack()
    for i, item in enumerate(items):
        button = ttk.Button(
            button_frame, text=item, command=lambda i=i: click(child_frame, i + 1)
        )
        button.grid(row=0, column=i, padx=5)


def create_Treeview(child_frame):
    tree = ttk.Treeview(
        child_frame,
        columns=(
            "Timestamp",
            "Action",
            "Protocol",
            "Gid",
            "Sid",
            "Rev",
            "Message",
            "Service",
            "Source IP",
            "Source Port",
            "Destination IP",
            "Destination Port",
        ),
    )
    # Đặt tên cột và định dạng
    tree.heading("#0", text="Index")
    tree.column("#0", width=50)
    tree.heading("Timestamp", text="Timestamp")
    tree.column("Timestamp", width=120)
    tree.heading("Action", text="Action")
    tree.column("Action", width=120)
    tree.heading("Protocol", text="Protocol")
    tree.column("Protocol", width=80)
    tree.heading("Gid", text="Gid")
    tree.column("Gid", width=80)
    tree.heading("Sid", text="Sid")
    tree.column("Sid", width=80)
    tree.heading("Rev", text="Rev")
    tree.column("Rev", width=80)
    tree.heading("Message", text="Message")
    tree.column("Message", width=80)
    tree.heading("Service", text="Service")
    tree.column("Service", width=80)
    tree.heading("Source IP", text="Source IP")
    tree.column("Source IP", width=80)
    tree.heading("Source Port", text="Source Port")
    tree.column("Source Port", width=80)
    tree.heading("Destination IP", text="Destination IP")
    tree.column("Destination IP", width=80)
    tree.heading("Destination Port", text="Destination Port")
    tree.column("Destination Port", width=80)

    # Đặt dữ liệu vào bảng
    # for i, row in enumerate(data_from_file):
    #     tree.insert("", i, text=str(i), values=row)
    for i, alert in enumerate(Alert_BLL.to_tuples()):
        tree.insert("", i, text=str(i), values=alert)
    # Hiển thị Treeview
    tree.pack(expand=True, fill="both")

    x_scrollbar = ttk.Scrollbar(child_frame, orient="horizontal", command=tree.xview)
    x_scrollbar.pack(side="bottom", fill="x")

    # Tạo một cột ảo với chiều rộng lớn để tạo nút cuộn ngang

    # Kết nối thanh cuộn ngang với cột ảo
    tree.configure(xscrollcommand=x_scrollbar.set)
    return tree


def click(child_frame, item_id):
    # Xóa nội dung hiện tại
    for widget in child_frame.winfo_children():
        widget.destroy()
    # Hiển thị nội dung mới tương ứng với mục được chọn
    if item_id == 1:
        create_Treeview(child_frame)
    elif item_id == 2:
        plot.Protocol_plot(child_frame)
    elif item_id == 3:
        create_Treeview(child_frame)


def show_panel(parent_frame):
    # Đọc dữ liệu từ file

    # Tạo frame con
    child_frame = ttk.Frame(parent_frame)
    child_frame.pack(fill="both", expand=True)
    # Tạo Treeview để hiển thị bảng
    # tree = create_Treeview(parent_frame)
    # Thêm các nút dưới bảng
    add_buttons_below_tree(parent_frame, child_frame)


# Mở cửa sổ và hiển thị bảng (không gọi)
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Panel 1")
    # Chỉ cần gọi hàm show_panel với đường dẫn đến file txt
    show_panel(root)

    root.mainloop()
