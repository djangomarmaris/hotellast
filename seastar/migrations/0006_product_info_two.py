# Generated by Django 4.0.5 on 2023-04-10 18:17

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seastar', '0005_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='info_two',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=21),
            preserve_default=False,
        ),
    ]
