import tkinter as tk
from tkinter import ttk
from Threat_BLL import *
from Alert_BLL import *
from read_alert_to_threat import *
# Tam thoi ok, khong can sua them
class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản trị mạng")
        self.root.geometry("600x400")  # Tăng kích thước cửa sổ
        self.root.resizable(width=False, height=True)
        # Tạo thanh điều hướng bên trái
        self.navigation_frame = ttk.Frame(self.root, width=5)
        self.navigation_frame.grid(row=0, column=0, sticky="ns")
        self.navigation_frame.config(width=100, height=400)

        # Tạo khung viền cho nội dung bên phải
        self.content_frame_border = ttk.Frame(self.root, borderwidth=2, relief="ridge")
        self.content_frame_border.grid(row=0, column=1, sticky="nsew", padx=(0, 10),pady = (0,10))
        self.content_frame_border.config(width=500, height=400)
        self.content_frame_border.grid_propagate(False)
        # Tạo nội dung bên phải
        self.content_frame = ttk.Frame(self.content_frame_border)
        self.content_frame.pack(fill="both", expand=True)
        # Đặt trọng số để phân chia tỉ lệ 1:4
        self.root.grid_columnconfigure(0,  minsize=100)
        self.root.grid_columnconfigure(1, weight=5)  # Giảm trọng số để nội dung chiếm phần lớn
        self.root.grid_rowconfigure(0, weight=1)
        # Thêm các mục vào thanh điều hướng
        self.add_navigation_items()

    def add_navigation_items(self):
        items = ["Status", "Logs", "Threats"]

        for i, item in enumerate(items):
            button = ttk.Button(self.navigation_frame, text=item, command=lambda i=i: self.show_content(i+1))
            button.grid(row=i, column=0, sticky="ew")
        button = ttk.Button(self.navigation_frame, text="Reload", command= lambda: self.reload_on_click())
        button.grid(row = 4, column = 0, sticky= "s")

    def reload_on_click(self):
        # reload snort
        mf.reload_snort()
        # reload threat list
        Threat_BLL.update_threat_list()
        read_alert_to_threat()
        Threat_BLL.load_threat()
        print("Reloaded all")
        return "Reloaded"

    def show_content(self, item_number):
        # Xóa nội dung hiện tại
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Hiển thị nội dung mới tương ứng với mục được chọn
        if item_number == 1:
            self.load_panel("panel1.py")
        elif item_number == 2:
            self.load_panel("panel2.py")
        elif item_number == 3:
            self.load_panel("panel3.py")

    def load_panel(self, panel_filename):
        try:
            # Import module dynamically
            panel_module = __import__(panel_filename.replace(".py", ""))
            # Call a function (assuming there is a function named 'show_panel' in panel module)
            panel_module.show_panel(self.content_frame)
        except ImportError:
            # Handle import error
            print(f"Error loading panel: {panel_filename}")

if __name__ == "__main__":
    read_alert_to_threat()
    Threat_BLL()
    Alert_BLL()
    Threat_BLL.load_threat()

    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
    Threat_BLL.update_threat_list()
