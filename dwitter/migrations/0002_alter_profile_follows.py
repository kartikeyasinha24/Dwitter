# Generated by Django 4.0.5 on 2022-11-25 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwitter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to='dwitter.profile'),
        ),
    ]
