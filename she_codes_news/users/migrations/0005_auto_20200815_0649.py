# Generated by Django 3.0.8 on 2020-08-14 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='images/profile/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
