from data.dataconnection2 import DataConnection
from models.dichvu_model import DichVu

class DichVuRepository:
    def __init__(self):
        self.db = DataConnection()

    def get_all(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM DichVu")
        result = [DichVu(row.MaDV, row.TenDV, row.GiaTien) for row in cursor.fetchall()]
        conn.close()
        return result

    def insert(self, dichvu):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO DichVu (TenDV, GiaTien) VALUES (?, ?)",
            (dichvu.TenDV, dichvu.GiaTien)
        )
        conn.commit()
        conn.close()

    def update(self, dichvu):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE DichVu SET TenDV=?, GiaTien=? WHERE MaDV=?",
            (dichvu.TenDV, dichvu.GiaTien, dichvu.MaDV)
        )
        conn.commit()
        conn.close()

    def delete(self, madv):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM DichVu WHERE MaDV=?", (madv,))
        conn.commit()
        conn.close()

    def search(self, keyword):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM DichVu 
            WHERE CAST(MaDV AS NVARCHAR) LIKE ? OR TenDV LIKE ?
        """
        param = (f"%{keyword}%", f"%{keyword}%")
        cursor.execute(query, param)
        result = [DichVu(row.MaDV, row.TenDV, row.GiaTien) for row in cursor.fetchall()]
        conn.close()
        return result
