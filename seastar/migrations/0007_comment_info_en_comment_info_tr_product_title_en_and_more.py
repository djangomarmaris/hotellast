# Generated by Django 4.0.5 on 2023-04-11 15:42

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seastar', '0006_product_info_two'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='info_en',
            field=models.TextField(max_length=250, null=True, verbose_name='Müşteri Yorumu'),
        ),
        migrations.AddField(
            model_name='comment',
            name='info_tr',
            field=models.TextField(max_length=250, null=True, verbose_name='Müşteri Yorumu'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(db_index=True, max_length=200, null=True, verbose_name='Başlık'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_tr',
            field=models.CharField(db_index=True, max_length=200, null=True, verbose_name='Başlık'),
        ),
        migrations.AddField(
            model_name='welcome',
            name='info_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='welcome',
            name='info_tr',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='welcome',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Başlık'),
        ),
        migrations.AddField(
            model_name='welcome',
            name='title_tr',
            field=models.CharField(max_length=500, null=True, verbose_name='Başlık'),
        ),
    ]
