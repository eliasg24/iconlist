# Generated by Django 4.0.3 on 2023-06-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='position',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
