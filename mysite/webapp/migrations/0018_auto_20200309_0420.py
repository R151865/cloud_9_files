# Generated by Django 3.0 on 2020-03-09 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_auto_20200309_0410'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]
