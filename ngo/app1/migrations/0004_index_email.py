# Generated by Django 3.1.4 on 2020-12-24 06:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_index_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]
