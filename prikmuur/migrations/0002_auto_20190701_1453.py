# Generated by Django 2.2.2 on 2019-07-01 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prikmuur', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='notice_text',
            new_name='noticeText',
        ),
    ]
