# Generated by Django 4.0.4 on 2022-04-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_api', '0002_user_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.CharField(default='subscriber', max_length=64),
        ),
    ]