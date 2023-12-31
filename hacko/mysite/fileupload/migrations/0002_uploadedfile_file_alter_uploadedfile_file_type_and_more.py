# Generated by Django 4.2.2 on 2023-07-15 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(default='default_file.txt', upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='file_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='tech_stack',
            field=models.CharField(max_length=255),
        ),
    ]
