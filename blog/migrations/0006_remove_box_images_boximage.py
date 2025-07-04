# Generated by Django 5.2.1 on 2025-06-21 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_description_slug_box_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='box',
            name='images',
        ),
        migrations.CreateModel(
            name='BoxImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='box_images/')),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.box')),
            ],
        ),
    ]
