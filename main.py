import tkinter as tk
from views.khachhang_view import KhachHangView
from controllers.khachhang_controller import KhachHangController

if __name__ == "__main__":
    root = tk.Tk()
    view = KhachHangView(root)
    controller = KhachHangController(view)
    root.mainloop()
