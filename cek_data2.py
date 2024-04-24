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
        # Initialize an empty DataFrame to store the filled data
        filled_data = []

        # Iterate through each unique 'Nama' in the compare data
        for nama in compare_data['Nama'].unique():
            # Get all rows with the current 'Nama' from the reference data
            reference_subset = reference_data[reference_data['Nama'] == nama]

            # Check if there are multiple entries for the same 'Nama' in reference data
            if len(reference_subset) > 0:
                # If there are multiple entries, select the first entry
                reference_subset = reference_subset.iloc[[0]]

            # Merge the current subset of reference data with the compare data
            merged_subset = pd.merge(compare_data[compare_data['Nama'] == nama], reference_subset, on='Nama', how='left')

            print(f"Merged subset for {nama}:\n{merged_subset}")

            # Append the merged subset to the filled data list
            filled_data.append(merged_subset)

        # Concatenate all DataFrames in the filled data list
        filled_data = pd.concat(filled_data, ignore_index=True)
        
        return filled_data
    except Exception as e:
        print(f"Terjadi kesalahan saat mengisi data 2020A: {e}")
        return None


# Path ke file Excel data acuan dan data 2020A
reference_file_path = "C:\\Users\\Admin\\Documents\\pysc\\excels\\DATA_ACUAN.xlsx"
compare_file_path = "C:\\Users\\Admin\\Documents\\pysc\\excels\\DATA_2020C.xlsx"
output_file_path = "C:\\Users\\Admin\\Documents\\pysc\\excels\\DATA_2020C_filledsx12345.xlsx"

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
