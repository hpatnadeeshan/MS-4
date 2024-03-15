# Generated by Django 3.2 on 2024-03-03 16:37

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
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=255)),
                ('sku', models.IntegerField()),
                ('gtin12', models.BigIntegerField()),
                ('breadcrumb', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('availability', models.CharField(max_length=50)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('average_rating', models.FloatField()),
                ('reviews_count', models.IntegerField()),
                ('ingredients', models.TextField()),
                ('calory_content', models.CharField(max_length=100)),
                ('nutrition_analysis', models.TextField()),
                ('feeding_instructions', models.TextField()),
                ('scraped_at', models.DateTimeField()),
                ('categories', models.ManyToManyField(to='products.Category')),
            ],
        ),
    ]
