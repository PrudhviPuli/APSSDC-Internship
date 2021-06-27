# Generated by Django 3.2.4 on 2021-06-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'signup',
            },
        ),
    ]
