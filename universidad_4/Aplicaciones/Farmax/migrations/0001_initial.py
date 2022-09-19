# Generated by Django 3.0.6 on 2022-09-18 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('codigo', models.IntegerField(max_length=6, primary_key=True, serialize=False)),
                ('telefono', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(max_length=10)),
                ('cargo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(choices=[('generico', 'Generico'), ('laboratorio', 'Laboratorio')], max_length=30)),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('fecha_expiracion', models.DateField()),
                ('fecha_produccion', models.DateField()),
                ('precio_Compra', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('precio_venta', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proveedor', models.CharField(max_length=30)),
                ('ruc', models.CharField(max_length=10, unique=True)),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=60)),
            ],
        ),
    ]
