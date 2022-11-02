from pydantic import BaseModel , EmailStr
from typing import Optional

class Siswa(BaseModel):
    nama : str
    jurusan :str
    kelas :int
    alamat: str
    jenis_kelamin: str
    
    class Config:
        schema_extra = {
            "example": {
                "nama": "Airin",
                "jurusan": "Rekayasa Perangkat Lunak",
                "kelas": 11,
                "alamat": "Cimareme",
                "jenis_kelamin": "Laki-Laki"
            }
        }

class UpdatedSiswa(BaseModel):
    nama : Optional[str] = ''
    jurusan :Optional[str] = ''
    kelas :Optional[int] = 0
    alamat: Optional[str] = ''
    jenis_kelamin: Optional[str] = ''
    
    class Config:
        schema_extra = {
            "example": {
                "nama": "",
                "jurusan": "",
                "kelas": 0,
                "alamat": "",
                "jenis_kelamin": ""
            }
        }

class Nilai(BaseModel):
    nilai:int
    class Config:
        schema_extra = {
            "example": {
                "nilai": 80
            }
        }

class SiswaOut(Siswa):
    id:str
    nilai:list

class NilaiOut(BaseModel):
    id:str
    nama:str
    nilai:list
    