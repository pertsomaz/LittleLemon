# Generated by Django 4.2.16 on 2024-11-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_id_alter_booking_no_of_guests_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]