import tkinter as tk
from tkinter import ttk

class DichVuView:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("Quản lý Dịch vụ Nha khoa")

                # Ô tìm kiếm
        frm_search = tk.Frame(root)
        frm_search.pack(pady=5)

        tk.Label(frm_search, text="Tìm kiếm (Mã hoặc Tên DV):").pack(side=tk.LEFT)
        self.txt_timkiem = tk.Entry(frm_search, width=30)
        self.txt_timkiem.pack(side=tk.LEFT, padx=5)
        self.btn_timkiem = tk.Button(frm_search, text="Tìm kiếm")
        self.btn_timkiem.pack(side=tk.LEFT)


        # Form
        frm = tk.Frame(root)
        frm.pack(pady=10)

        tk.Label(frm, text="Mã DV").grid(row=0, column=0)
        self.txt_madv = tk.Entry(frm)
        self.txt_madv.grid(row=0, column=1)

        tk.Label(frm, text="Tên DV").grid(row=1, column=0)
        self.txt_tendv = tk.Entry(frm)
        self.txt_tendv.grid(row=1, column=1)

        tk.Label(frm, text="Giá Tiền").grid(row=2, column=0)
        self.txt_giatien = tk.Entry(frm)
        self.txt_giatien.grid(row=2, column=1)

        # Nút
        self.btn_them = tk.Button(frm, text="Thêm")
        self.btn_sua = tk.Button(frm, text="Sửa")
        self.btn_xoa = tk.Button(frm, text="Xóa")
        self.btn_them.grid(row=3, column=0)
        self.btn_sua.grid(row=3, column=1)
        self.btn_xoa.grid(row=3, column=2)

        # Bảng
        self.table = ttk.Treeview(root, columns=("MaDV", "TenDV", "GiaTien"), show="headings")
        self.table.heading("MaDV", text="Mã DV")
        self.table.heading("TenDV", text="Tên Dịch Vụ")
        self.table.heading("GiaTien", text="Giá Tiền")
        self.table.pack(fill="both", expand=True)

        self.controller = controller  # controller điều khiển view

    def hien_thi_bang(self, ds_dv):
        for row in self.table.get_children():
            self.table.delete(row)
        for dv in ds_dv:
            self.table.insert("", "end", values=(dv.MaDV, dv.TenDV, dv.GiaTien))

    def hien_thi_chi_tiet_form(self):
        selected = self.table.focus()
        if not selected:
            return
        values = self.table.item(selected, "values")
        self.txt_madv.delete(0, tk.END)
        self.txt_tendv.delete(0, tk.END)
        self.txt_giatien.delete(0, tk.END)
        self.txt_madv.insert(0, values[0])
        self.txt_tendv.insert(0, values[1])
        self.txt_giatien.insert(0, values[2])
