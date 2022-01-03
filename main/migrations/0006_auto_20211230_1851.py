# Generated by Django 3.2.8 on 2021-12-30 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_certificate_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='name',
            new_name='provider',
        ),
        migrations.AlterField(
            model_name='certificate',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
