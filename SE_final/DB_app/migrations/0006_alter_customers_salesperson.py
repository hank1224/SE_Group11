# Generated by Django 4.1 on 2023-06-15 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DB_app', '0005_customerwebviews_delete_onlinestorevisits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='salesperson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DB_app.salespeople'),
        ),
    ]
