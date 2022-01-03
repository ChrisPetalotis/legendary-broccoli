# Generated by Django 3.2.8 on 2021-12-30 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_skill_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='image',
            new_name='image_file',
        ),
        migrations.AddField(
            model_name='certificate',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
