# Generated by Django 3.2.6 on 2021-08-26 09:51

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_users_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='핸드폰 번호'),
        ),
        migrations.AlterField(
            model_name='users',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='남성 / 여성'),
        ),
    ]