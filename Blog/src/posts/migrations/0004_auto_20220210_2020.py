# Generated by Django 3.2 on 2022-02-10 20:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_tumbnail_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
