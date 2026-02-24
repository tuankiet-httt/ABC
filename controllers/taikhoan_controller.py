from models.taikhoan_model import TaiKhoan
from services.taikhoan_service import TaiKhoanService
from repository.nhanvien_repository import NhanVienRepository


class TaiKhoanController:
    def __init__(self, view):
        self.view = view
        self.service = TaiKhoanService()
        self.nv_repo = NhanVienRepository()
        ds_nv = self.nv_repo.get_all()
        self.view.nap_danh_sach_nhanvien(ds_nv)


        # Gán sự kiện cho nút trong View
        self.view.btn_them.config(command=self.them)
        self.view.btn_sua.config(command=self.sua)
        self.view.btn_xoa.config(command=self.xoa)
        self.view.btn_tim.config(command=self.tim_kiem)
        self.view.table.bind("<<TreeviewSelect>>", self.view.hien_thi_chi_tiet_form)

        # Lần đầu load dữ liệu
        self.hien_thi_danh_sach()

    def hien_thi_danh_sach(self):
        ds = self.service.lay_danh_sach()
        self.view.hien_thi_bang(ds)

    def them(self):
        data = self.view.get_form_data()
        tk = TaiKhoan(**data)
        self.service.them_taikhoan(tk)
        self.hien_thi_danh_sach()

    def sua(self):
        data = self.view.get_form_data()
        tk = TaiKhoan(**data)
        self.service.sua_taikhoan(tk)
        self.hien_thi_danh_sach()

    def xoa(self):
        data = self.view.get_form_data()
        self.service.xoa_taikhoan(data["TenDangNhap"])
        self.hien_thi_danh_sach()

    def tim_kiem(self):
        keyword = self.view.txt_tim.get()
        ds = self.service.tim_kiem(keyword)
        self.view.hien_thi_bang(ds)
