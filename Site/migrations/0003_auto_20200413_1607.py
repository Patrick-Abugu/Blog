# Generated by Django 3.0.5 on 2020-04-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0002_auto_20200410_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='bmt.jpg', upload_to=''),
        ),
    ]
