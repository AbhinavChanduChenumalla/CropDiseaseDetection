# Generated by Django 3.2.3 on 2021-05-29 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0002_alter_uploads_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploads',
            name='path',
            field=models.TextField(null=True),
        ),
    ]