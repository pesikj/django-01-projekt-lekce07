# Generated by Django 4.0.4 on 2022-05-11 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_bookloan'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookloan',
            name='returned_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
