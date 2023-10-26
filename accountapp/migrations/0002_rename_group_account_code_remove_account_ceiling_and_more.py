# Generated by Django 4.2.6 on 2023-10-24 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='group',
            new_name='code',
        ),
        migrations.RemoveField(
            model_name='account',
            name='ceiling',
        ),
        migrations.RemoveField(
            model_name='account',
            name='currency',
        ),
        migrations.AddField(
            model_name='account',
            name='main_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accountapp.account'),
        ),
        migrations.AlterField(
            model_name='account',
            name='typeAccount',
            field=models.CharField(blank=True, choices=[('main', 'main'), ('sub', 'sub')], max_length=255),
        ),
    ]