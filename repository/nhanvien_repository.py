from data.dataconnection3 import DataConnection

class NhanVienRepository:
    def __init__(self):
        self.db = DataConnection()

    def get_all(self):
        with self.db.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT MaNV, TenNV FROM NhanVien")
            return cur.fetchall()
