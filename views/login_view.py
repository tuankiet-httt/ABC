import customtkinter as ctk
from tkinter import messagebox

class LoginView:
    def __init__(self, root):
        ctk.set_appearance_mode("light")          # giao diện sáng
        ctk.set_default_color_theme("blue")       # tone xanh dương

        self.root = root
        self.root.title("Đăng nhập hệ thống")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # ---- Khung chính ----
        frame = ctk.CTkFrame(self.root, corner_radius=15)
        frame.pack(pady=40, padx=60, fill="both", expand=True)

        title = ctk.CTkLabel(frame, text="Đăng nhập", font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=(20, 15))

        # ---- Nhập tài khoản ----
        self.txt_taikhoan = ctk.CTkEntry(frame, placeholder_text="Tên đăng nhập", width=220)
        self.txt_taikhoan.pack(pady=8)

        # ---- Nhập mật khẩu ----
        self.txt_matkhau = ctk.CTkEntry(frame, placeholder_text="Mật khẩu", show="*", width=220)
        self.txt_matkhau.pack(pady=8)

        # ---- Nút đăng nhập ----
        self.btn_dangnhap = ctk.CTkButton(frame, text="Đăng nhập", width=120, height=32)
        self.btn_dangnhap.pack(pady=20)
