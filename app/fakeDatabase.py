from xlsxwriter import Workbook

fake_db = []

async def find_siswa(id:str,data:list):
    if not data:
        return {},None
    for i, val in enumerate(fake_db):
        if val.get("id") == id:
            return val,i
    return {},None

async def get_nilai_info(nilai:list):
    if not nilai:
        return 0,0,0
    average = 0
    min_val = min(nilai)
    max_val = max(nilai)
    devided = 0
    for item in nilai:
        average += item
        devided +=1
    
    return min_val, max_val, round(average/devided)

async def get_max_len_nilai(data:list):
    nilai = []
    for i in data:
        len_nilai = len(i.get("nilai"))
        nilai.append(len_nilai)

    return max(nilai)

async def save_data_to_excel(data:list,max_len:int):
    workbook = Workbook("nilai.xlsx")
    worksheet = workbook.add_worksheet("D.4")


    addon = workbook.add_format(
        {
            "font": "Cambria",
            "align": "center",
            "font_size":"9",
            "border":True,
            "bg_color":"#EDEDED",
            "text_wrap" : True
        }
    )
    addon.set_align('vcenter')

    head = workbook.add_format(
        {
            "align": "center",
            "font": "Cambria",
            "font_size": "11",
        }
    )

    content = workbook.add_format(
        {
            "font": "Cambria",
            "align": "center",
            "font_size":"9",
            "border":True,
            "text_wrap" : True
        }
    )
    content.set_align('vcenter')


    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 25)
    worksheet.set_column('C:C', 16)
    worksheet.set_column('D:D', 16)
    worksheet.set_column('E:E', 16)
    worksheet.set_column('F:F', 18)
    worksheet.set_column('G:G', 18)
    worksheet.set_column('H:H', 18)
    worksheet.merge_range('A3:H3', 'D.4 BUKU KADER PEMBERDAYAAN MASYARAKAT',head)
    worksheet.merge_range('A4:H4', 'DESA CIKONENG KABUPATEN BANDUNG',head)

    ALPHABET_STRING = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    worksheet.write('A6', 'NO URUT',addon)
    worksheet.write('B6', 'JURUSAN',addon)
    worksheet.write('C6', 'KELAS',addon)
    worksheet.write('D6', 'ALAMAT',addon)
    worksheet.write('E6', 'JENIS KELAMIN',addon)
    worksheet.write('F6', 'BIDANG',addon)
    worksheet.write('G6', 'ALAMAT',addon)
    worksheet.write('H6', 'KETERANGAN',addon)

    worksheet.write('A7', '1',addon)
    worksheet.write('B7', '2',addon)
    worksheet.write('C7', '3',addon)
    worksheet.write('D7', '4',addon)
    worksheet.write('E7', '5',addon)
    worksheet.write("F7","6",addon)
    worksheet.write("G7","7",addon)
    worksheet.write("H7","8",addon)

    for index, entry in enumerate(data):
        worksheet.write(index+6+1, 0, str(index+1), content)
        worksheet.write(index+6+1, 1, entry.get("nama"), content)
        worksheet.write(index+6+1, 2, f"{entry.get('umur')}",content)
        worksheet.write(index+6+1, 3, entry.get('jenis_kelamin'),content)
        worksheet.write(index+6+1, 4, entry.get("pendidikan"),content)
        worksheet.write(index+6+1, 5, entry.get("bidang"),content)
        worksheet.write(index+6+1, 6, f"{entry.get('alamat')}",content)
        worksheet.write(index+6+1, 7, f"{entry.get('keterangan')}",content)

    workbook.close()