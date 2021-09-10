# Generated by Django 3.0 on 2021-08-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('messages', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'CONATCT LIST ',
            },
        ),
    ]