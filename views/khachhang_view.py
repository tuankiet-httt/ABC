import tkinter as tk
from tkinter import ttk
from models.khachhang_model import KhachHang

class KhachHangView:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản Lý Khách Hàng")

        # --- Khu vực tìm kiếm ---
        tk.Label(root, text="Tìm (Mã/Tên):").grid(row=0, column=0)
        self.txt_timkiem = tk.Entry(root)
        self.txt_timkiem.grid(row=0, column=1)
        self.btn_timkiem = tk.Button(root, text="Tìm kiếm")
        self.btn_timkiem.grid(row=0, column=2)
        self.btn_hienthi = tk.Button(root, text="Hiển thị tất cả")
        self.btn_hienthi.grid(row=0, column=3)

        # --- Form nhập ---
        tk.Label(root, text="Tên KH:").grid(row=1, column=0)
        tk.Label(root, text="Giới Tính:").grid(row=2, column=0)
        tk.Label(root, text="Số ĐT:").grid(row=3, column=0)

        self.txt_ten = tk.Entry(root)
        self.txt_gt = tk.Entry(root)
        self.txt_sdt = tk.Entry(root)
        self.txt_ten.grid(row=1, column=1)
        self.txt_gt.grid(row=2, column=1)
        self.txt_sdt.grid(row=3, column=1)

        # --- Nút thao tác ---
        self.btn_them = tk.Button(root, text="Thêm")
        self.btn_sua = tk.Button(root, text="Sửa")
        self.btn_xoa = tk.Button(root, text="Xóa")
        self.btn_them.grid(row=4, column=0)
        self.btn_sua.grid(row=4, column=1)
        self.btn_xoa.grid(row=4, column=2)

        # --- Bảng ---
        self.tree = ttk.Treeview(root, columns=("makh", "ten", "gt", "sdt"), show="headings")
        self.tree.heading("makh", text="Mã KH")
        self.tree.heading("ten", text="Tên KH")
        self.tree.heading("gt", text="Giới Tính")
        self.tree.heading("sdt", text="Số ĐT")
        self.tree.grid(row=5, column=0, columnspan=4)

        self.selected_makh = None

    # --- Các hàm hỗ trợ Controller ---
    def hien_thi_danh_sach(self, ds):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for kh in ds:
            self.tree.insert("", "end", values=(kh.MaKH, kh.TenKH, kh.GioiTinh, kh.SoDT))

    def lay_du_lieu_tu_form(self):
        return KhachHang(
            MaKH=self.selected_makh,
            TenKH=self.txt_ten.get(),
            GioiTinh=self.txt_gt.get(),
            SoDT=self.txt_sdt.get()
        )

    def cap_nhat_form_tu_bang(self):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")
            self.selected_makh = values[0]
            self.txt_ten.delete(0, tk.END)
            self.txt_ten.insert(0, values[1])
            self.txt_gt.delete(0, tk.END)
            self.txt_gt.insert(0, values[2])
            self.txt_sdt.delete(0, tk.END)
            self.txt_sdt.insert(0, values[3])

    def lay_makh_chon(self):
        return self.selected_makh

    def lay_tu_khoa_tim_kiem(self):
        return self.txt_timkiem.get()
