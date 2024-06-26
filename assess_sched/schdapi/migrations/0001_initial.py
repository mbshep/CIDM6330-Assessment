# Generated by Django 5.0.4 on 2024-05-02 01:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Assessment",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("lab_id", models.CharField(max_length=10)),
                ("timeframe", models.CharField(max_length=50)),
                ("man_days", models.IntegerField()),
                ("notes", models.TextField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Reassess", "rea"),
                            ("Initial", "ini"),
                            ("PreAssessment", "pre"),
                            ("Relocation", "reloc"),
                        ],
                        default="Reassess",
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Assessor",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("fname", models.CharField(max_length=25)),
                ("lname", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Lab",
            fields=[
                (
                    "id",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "techs",
                    models.CharField(
                        choices=[
                            ("Chemistry", "chem"),
                            ("Micro", "micro"),
                            ("WET", "wet"),
                            ("Radiochemistry", "radchem"),
                            ("Asbestos", "asb"),
                        ],
                        default="Chemistry",
                        max_length=15,
                    ),
                ),
                ("location", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="Sched",
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
            ],
        ),
    ]
