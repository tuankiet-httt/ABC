from tkinter import messagebox
from views.main_view import MainView
from models.login_model import TaiKhoanModel

class TaiKhoanController:
    def __init__(self, view):
        self.view = view
        self.model = TaiKhoanModel()
        self.view.btn_dangnhap.configure(command=self.dang_nhap)

    def dang_nhap(self):
        from controllers.main_controller import MainController  # ✅ import ở đây để tránh vòng lặp

        username = self.view.txt_taikhoan.get()
        password = self.view.txt_matkhau.get()

        if not username or not password:
            messagebox.showwarning("Thông báo", "Vui lòng nhập đủ thông tin!")
            return

        user = self.model.kiem_tra_dang_nhap(username, password)
        if user:
            messagebox.showinfo("Đăng nhập thành công", f"Xin chào {user['username']} ({user['role']})")
            self.view.root.destroy()

            view = MainView(user['role'], username)
            MainController(view, username)
            view.root.mainloop()  # ✅ gọi mainloop() ở đây

        else:
            messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu!")
