# Generated by Django 3.0.2 on 2020-01-09 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_auto_20200105_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=40)),
                ('rollno', models.IntegerField()),
                ('marks', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]