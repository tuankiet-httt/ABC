from data.dataconnection import DataConnection
from models.khachhang_model import KhachHang

class KhachHangRepository:
    def get_all(self):
        conn = DataConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM KhachHang")
        rows = cursor.fetchall()
        conn.close()
        return [KhachHang(*row) for row in rows]

    def add(self, kh):
        conn = DataConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO KhachHang (TenKH, GioiTinh, SoDT) VALUES (?, ?, ?)",
            (kh.TenKH, kh.GioiTinh, kh.SoDT)
        )
        conn.commit()
        conn.close()

    def update(self, kh):
        conn = DataConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE KhachHang SET TenKH=?, GioiTinh=?, SoDT=? WHERE MaKH=?",
            (kh.TenKH, kh.GioiTinh, kh.SoDT, kh.MaKH)
        )
        conn.commit()
        conn.close()

    def delete(self, MaKH):
        conn = DataConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM KhachHang WHERE MaKH=?", (MaKH,))
        conn.commit()
        conn.close()

    def search(self, keyword):
        conn = DataConnection.get_connection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM KhachHang
            WHERE CAST(MaKH AS NVARCHAR) LIKE ? OR TenKH LIKE ?
        """
        like_kw = f"%{keyword}%"
        cursor.execute(query, (like_kw, like_kw))
        rows = cursor.fetchall()
        conn.close()
        return [KhachHang(*row) for row in rows]
