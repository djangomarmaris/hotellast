# Generated by Django 4.0.5 on 2023-04-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seastar', '0008_comment_info_ru_product_title_ru_welcome_info_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='welcome',
            field=models.CharField(db_index=True, default=21, max_length=10000, verbose_name='İsim'),
            preserve_default=False,
        ),
    ]
