# Generated by Django 2.2.1 on 2019-06-13 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190612_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='pic1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='customuser',
            name='pic2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='customuser',
            name='pic3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='customuser',
            name='pic4',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='customuser',
            name='pic5',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]