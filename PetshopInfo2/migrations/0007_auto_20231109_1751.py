# Generated by Django 3.2.8 on 2023-11-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetshopInfo2', '0006_alter_pets_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='hungry',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='pets',
            name='location',
            field=models.CharField(choices=[('Location1', 'Location 1'), ('Location2', 'Location 2'), ('Location3', 'Location 3'), ('Location4', 'Location 4')], default='-', max_length=40, null=True),
        ),
    ]
