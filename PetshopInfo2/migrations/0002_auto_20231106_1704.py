# Generated by Django 3.2.8 on 2023-11-06 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PetshopInfo2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('breed', models.CharField(max_length=100, verbose_name='Nom')),
                ('prénom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('mail', models.TextField(null=True, verbose_name='Mail')),
                ('mobile', models.CharField(max_length=16, null=True, verbose_name='Mobile')),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='formateur',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PetshopInfo2.pets'),
        ),
        migrations.DeleteModel(
            name='Formateur',
        ),
    ]
