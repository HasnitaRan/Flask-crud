from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class WasteBankModel(db.Model):
    __tablename__ = "wastebank"
    
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String())
    jenis = db.Column(db.String())
    harga = db.Column(db.String())
    
    def __init__(self, nama, jenis, harga):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        
        def __repr__(self):
            return f"{self.nama}:{self.jenis}"
        