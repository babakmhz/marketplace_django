# Generated by Django 3.1.2 on 2020-10-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0004_auto_20201017_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subitem',
            name='attributes',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='attributes',
            field=models.ManyToManyField(blank=True, default='', to='test.Attribute'),
        ),
    ]
