# Generated by Django 2.1.7 on 2019-04-04 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20190401_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_picture',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.URLField(max_length=300, null=True),
        ),
    ]
