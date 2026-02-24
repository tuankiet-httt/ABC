import os
import sys
import tkinter as tk
from tkinter import messagebox
from models.login_model import TaiKhoanModel
from views.login_view import LoginView
from controllers.login_controller import TaiKhoanController

class MainController:
    def __init__(self, view, username):
        self.view = view
        self.username = username
        self.model = TaiKhoanModel()

        self.view.on_dang_xuat = self.dang_xuat
        self.view.on_doi_mat_khau = self.doi_mat_khau
        self.view.cap_nhat_menu()

    def dang_xuat(self):
        """Xử lý đăng xuất"""
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn đăng xuất không?"):
            self.view.root.destroy()

            # 🔹 Khởi động lại toàn bộ chương trình (reset lại giao diện đẹp như ban đầu)
            python = sys.executable
            os.execl(python, python, *sys.argv)

    def doi_mat_khau(self):
        """Xử lý đổi mật khẩu"""
        from customtkinter import CTkInputDialog

        old_pass = CTkInputDialog(text="Nhập mật khẩu cũ:", title="Đổi mật khẩu").get_input()
        new_pass = CTkInputDialog(text="Nhập mật khẩu mới:", title="Đổi mật khẩu").get_input()

        if not old_pass or not new_pass:
            return

        if self.model.doi_mat_khau(self.username, old_pass, new_pass):
            messagebox.showinfo("Thành công", "Đổi mật khẩu thành công!")
        else:
            messagebox.showerror("Lỗi", "Mật khẩu cũ không đúng!")
