# Generated by Django 4.2.1 on 2023-05-19 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=50)),
                ('descripcion', models.TextField(max_length=200)),
                ('precio', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
