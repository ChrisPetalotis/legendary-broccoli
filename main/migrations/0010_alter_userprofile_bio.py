# Generated by Django 3.2.8 on 2021-12-30 19:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20211230_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
