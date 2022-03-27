# Generated by Django 4.0.3 on 2022-03-26 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0008_alter_kitnet_inadimplente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitnet',
            name='Inadimplente',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='kitnet',
            name='NumKitnet',
            field=models.IntegerField(unique=b'I01\n', verbose_name='Numero do Kitnet'),
        ),
    ]
