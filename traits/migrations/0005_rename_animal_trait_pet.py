# Generated by Django 4.1.4 on 2022-12-19 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0004_trait_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trait',
            old_name='animal',
            new_name='pet',
        ),
    ]
