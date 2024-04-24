import pandas as pd

# Fungsi untuk membaca data dari file Excel
def read_excel(file_path):
    try:
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        print(f"Gagal membaca file Excel: {e}")
        return None

# Fungsi untuk menulis data ke file Excel
def write_excel(data, file_path):
    try:
        data.to_excel(file_path, index=False)
        print(f"Data telah ditulis ke: {file_path}")
    except Exception as e:
        print(f"Gagal menulis data ke file Excel: {e}")

# Fungsi untuk mengisi data 2020A dengan informasi dari data acuan berdasarkan nama
def fill_data_2020A(compare_data, reference_data):
    try:
        # Gabungkan data 2020A dengan data acuan berdasarkan kolom 'Nama'
        merged_data = pd.merge(compare_data, reference_data, on='Nama', how='left')
        return merged_data
    except Exception as e:
        print(f"Terjadi kesalahan saat mengisi data 2020A: {e}")
        return None

# Path ke file Excel data acuan dan data 2020A
reference_file_path = "C:\\Users\\Admin\\Documents\\pysc\\excels\\DATA_ACUAN.xlsx"
compare_file_path = "C:\\Users\\Admin\\Documents\\pysc\\excels\\DATA_2020A.xlsx"
output_file_path = "C:\\Users\\Admin\\Documents\\pysc\\excels\\DATA_2020A_filled.xlsx"

# Baca data dari kedua file Excel
reference_data = read_excel(reference_file_path)
compare_data = read_excel(compare_file_path)

if reference_data is not None and compare_data is not None:
    # Isi data 2020A dengan informasi dari data acuan berdasarkan nama
    filled_data_2020A = fill_data_2020A(compare_data, reference_data)

    if filled_data_2020A is not None:
        # Tulis data yang telah diisi ke file Excel baru
        write_excel(filled_data_2020A, output_file_path)
    else:
        print("Gagal mengisi data 2020A.")
else:
    print("Gagal membaca salah satu file Excel.")
