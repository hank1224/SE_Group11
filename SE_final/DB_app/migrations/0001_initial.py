# Generated by Django 4.1.7 on 2023-06-13 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_gender', models.CharField(choices=[('1', '男'), ('2', '女'), ('3', '其他'), ('4', '不願透漏')], max_length=1)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MassageChairModes',
            fields=[
                ('massage_chair_mode_id', models.AutoField(primary_key=True, serialize=False)),
                ('massage_chair_mode_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalStores',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_model', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_warranty', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Salespeople',
            fields=[
                ('salesperson_id', models.AutoField(primary_key=True, serialize=False)),
                ('salesperson_name', models.CharField(max_length=255)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB_app.physicalstores')),
            ],
        ),
        migrations.CreateModel(
            name='SalesRecords',
            fields=[
                ('sales_record_id', models.AutoField(primary_key=True, serialize=False)),
                ('sales_time', models.DateTimeField(auto_now_add=True)),
                ('sales_type', models.CharField(choices=[('1', '線上'), ('2', '實體')], max_length=1)),
                ('sales_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB_app.customers')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB_app.products')),
                ('salesperson', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='DB_app.salespeople')),
                ('store', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='DB_app.physicalstores')),
            ],
        ),
        migrations.CreateModel(
            name='SalesQuestionnaires',
            fields=[
                ('sales_record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='DB_app.salesrecords')),
                ('sales_process_score', models.IntegerField(blank=True)),
                ('warranty_process_score', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReferralCodes',
            fields=[
                ('referral_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('used_referral_code', models.CharField(blank=True, max_length=20)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DB_app.customers')),
            ],
        ),
        migrations.CreateModel(
            name='OnlineStoreVisits',
            fields=[
                ('visit_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB_app.customers')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB_app.products')),
            ],
        ),
        migrations.CreateModel(
            name='MassageChairs',
            fields=[
                ('massage_chair_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB_app.products')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB_app.physicalstores')),
            ],
        ),
        migrations.CreateModel(
            name='MassageChairRecord',
            fields=[
                ('usage_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('payment', models.CharField(choices=[('1', '現金'), ('2', 'APP付款')], max_length=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB_app.customers')),
                ('massage_chair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB_app.massagechairs')),
                ('massage_chair_mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB_app.massagechairmodes')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceReservations',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('reservation_time', models.DateTimeField()),
                ('Salespeople', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB_app.salespeople')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB_app.customers')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB_app.physicalstores')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceQuestionnaires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fill_time', models.DateTimeField(auto_now_add=True)),
                ('willingness_to_use_again', models.BooleanField(default=False)),
                ('massage_chair_mode_satisfaction', models.IntegerField(blank=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB_app.customers')),
                ('usage_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB_app.massagechairrecord')),
            ],
        ),
        migrations.AddField(
            model_name='customers',
            name='salesperson',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='DB_app.salespeople'),
        ),
        migrations.AddField(
            model_name='customers',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
