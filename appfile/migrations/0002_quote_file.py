# Generated by Django 4.1.4 on 2023-01-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='file',
            field=models.FileField(default='default.pdf', upload_to='quotes/'),
        ),
    ]
