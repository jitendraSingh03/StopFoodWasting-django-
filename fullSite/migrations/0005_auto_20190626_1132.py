# Generated by Django 2.1.5 on 2019-06-26 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullSite', '0004_auto_20190626_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='date',
            field=models.DateField(default='yyyy-mm-dd'),
        ),
    ]