# Generated by Django 3.0.5 on 2020-05-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200507_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='PostImage/<django.db.models.fields.related.ForeignKey>/'),
        ),
    ]
