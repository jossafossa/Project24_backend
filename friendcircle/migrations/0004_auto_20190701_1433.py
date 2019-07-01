# Generated by Django 2.2.1 on 2019-07-01 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friendcircle', '0003_friendcircle_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendcircle',
            name='members',
            field=models.ManyToManyField(related_name='memberships', through='friendcircle.FriendCircleMembership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendcirclemembership',
            name='friendcircle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friendcircle.FriendCircle'),
        ),
        migrations.AlterField(
            model_name='friendcirclemembership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
