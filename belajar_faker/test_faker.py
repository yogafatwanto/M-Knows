# Import library yang dibutuhkan
import pandas as pd
from faker import Faker
import random

# Definisikan kelas RandomDataGenerator untuk menghasilkan data acak
class RandomDataGenerator:
    def __init__(self, jumlah_data):
        """
        Inisialisasi objek RandomDataGenerator.

        Parameters:
            jumlah_data (int): Jumlah data yang akan digenerate.
        """
        self.fake_data = Faker(["id_ID"])
        self.jumlah_data = jumlah_data
        
    def generate_data(self):
        """
        Mengenerate data acak berdasarkan jumlah data yang diinginkan.

        Returns:
            list: List berisi data-data acak.
        """
        # Generate data nama pria dan wanita sesuai jumlah data
        self.nama_pria = [self.fake_data.name_male() for _ in range(self.jumlah_data // 2)]
        self.nama_wanita = [self.fake_data.name_female() for _ in range(self.jumlah_data // 2)]
        self.nama = self.nama_pria + self.nama_wanita
        self.gender = ["pria" for _ in range(self.jumlah_data // 2)] + ["wanita" for _ in range(self.jumlah_data // 2)]
        self.alamat = [self.fake_data.address() for _ in range(self.jumlah_data)]
        self.pendidikan = ["Sarjana", "SMA/SMK/MA", "SMP", "SD"]
        self.status_pernikahan = [random.choice(['Sudah menikah', 'Single']) for _ in range(self.jumlah_data)]
        
        # Inisialisasi list untuk menyimpan hasil pendidikan, umur, nomor telepon, pendapatan, dan customer_id
        hasil_pendidikan = []
        umur = []
        nomor_telepon = []
        pendapatan = []
        customer_id = []

        # Generate data pendidikan, umur, nomor telepon, pendapatan, dan customer_id
        for n in self.nama:
            split_nama = n.split(', ')
            if split_nama[0].lower().startswith('dr.') or split_nama[0].lower().startswith('drs.'):
                hasil_pendidikan.append("Doktor")
            elif len(split_nama) > 1 and split_nama[1].startswith('M'):
                hasil_pendidikan.append("Magister")
            elif len(split_nama) > 1 and split_nama[1].startswith('S') or (split_nama[0].lower().startswith('ir.')):
                hasil_pendidikan.append("Sarjana")
            else:
                random_pendidikan = random.choice(self.pendidikan)
                hasil_pendidikan.append(random_pendidikan)
                
        for _ in range(self.jumlah_data):
            split_nama = self.nama[_].split(' ')
            umur_min, umur_max = 15, 60
           
            if 'Doktor' in hasil_pendidikan[_]:
                umur_range = (30, umur_max)
            elif 'Magister' in hasil_pendidikan[_]:
                umur_range = (28, umur_max)
            elif 'Sarjana' in hasil_pendidikan[_]:
                umur_range = (25, umur_max)
            elif split_nama[0].lower().startswith('kh.') or split_nama[0].lower().startswith('hj.'):
                umur_range = (33, umur_max)
            else:
                umur_range = (umur_min, umur_max)  # Fix this line: assign values to umur_range
            umur.append(random.randint(umur_range[0], umur_range[1]))
            
        for _ in range(self.jumlah_data):
            nomor_telepon.append(f"+628{self.random_number(2)}-{self.random_number(4)}-{self.random_number(4)}")
            
        for _ in range(self.jumlah_data):
            pendapatan_min, pendapatan_max = 4000000, 100000000
            jarak_pendapatan = 500000

            if 'Doktor' in hasil_pendidikan[_]:
                pendapatan_range = (8000000, pendapatan_max)
            elif 'Magister' in hasil_pendidikan[_]:
                pendapatan_range = (12000000, pendapatan_max)
            elif 'Sarjana' in hasil_pendidikan[_]:
                pendapatan_range = (20000000, pendapatan_max)
            elif 'kh' in self.nama[_].lower() or 'hj' in self.nama[_].lower():
                pendapatan_range = (15000000, pendapatan_max)
            else:
                pendapatan_range = (pendapatan_min, pendapatan_max)

            pendapatan_random = random.randint(pendapatan_range[0], pendapatan_range[1])
            pendapatan_bulat = round(pendapatan_random / jarak_pendapatan) * jarak_pendapatan

            pendapatan.append(pendapatan_bulat)

        for _ in range(self.jumlah_data):
            customer_id.append(f"CUS_{self.random_number(6)}")
            
        # Menggabungkan data-data yang dihasilkan menjadi bentuk dictionary
        data = []
        for i in range(self.jumlah_data):
            data.append({
                "customer_id": customer_id[i],
                "nama": self.nama[i],
                "gender": self.gender[i],
                "pendidikan": hasil_pendidikan[i],
                "umur": umur[i],
                "alamat": self.alamat[i],
                "nomor_telepon": nomor_telepon[i],
                "status_pernikahan": self.status_pernikahan[i],
                "pendapatan": pendapatan[i]
            })
            
        return data
    
    def random_number(self, length):
        """
        Mengenerate angka acak sepanjang panjang yang ditentukan.

        Parameters:
            length (int): Panjang angka yang ingin digenerate.

        Returns:
            str: Angka acak dalam bentuk string.
        """
        return ''.join(random.choice("0123456789") for _ in range(length))

# Generate data dengan jumlah_data sebanyak 1000
generator = RandomDataGenerator(1000)
data = generator.generate_data()

# Create DataFrame dan urutkan berdasarkan customer_id
df = pd.DataFrame(data).sort_values(by="customer_id")

# Ubah gender berdasarkan kata 'kh' dan 'hj' dalam nama
df.loc[df['nama'].str.contains('kh', case=False), "gender"] = "pria"
df.loc[df['nama'].str.contains('hj', case=False), "gender"] = "wanita"

# Simpan DataFrame ke file CSV dengan nama yang sesuai jumlah baris data
df.to_csv(f"dummy_data_{len(df)}.csv", index=False)
