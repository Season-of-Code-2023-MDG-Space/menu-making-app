# Generated by Django 4.1.7 on 2023-03-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_rename_day2_post_day_rename_item2_post_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gravy',
            name='gravy',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='normal',
            name='fullname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='snacks',
            name='snacks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sweets',
            name='sweets',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
