# Generated by Django 5.1.2 on 2024-11-03 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_material_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default='Request', max_length=255),
            preserve_default=False,
        ),
    ]