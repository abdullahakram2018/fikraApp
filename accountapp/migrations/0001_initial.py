# Generated by Django 4.2 on 2023-10-15 14:40

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
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=180)),
                ('ceiling', models.DecimalField(decimal_places=2, max_digits=10)),
                ('group', models.CharField(blank=True, max_length=180)),
                ('typeAccount', models.CharField(blank=True, max_length=180)),
                ('note', models.CharField(blank=True, max_length=180)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=180)),
                ('address', models.CharField(blank=True, max_length=180)),
                ('manager', models.CharField(blank=True, max_length=180)),
                ('note', models.CharField(blank=True, max_length=180)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=180)),
                ('color', models.CharField(blank=True, max_length=180)),
                ('note', models.CharField(blank=True, max_length=180)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='category_branch', to='accountapp.branch')),
                ('user_add', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='add_cate', to=settings.AUTH_USER_MODEL)),
                ('user_edit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='edit_cate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=10)),
                ('name', models.CharField(blank=True, max_length=180)),
                ('note', models.CharField(blank=True, max_length=180)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='currency_branch', to='accountapp.branch')),
                ('user_add', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='add_curr', to=settings.AUTH_USER_MODEL)),
                ('user_edit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='edit_curr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desentry', models.CharField(blank=True, max_length=180, null=True)),
                ('docid', models.CharField(blank=True, max_length=180, null=True)),
                ('dateentry', models.DateField(blank=True, null=True)),
                ('review', models.BooleanField(blank=True, default=False, null=True)),
                ('arvhive', models.ImageField(blank=True, null=True, upload_to='img')),
                ('noteentry', models.CharField(blank=True, max_length=180, null=True)),
                ('date_add', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_edit', models.DateTimeField(auto_now=True, null=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='entry_branch', to='accountapp.branch')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accountapp.currency')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=180)),
                ('lessAmount', models.FloatField(blank=True)),
                ('note', models.CharField(blank=True, max_length=180)),
                ('barcode', models.CharField(blank=True, max_length=180)),
                ('tracking', models.BooleanField(blank=True, default=False, null=True)),
                ('sku', models.CharField(blank=True, max_length=180)),
                ('color', models.CharField(blank=True, max_length=180)),
                ('image', models.CharField(blank=True, max_length=180)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('package', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='item_branch', to='accountapp.branch')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accountapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeUnit', models.CharField(blank=True, max_length=180)),
                ('name', models.CharField(blank=True, max_length=180)),
                ('note', models.CharField(blank=True, max_length=180)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='unit_branch', to='accountapp.branch')),
                ('user_add', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='add_unit', to=settings.AUTH_USER_MODEL)),
                ('user_edit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='edit_unit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TypeDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=180)),
                ('note', models.CharField(blank=True, max_length=180)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='typedoc_branch', to='accountapp.branch')),
                ('user_add', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='add_typedoc', to=settings.AUTH_USER_MODEL)),
                ('user_edit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='edit_typedoc', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=180)),
                ('location', models.CharField(blank=True, max_length=180)),
                ('capacity', models.CharField(blank=True, max_length=180)),
                ('storage_status', models.CharField(blank=True, max_length=180)),
                ('note', models.CharField(blank=True, max_length=180)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='store_branch', to='accountapp.branch')),
                ('user_add', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='add_stor', to=settings.AUTH_USER_MODEL)),
                ('user_edit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='edit_stor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('note', models.CharField(blank=True, max_length=180)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='priceitem_branch', to='accountapp.branch')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='itemprice', to='accountapp.item')),
                ('user_add', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='add_priceitem', to=settings.AUTH_USER_MODEL)),
                ('user_edit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='edit_priceitem', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accountapp.unit'),
        ),
        migrations.AddField(
            model_name='item',
            name='user_add',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='add_item', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='user_edit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='edit_item', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='EntryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('note_dat_en', models.CharField(blank=True, max_length=180)),
                ('success', models.BooleanField(blank=True, default=False)),
                ('entry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entry_details', to='accountapp.entry')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accountapp.item')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accountapp.store')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accountapp.unit')),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='typeDoc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accountapp.typedoc'),
        ),
        migrations.AddField(
            model_name='entry',
            name='user_add',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='add_entry', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='entry',
            name='user_edit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='edit_entry', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CurrencyPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selling', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('buying', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('note', models.CharField(blank=True, max_length=180)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='branchpricecurr', to='accountapp.branch')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='currencyprice', to='accountapp.currency')),
                ('user_add', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_addpricecurr', to=settings.AUTH_USER_MODEL)),
                ('user_edit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_editpricecurr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ar', models.CharField(blank=True, max_length=180)),
                ('name_en', models.CharField(blank=True, max_length=180)),
                ('note_ar', models.CharField(blank=True, max_length=180)),
                ('note_en', models.CharField(blank=True, max_length=180)),
                ('logo', models.ImageField(blank=True, upload_to='logo')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now=True)),
                ('user_add', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='add_com', to=settings.AUTH_USER_MODEL)),
                ('user_edit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='edit_com', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accountapp.company'),
        ),
        migrations.AddField(
            model_name='branch',
            name='user_add',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='add_branch', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='branch',
            name='user_edit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='edit_branch', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AccountEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('note_acc_en', models.CharField(blank=True, max_length=180)),
                ('creditor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creditor_account', to='accountapp.account')),
                ('debtor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debtor_account', to='accountapp.account')),
                ('entry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entry_account', to='accountapp.entry')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='account_branch', to='accountapp.branch'),
        ),
        migrations.AddField(
            model_name='account',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accountapp.currency'),
        ),
        migrations.AddField(
            model_name='account',
            name='user_add',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='add_acc', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='user_edit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='edit_acc', to=settings.AUTH_USER_MODEL),
        ),
    ]
