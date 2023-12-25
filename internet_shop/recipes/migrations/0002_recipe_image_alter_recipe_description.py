# Generated by Django 4.2.7 on 2023-12-25 17:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='img/%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(default=None),
        ),
    ]
