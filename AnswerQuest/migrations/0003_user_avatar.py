# Generated by Django 2.2.6 on 2019-11-01 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnswerQuest', '0002_user_starred'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='user_avatars/'),
        ),
    ]