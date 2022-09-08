# Generated by Django 4.1 on 2022-09-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_remove_products_categoryid_alter_product_categoryid_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="proAvailability",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="product", name="proFacts", field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="proOrigin",
            field=models.TextField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name="product", name="proProfile", field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="product", name="proStory", field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="product", name="proDetail", field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="proDimension",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="product", name="proPrice", field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="product",
            name="proWeight",
            field=models.CharField(max_length=100, null=True),
        ),
    ]