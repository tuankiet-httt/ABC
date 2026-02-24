import tkinter as tk
from views.taikhoan_view import TaiKhoanView
from controllers.taikhoan_controller import TaiKhoanController

if __name__ == "__main__":
    root = tk.Tk()
    view = TaiKhoanView(root)
    controller = TaiKhoanController(view)
    root.mainloop()
