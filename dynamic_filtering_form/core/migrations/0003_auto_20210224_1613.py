# Generated by Django 3.1.7 on 2021-02-24 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210224_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='categories',
            field=models.ManyToManyField(default=None, to='core.Category'),
        ),
    ]
