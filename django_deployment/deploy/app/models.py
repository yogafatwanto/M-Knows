from django.db import models

# Create your models here.

class MlData(models.Model):
    GENDER_CHOICES = [
		('Male', 'Male'),
		('Female', 'Female'),
    ]
    STATUS_PERNIKAHAN_CHOICES = [
        ('Single', 'Single'),
		('Menikah', 'Menikah')
    ]
    PENDIDIKAN_CHOICES = [
        ('SD', 'SD'),
		('SMP', 'SMP'),
		('SMA', 'SMA'),
		('S1', 'S1'),
		('S2', 'S2'),
		('S3', 'S3'),
    ]
    RIWAYAT_PEMINJAMAN_CHOICES = [
        ('Baik', 'Baik'),
        ('Tidak pernah', 'Tidak pernah')
    ]
 
    gender=models.CharField(max_length=15, choices=GENDER_CHOICES)
    pendidikan=models.CharField(max_length=15, choices=PENDIDIKAN_CHOICES)
    umur=models.IntegerField(default=18)
    pendapatan=models.IntegerField(default=1000000)
    status_pernikahan=models.CharField(max_length=15, choices=STATUS_PERNIKAHAN_CHOICES)
    jumlah_anak=models.IntegerField(default=0)
    riwayat_peminjaman=models.CharField(max_length=15, choices=RIWAYAT_PEMINJAMAN_CHOICES)
