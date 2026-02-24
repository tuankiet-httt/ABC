from data.dataconnection3 import DataConnection
from models.taikhoan_model import TaiKhoan

class TaiKhoanRepository:
    def __init__(self):
        self.db = DataConnection()

    def get_all(self):
        with self.db.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT TenDangNhap, MatKhau, LoaiNguoiDung, MaNV FROM TaiKhoan")
            rows = cur.fetchall()
            return [TaiKhoan(*r) for r in rows]

    def add(self, tk):
        with self.db.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO TaiKhoan (TenDangNhap, MatKhau, LoaiNguoiDung, MaNV) VALUES (?, ?, ?, ?)",
                (tk.TenDangNhap, tk.MatKhau, tk.LoaiNguoiDung, tk.MaNV)
            )
            conn.commit()

    def update(self, tk):
        with self.db.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                "UPDATE TaiKhoan SET MatKhau=?, LoaiNguoiDung=?, MaNV=? WHERE TenDangNhap=?",
                (tk.MatKhau, tk.LoaiNguoiDung, tk.MaNV, tk.TenDangNhap)
            )
            conn.commit()

    def delete(self, TenDangNhap):
        with self.db.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM TaiKhoan WHERE TenDangNhap=?", (TenDangNhap,))
            conn.commit()

    def search(self, keyword):
        with self.db.get_connection() as conn:
            cur = conn.cursor()
            sql = """
                SELECT TenDangNhap, MatKhau, LoaiNguoiDung, MaNV
                FROM TaiKhoan
                WHERE TenDangNhap LIKE ? OR LoaiNguoiDung LIKE ?
            """
            cur.execute(sql, (f"%{keyword}%", f"%{keyword}%"))
            rows = cur.fetchall()
            return [TaiKhoan(*r) for r in rows]
