# Generated by Django 3.2.13 on 2023-09-17 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilmesFamosos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('main_character', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=20)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Nomeados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('nominated', models.CharField(max_length=10)),
                ('year', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TopFilmes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('main_character', models.CharField(max_length=50)),
                ('feelings', models.CharField(choices=[('S', 'Sad'), ('H', 'Happy'), ('M', 'Mixed')], max_length=1)),
                ('position_in_top', models.IntegerField()),
                ('release_date', models.DateField()),
            ],
        ),
    ]