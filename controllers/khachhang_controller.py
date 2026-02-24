from services.khachhang_service import KhachHangService
from models.khachhang_model import KhachHang

class KhachHangController:
    def __init__(self, view):
        self.view = view
        self.service = KhachHangService()

        # Gán sự kiện nút của View
        self.view.btn_them.config(command=self.them)
        self.view.btn_sua.config(command=self.sua)
        self.view.btn_xoa.config(command=self.xoa)
        self.view.btn_timkiem.config(command=self.tim_kiem)
        self.view.btn_hienthi.config(command=self.load_data)
        self.view.tree.bind("<<TreeviewSelect>>", self.on_row_selected)

        # Load ban đầu
        self.load_data()

    def load_data(self):
        ds = self.service.lay_danh_sach()
        self.view.hien_thi_danh_sach(ds)

    def them(self):
        kh = self.view.lay_du_lieu_tu_form()
        self.service.them(kh)
        self.load_data()

    def sua(self):
        kh = self.view.lay_du_lieu_tu_form()
        self.service.sua(kh)
        self.load_data()

    def xoa(self):
        makh = self.view.lay_makh_chon()
        if makh:
            self.service.xoa(makh)
            self.load_data()

    def tim_kiem(self):
        keyword = self.view.lay_tu_khoa_tim_kiem()
        ds = self.service.tim_kiem(keyword)
        self.view.hien_thi_danh_sach(ds)

    def on_row_selected(self, event):
        self.view.cap_nhat_form_tu_bang()
