# Generated by Django 3.2.9 on 2021-12-02 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20211202_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment_body',
        ),
    ]
