# Generated by Django 4.2.3 on 2023-07-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='categoria',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
