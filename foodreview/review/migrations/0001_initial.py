# Generated by Django 4.2 on 2023-05-27 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.CharField(default='', max_length=1)),
                ('comment', models.CharField(default='', max_length=2000)),
            ],
        ),
    ]
