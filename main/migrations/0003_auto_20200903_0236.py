# Generated by Django 3.0.7 on 2020-09-02 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_completion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='completion',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]