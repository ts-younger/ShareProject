# Generated by Django 2.1 on 2020-05-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='houseinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=20, unique=True)),
                ('p_age', models.IntegerField(default=10)),
                ('p_sex', models.BooleanField(default=True)),
            ],
        ),
    ]
