# Generated by Django 3.1.2 on 2020-10-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryattribute',
            name='attributes',
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='attributes',
            field=models.ManyToManyField(blank=True, default='', to='test.Attribute'),
        ),
    ]