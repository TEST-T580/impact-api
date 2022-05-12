# Generated by Django 4.0.4 on 2022-05-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervention',
            name='long_description_en',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='intervention',
            name='long_description_no',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='intervention',
            name='short_description_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='intervention',
            name='short_description_no',
            field=models.CharField(max_length=100, null=True),
        ),
    ]