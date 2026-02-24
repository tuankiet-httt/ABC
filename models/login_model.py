from data.dataconnection4 import DataConnection

class TaiKhoanModel:
    def __init__(self):
        db = DataConnection()
        self.conn = db.get_connection()

    def kiem_tra_dang_nhap(self, username, password):
        cursor = self.conn.cursor()
        query = "SELECT TenDangNhap, MatKhau, LoaiNguoiDung FROM TaiKhoan WHERE TenDangNhap = ? AND MatKhau = ?"
        cursor.execute(query, (username, password))
        row = cursor.fetchone()
        if row:
            return {"username": row[0], "role": row[2]}
        return None
    
    def doi_mat_khau(self, username, old_pass, new_pass):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM TaiKhoan WHERE TenDangNhap=? AND MatKhau=?", (username, old_pass))
        if cursor.fetchone():
            cursor.execute("UPDATE TaiKhoan SET MatKhau=? WHERE TenDangNhap=?", (new_pass, username))
            self.conn.commit()
            return True
        return False
