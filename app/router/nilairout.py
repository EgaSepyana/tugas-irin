from fastapi import APIRouter , HTTPException , status, Response
from .. import schema
from ..fakeDatabase import fake_db , find_siswa, get_nilai_info, get_max_len_nilai

router = APIRouter(
    prefix="/nilai",
    tags=["Nilai"]
)

@router.post("/{id}",response_model=schema.NilaiOut)
async def add_nilai_to_siswa(id:str,nilai:schema.Nilai):
    siswa,index = await find_siswa(id,fake_db)
    if not siswa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Siswa Does't Not Exist")
    
    fake_db[index]["nilai"].append(nilai.nilai)
    return fake_db[index]

@router.delete("/{id}")
async def Reset_nilai(id:str):
    siswa,index = await find_siswa(id,fake_db)
    if not siswa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Siswa Does't Not Exist")
    
    fake_db[index]["nilai"] = []

    return {"Massage" : "Successful Reset Nilai"}

@router.get("/{id}")
async def Get_nilai_siswa(id:str):
    siswa,index = await find_siswa(id,fake_db)
    if not siswa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Siswa Does't Not Exist")
    min,max,average = await get_nilai_info(siswa.get("nilai"))
    if (min == 0) & (max == 0) & (max == 0):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This Siswa Does't Have Nilai")

    return {"id":siswa.get("id"),"nama":siswa.get("nama"), "nilai" : siswa.get("nilai"),"nilai_minimal":min,"nilai_maximal":max,"rata-rata":average}

@router.get("/")
async def Save_nilai_to_excel():
    if not fake_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You Not input nilai")
    len_nilai = await get_max_len_nilai(fake_db)
    return {"len" : len_nilai}
    
    
    
    

    