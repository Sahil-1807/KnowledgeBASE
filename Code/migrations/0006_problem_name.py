# Generated by Django 3.0.4 on 2020-03-31 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Code', '0005_problem_important'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='name',
            field=models.CharField(default='hello', max_length=300, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
