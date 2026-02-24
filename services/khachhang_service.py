from repository.khachhang_repository import KhachHangRepository

class KhachHangService:
    def __init__(self):
        self.repo = KhachHangRepository()

    def lay_danh_sach(self):
        return self.repo.get_all()

    def them(self, kh):
        self.repo.add(kh)

    def sua(self, kh):
        self.repo.update(kh)

    def xoa(self, makh):
        self.repo.delete(makh)

    def tim_kiem(self, keyword):
        return self.repo.search(keyword)

