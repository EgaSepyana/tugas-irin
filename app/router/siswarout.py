from fastapi import APIRouter , HTTPException , status
from typing import List
import uuid
from .. import schema
from ..fakeDatabase import fake_db , find_siswa

router = APIRouter(
    prefix="/siswa",
    tags=["Siswa"]
)

@router.get("/", response_model=List[schema.SiswaOut])
async def get_siswa():
    return fake_db

@router.get("/{id}")
async def get_siswa_by_id(id:str):
    data,i = await find_siswa(id,fake_db)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Has Not Found")

    return data

@router.post("/", response_model=schema.SiswaOut)
async def add_siswa(post:schema.Siswa):
    siswa = post.dict()
    siswa["id"] = uuid.uuid4().hex
    siswa["nilai"] = []
    fake_db.append(siswa)
    return siswa

@router.put("/{id}", response_model=schema.SiswaOut)
async def update_siswa(id:str, payload:schema.UpdatedSiswa):
    old_data,index = await find_siswa(id,fake_db)
    if not old_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Has Not Found")

    nama = old_data.get('nama') if not payload.nama else payload.nama
    jurusan = old_data.get('jurusan') if not payload.jurusan else payload.jurusan
    kelas = old_data.get('kelas') if not payload.kelas else payload.kelas
    alamat = old_data.get('alamat') if not payload.alamat else payload.alamat
    jenis_kelamin = old_data.get('jenis_kelamin') if not payload.jenis_kelamin else payload.jenis_kelamin

    fake_db[index]["nama"] = nama
    fake_db[index]["jurusan"] = jurusan
    fake_db[index]["kelas"] = kelas
    fake_db[index]["alamat"] = alamat
    fake_db[index]["jenis_kelamin"] = jenis_kelamin
    
    return fake_db[index]
    


# @router.post("siswa/nilai/{id}")
# async def add_nilai_to_siswa(id:str,nilai:schema.Nilai):
#     siswa = await find_siswa(id,fake_db)
#     if not siswa:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Siswa Does't Not Exist")
#     nilai_siswa:dict = siswa.get("nilai")
#     nilai_siswa[nilai.keterangan_nilai] = nilai.nilai