# Generated by Django 4.2.2 on 2023-06-10 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=10)),
                ('Lname', models.CharField(max_length=10)),
                ('Uname', models.CharField(max_length=10)),
                ('Password', models.CharField(max_length=10)),
                ('Cpassword', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobno', models.CharField(max_length=13)),
            ],
        ),
    ]
