# Generated by Django 2.2.5 on 2019-10-03 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_obr', '0009_base_obr_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='thema_obr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kod', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
