# Generated by Django 3.2.7 on 2022-06-04 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='time',
            field=models.CharField(choices=[(9, '09:00 – 10:00'), (10, '10:00 – 11:00'), (11, '11:00 – 12:00'), (12, '12:00 – 13:00'), (13, '13:00 – 14:00'), (14, '14:00 – 15:00'), (15, '15:00 – 16:00'), (16, '16:00 – 17:00'), (17, '17:00 – 18:00')], max_length=300),
        ),
    ]
