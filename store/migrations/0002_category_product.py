# Generated by Django 4.1 on 2022-08-06 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cateName', models.CharField(max_length=200)),
                ('cateDetail', models.TextField()),
                ('cateParent', models.IntegerField()),
                ('cateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proName', models.CharField(max_length=250)),
                ('proDetail', models.TextField()),
                ('proPrice', models.FloatField()),
                ('proWeight', models.CharField(max_length=100)),
                ('proDimension', models.CharField(max_length=200)),
                ('proIsPublish', models.BooleanField(default=True)),
                ('proCreated', models.DateTimeField(auto_now_add=True)),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.categories')),
            ],
        ),
    ]
