from models.dichvu_model import DichVu
from services.dichvu_service import DichVuService

class DichVuController:
    def __init__(self, view):
        self.view = view
        self.service = DichVuService()
        self.view.btn_timkiem.config(command=self.tim_kiem)


        # Gán sự kiện cho nút
        self.view.btn_them.config(command=self.them)
        self.view.btn_sua.config(command=self.sua)
        self.view.btn_xoa.config(command=self.xoa)
        self.view.table.bind("<<TreeviewSelect>>", self.hien_thi_chi_tiet)

        # Load dữ liệu ban đầu
        self.hien_thi_ds()

    def hien_thi_ds(self):
        dichvus = self.service.lay_danh_sach()
        self.view.hien_thi_bang(dichvus)

    def them(self):
        ten = self.view.txt_tendv.get()
        gia = self.view.txt_giatien.get()
        dv = DichVu(tendv=ten, giatien=gia)
        self.service.them_dichvu(dv)
        self.hien_thi_ds()

    def sua(self):
        madv = self.view.txt_madv.get()
        ten = self.view.txt_tendv.get()
        gia = self.view.txt_giatien.get()
        dv = DichVu(madv=madv, tendv=ten, giatien=gia)
        self.service.sua_dichvu(dv)
        self.hien_thi_ds()

    def xoa(self):
        madv = self.view.txt_madv.get()
        self.service.xoa_dichvu(madv)
        self.hien_thi_ds()

    def hien_thi_chi_tiet(self, event):
        self.view.hien_thi_chi_tiet_form()

    def tim_kiem(self):
        keyword = self.view.txt_timkiem.get()
        ds = self.service.tim_kiem_dichvu(keyword)
        self.view.hien_thi_bang(ds)

