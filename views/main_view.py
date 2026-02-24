import customtkinter as ctk
from tkinter import Menu, messagebox

class MainView:
    def __init__(self, role, username):
        self.root = ctk.CTk()
        self.root.title("Hệ thống Quản Lý Dịch Vụ Nha Khoa")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)

        self.role = role
        self.username = username

        # --- Thanh tiêu đề ---
        top_frame = ctk.CTkFrame(self.root, fg_color="#1976D2", height=60)
        top_frame.pack(fill="x")

        ctk.CTkLabel(
            top_frame,
            text="HỆ THỐNG QUẢN LÝ DỊCH VỤ NHA KHOA",
            font=("Arial", 18, "bold"),
            text_color="white",
        ).place(x=20, y=15)

        ctk.CTkLabel(
            top_frame,
            text=f"Quyền: {self.role}",
            font=("Arial", 14),
            text_color="white",
        ).place(relx=0.9, y=20, anchor="center")

        # --- Khung chức năng bên trái ---
        left_frame = ctk.CTkFrame(self.root, width=200)
        left_frame.pack(side="left", fill="y")

        ctk.CTkLabel(left_frame, text="Menu chức năng", font=("Arial", 14, "bold")).pack(pady=10)

        self.btn_hethong = ctk.CTkButton(left_frame, text="Hệ thống", command=self.show_menu_hethong, width=150)
        self.btn_hethong.pack(pady=10)

        self.btn_quanly = ctk.CTkButton(left_frame, text="Quản lý", width=150, command=self.show_menu_quanly)
        self.btn_quanly.pack(pady=10)

        self.btn_thongke = ctk.CTkButton(left_frame, text="Thống kê", width=150, command=self.show_menu_thongke)
        self.btn_thongke.pack(pady=10)

        # --- Vùng chính ---
        self.main_content = ctk.CTkFrame(self.root, corner_radius=15)
        self.main_content.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(
            self.main_content,
            text="Chào mừng bạn đến với hệ thống!",
            font=("Arial", 16, "bold"),
            text_color="black"
        ).place(relx=0.5, rely=0.5, anchor="center")

        # --- Khóa quyền ---
        if self.role.lower() == "nhanvien":
            self.btn_quanly.configure(state="disabled")
            self.btn_thongke.configure(state="disabled")

        # --- Popup menu hệ thống ---
        self.menu_hethong = Menu(self.root, tearoff=0)
        self.menu_hethong.add_command(label="Đổi mật khẩu", command=self.on_doi_mat_khau)
        self.menu_hethong.add_command(label="Đăng xuất", command=self.on_dang_xuat)

        # --- THÊM MENU QUẢN LÝ ---
        self.menu_quanly = Menu(self.root, tearoff=0)
        self.menu_quanly.add_command(label="Quản lý hóa đơn", command=self.on_quanly_hoadon)
        self.menu_quanly.add_command(label="Quản lý dịch vụ", command=self.on_quanly_dichvu)
        self.menu_quanly.add_command(label="Quản lý nhân viên", command=self.on_quanly_nhanvien)
        self.menu_quanly.add_command(label="Quản lý tài khoản", command=self.on_quanly_taikhoan)

        # --- THÊM MENU THỐNG KÊ ---
        self.menu_thongke = Menu(self.root, tearoff=0)
        self.menu_thongke.add_command(label="Theo ngày", command=self.on_thongke_ngay)
        self.menu_thongke.add_command(label="Theo tuần", command=self.on_thongke_tuan)
        self.menu_thongke.add_command(label="Theo tháng", command=self.on_thongke_thang)

    def show_menu_hethong(self):
        x = self.btn_hethong.winfo_rootx()
        y = self.btn_hethong.winfo_rooty() + self.btn_hethong.winfo_height()
        self.menu_hethong.tk_popup(x, y)

    # --- THÊM HÀM HIỂN THỊ MENU QUẢN LÝ ---
    def show_menu_quanly(self):
        x = self.btn_quanly.winfo_rootx()
        y = self.btn_quanly.winfo_rooty() + self.btn_quanly.winfo_height()
        self.menu_quanly.tk_popup(x, y)

    # --- THÊM HÀM HIỂN THỊ MENU THỐNG KÊ ---
    def show_menu_thongke(self):
        x = self.btn_thongke.winfo_rootx()
        y = self.btn_thongke.winfo_rooty() + self.btn_thongke.winfo_height()
        self.menu_thongke.tk_popup(x, y)

    def on_dang_xuat(self):
        pass

    def on_doi_mat_khau(self):
        pass

    def cap_nhat_menu(self):
        """Cập nhật lại menu để dùng hàm từ MainController"""
        self.menu_hethong.delete(0, "end")
        self.menu_hethong.add_command(label="Đổi mật khẩu", command=self.on_doi_mat_khau)
        self.menu_hethong.add_command(label="Đăng xuất", command=self.on_dang_xuat)

    # --- THÊM CÁC HÀM CHỨC NĂNG QUẢN LÝ ---
    def on_quanly_hoadon(self):
        messagebox.showinfo("Quản lý hóa đơn", "Mở giao diện Quản lý hóa đơn")

    def on_quanly_dichvu(self):
        messagebox.showinfo("Quản lý dịch vụ", "Mở giao diện Quản lý dịch vụ")

    def on_quanly_nhanvien(self):
        messagebox.showinfo("Quản lý nhân viên", "Mở giao diện Quản lý nhân viên")

    def on_quanly_taikhoan(self):
        messagebox.showinfo("Quản lý tài khoản", "Mở giao diện Quản lý tài khoản")

    # --- THÊM CÁC HÀM THỐNG KÊ ---
    def on_thongke_ngay(self):
        messagebox.showinfo("Thống kê", "Hiển thị thống kê doanh thu theo ngày")

    def on_thongke_tuan(self):
        messagebox.showinfo("Thống kê", "Hiển thị thống kê doanh thu theo tuần")

    def on_thongke_thang(self):
        messagebox.showinfo("Thống kê", "Hiển thị thống kê doanh thu theo tháng")
