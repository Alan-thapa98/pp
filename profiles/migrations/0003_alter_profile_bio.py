# Generated by Django 3.2.6 on 2022-06-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='No Biography!!!', max_length=300),
        ),
    ]