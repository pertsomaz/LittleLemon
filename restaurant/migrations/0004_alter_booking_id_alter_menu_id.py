# Generated by Django 4.2.16 on 2024-11-21 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_booking_id_alter_menu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
