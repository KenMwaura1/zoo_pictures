# Generated by Django 3.2.8 on 2021-10-10 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('description', models.TextField()),
                ('author', models.CharField(default='admin', max_length=43)),
                ('image', models.ImageField(upload_to='images/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='z_pictures.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='z_pictures.location')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
