import tkinter as tk
from tkinter import ttk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My App")
        self.root.geometry("600x400")

        # Tạo thanh điều hướng bên trái
        self.navigation_frame = ttk.Frame(self.root, width=150)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")

        # Tạo nội dung bên phải
        self.content_frame = ttk.Frame(self.root)
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        # Đặt trọng số để phân chia tỉ lệ 1:4
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=4)

        # Thêm các mục vào thanh điều hướng
        self.add_navigation_items()

    def add_navigation_items(self):
        items = ["Item 1", "Item 2", "Item 3"]

        for i, item in enumerate(items):
            button = ttk.Button(self.navigation_frame, text=item, command=lambda i=i: self.show_content(i+1))
            button.grid(row=i, column=0, sticky="ew")

    def show_content(self, item_number):
        # Xóa nội dung hiện tại
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Hiển thị nội dung mới tương ứng với mục được chọn
        content_label = ttk.Label(self.content_frame, text=f"Content for Item {item_number}")
        content_label.pack(expand=True, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
