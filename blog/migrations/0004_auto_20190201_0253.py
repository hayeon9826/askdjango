# Generated by Django 2.1.5 on 2019-01-31 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190201_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(choices=[('제목1', '세간'), ('제목2', '픽즐'), ('제목3', '모잇')], max_length=100),
        ),
    ]