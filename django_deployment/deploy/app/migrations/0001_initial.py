# Generated by Django 4.2.4 on 2023-08-22 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="data",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")], max_length=15
                    ),
                ),
                (
                    "pendidikan",
                    models.CharField(
                        choices=[
                            ("SD", "SD"),
                            ("SMP", "SMP"),
                            ("SMA", "SMA"),
                            ("S1", "S1"),
                            ("S2", "S2"),
                            ("S3", "S3"),
                        ],
                        max_length=15,
                    ),
                ),
                ("umur", models.IntegerField(default=18)),
                ("pendapatan", models.IntegerField(default=1000000)),
                (
                    "status_pernikahan",
                    models.CharField(
                        choices=[("Single", "Single"), ("Menikah", "Menikah")],
                        max_length=15,
                    ),
                ),
                ("jumlah_anak", models.IntegerField(default=0)),
                (
                    "riwayat_peminjaman",
                    models.CharField(
                        choices=[("Baik", "Baik"), ("Tidak pernah", "Tidak pernah")],
                        max_length=15,
                    ),
                ),
            ],
        ),
    ]
