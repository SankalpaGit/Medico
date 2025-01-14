# Generated by Django 4.1.12 on 2024-03-28 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medico', '0006_requestblood'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonateBlood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('blood_group', models.CharField(max_length=5)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
