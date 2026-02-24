from repository.taikhoan_repository import TaiKhoanRepository

class TaiKhoanService:
    def __init__(self):
        self.repo = TaiKhoanRepository()

    def lay_danh_sach(self):
        return self.repo.get_all()

    def them_taikhoan(self, tk):
        self.repo.add(tk)

    def sua_taikhoan(self, tk):
        self.repo.update(tk)

    def xoa_taikhoan(self, TenDangNhap):
        self.repo.delete(TenDangNhap)

    def tim_kiem(self, keyword):
        return self.repo.search(keyword)
