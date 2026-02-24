import tkinter as tk
from views.login_view import LoginView
from controllers.login_controller import TaiKhoanController

def main():
    root = tk.Tk()
    view = LoginView(root)
    TaiKhoanController(view)
    root.mainloop()

if __name__ == "__main__":
    main()
