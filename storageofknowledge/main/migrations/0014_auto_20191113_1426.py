# Generated by Django 2.1.11 on 2019-11-13 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_user_token'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserToken',
            new_name='UserConfirmation',
        ),
        migrations.RenameField(
            model_name='userconfirmation',
            old_name='token',
            new_name='secret_key',
        ),
        migrations.AlterModelTable(
            name='userconfirmation',
            table='user_confirmation',
        ),
    ]