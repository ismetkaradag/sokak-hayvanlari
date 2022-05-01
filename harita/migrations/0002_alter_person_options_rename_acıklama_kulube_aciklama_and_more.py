# Generated by Django 4.0.3 on 2022-04-29 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harita', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['-beslemesayisi']},
        ),
        migrations.RenameField(
            model_name='kulube',
            old_name='acıklama',
            new_name='aciklama',
        ),
        migrations.RenameField(
            model_name='kulube',
            old_name='kapı',
            new_name='kapi',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='beslemesayısı',
            new_name='beslemesayisi',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='bildirmesayısı',
            new_name='bildirmesayisi',
        ),
        migrations.AddField(
            model_name='kulube',
            name='dogcat',
            field=models.CharField(default='Kedi', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='kulube',
            name='img',
            field=models.CharField(default='2.jpeg', max_length=100, null=True),
        ),
    ]
