import tkinter as tk
from tkinter import ttk

class TaiKhoanView:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý ")

        frm = tk.Frame(root)
        frm.pack(pady=10)

        tk.Label(frm, text="Tên đăng nhập").grid(row=0, column=0)
        self.txt_tendn = tk.Entry(frm)
        self.txt_tendn.grid(row=0, column=1)

        tk.Label(frm, text="Mật khẩu").grid(row=1, column=0)
        self.txt_matkhau = tk.Entry(frm, show="*")
        self.txt_matkhau.grid(row=1, column=1)

        tk.Label(frm, text="Loại người dùng").grid(row=2, column=0)
        self.cbo_loai = ttk.Combobox(frm, values=["Admin", "NhanVien"], state="readonly")
        self.cbo_loai.grid(row=2, column=1)

        tk.Label(frm, text="Nhân viên").grid(row=3, column=0)
        self.cbo_nhanvien = ttk.Combobox(frm, state="readonly")
        self.cbo_nhanvien.grid(row=3, column=1)


        # Tìm kiếm
        tk.Label(frm, text="Tìm kiếm").grid(row=5, column=0)
        self.txt_tim = tk.Entry(frm)
        self.txt_tim.grid(row=5, column=1)

        # Nút chức năng
        self.btn_them = tk.Button(frm, text="Thêm")
        self.btn_sua = tk.Button(frm, text="Sửa")
        self.btn_xoa = tk.Button(frm, text="Xóa")
        self.btn_tim = tk.Button(frm, text="Tìm kiếm")
        self.btn_them.grid(row=4, column=0, pady=5)
        self.btn_sua.grid(row=4, column=1, pady=5)
        self.btn_xoa.grid(row=4, column=2, pady=5)
        self.btn_tim.grid(row=5, column=2, pady=5)

        # Bảng
        self.table = ttk.Treeview(root, columns=("TenDangNhap", "MatKhau", "LoaiNguoiDung", "MaNV"), show="headings")
        for col, text in zip(("TenDangNhap", "MatKhau", "LoaiNguoiDung", "MaNV"),
                            ("Tên đăng nhập", "Mật khẩu", "Loại ND", "Mã NV")):
            self.table.heading(col, text=text)
        self.table.pack(fill="both", expand=True, pady=10)

    def hien_thi_bang(self, ds_tk):
        for row in self.table.get_children():
            self.table.delete(row)
        for tk in ds_tk:
            self.table.insert("", "end", values=(tk.TenDangNhap, tk.MatKhau, tk.LoaiNguoiDung, tk.MaNV))

    def get_form_data(self):
        return {
            "TenDangNhap": self.txt_tendn.get(),
            "MatKhau": self.txt_matkhau.get(),
            "LoaiNguoiDung": self.cbo_loai.get(),
            "MaNV": self.txt_manv.get(),
        }

    def hien_thi_chi_tiet_form(self, event=None):
        selected = self.table.focus()
        if not selected:
            return
        values = self.table.item(selected, "values")
        self.txt_tendn.delete(0, tk.END)
        self.txt_matkhau.delete(0, tk.END)
        self.txt_manv.delete(0, tk.END)
        self.txt_tendn.insert(0, values[0])
        self.txt_matkhau.insert(0, values[1])
        self.cbo_loai.set(values[2])
        self.txt_manv.insert(0, values[3])

    def nap_danh_sach_nhanvien(self, ds_nv):
        """
        ds_nv: danh sách tuple (MaNV, HoTen)
        """
        self.cbo_nhanvien["values"] = [nv[1] for nv in ds_nv]  # hiển thị tên
        self._nv_map = {nv[1]: nv[0] for nv in ds_nv}          # map tên -> mã

def get_form_data(self):
    ten_nv = self.cbo_nhanvien.get()
    ma_nv = self._nv_map.get(ten_nv, None)
    return {
        "TenDangNhap": self.txt_tendn.get(),
        "MatKhau": self.txt_matkhau.get(),
        "LoaiNguoiDung": self.cbo_loai.get(),
        "MaNV": ma_nv,
    }

def hien_thi_chi_tiet_form(self, event=None):
    selected = self.table.focus()
    if not selected:
        return
    values = self.table.item(selected, "values")
    self.txt_tendn.delete(0, tk.END)
    self.txt_matkhau.delete(0, tk.END)
    self.txt_tendn.insert(0, values[0])
    self.txt_matkhau.insert(0, values[1])
    self.cbo_loai.set(values[2])

    # Tự động chọn tên nhân viên tương ứng
    if hasattr(self, "_nv_map"):
        for ten, ma in self._nv_map.items():
            if str(ma) == str(values[3]):
                self.cbo_nhanvien.set(ten)
                break

