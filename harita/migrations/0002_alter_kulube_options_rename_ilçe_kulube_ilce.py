# Generated by Django 4.0.3 on 2022-04-20 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('harita', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kulube',
            options={'ordering': ['sontarih']},
        ),
        migrations.RenameField(
            model_name='kulube',
            old_name='ilçe',
            new_name='ilce',
        ),
    ]
