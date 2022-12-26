# Generated by Django 4.1.4 on 2022-12-26 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companies_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('Title', models.CharField(max_length=30)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('url', models.CharField(max_length=30)),
            ],
        ),
    ]