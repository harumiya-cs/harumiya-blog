# Generated by Django 4.2.2 on 2023-08-05 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_options_post_slug_post_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='word_count',
        ),
    ]
