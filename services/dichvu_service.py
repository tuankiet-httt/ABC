from repository.dichvu_repository import DichVuRepository

class DichVuService:
    def __init__(self):
        self.repo = DichVuRepository()

    def lay_danh_sach(self):
        return self.repo.get_all()

    def them_dichvu(self, dichvu):
        if not dichvu.TenDV:
            raise ValueError("Tên dịch vụ không được để trống")
        self.repo.insert(dichvu)

    def sua_dichvu(self, dichvu):
        if dichvu.MaDV is None:
            raise ValueError("Thiếu mã dịch vụ khi cập nhật")
        self.repo.update(dichvu)

    def xoa_dichvu(self, MaDV):
        self.repo.delete(MaDV)

    def tim_kiem_dichvu(self, keyword):
        if not keyword:
            # Nếu không nhập gì thì trả về tất cả
            return self.repo.get_all()
        return self.repo.search(keyword)

