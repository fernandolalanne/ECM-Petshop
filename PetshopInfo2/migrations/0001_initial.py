# Generated by Django 3.2.8 on 2023-11-06 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Formateur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('prénom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('mail', models.TextField(null=True, verbose_name='Mail')),
                ('mobile', models.CharField(max_length=16, null=True, verbose_name='Mobile')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='PetshopInfo2.formateur')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
