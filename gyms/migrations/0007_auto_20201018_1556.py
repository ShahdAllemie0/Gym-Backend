# Generated by Django 3.1.2 on 2020-10-18 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gyms', '0006_auto_20201018_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='type',
            field=models.CharField(choices=[(1, 'Aerial'), (2, 'Barre'), (3, 'Bootcamp'), (4, 'Boxing'), (5, 'Circuit training'), (6, 'Crossfit'), (7, 'Cycling')], max_length=1),
        ),
    ]
