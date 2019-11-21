# Generated by Django 2.1.11 on 2019-10-19 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20191018_1434'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='linkdislike',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='linkdislike',
            name='link',
        ),
        migrations.RemoveField(
            model_name='linkdislike',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='notedislike',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='notedislike',
            name='note',
        ),
        migrations.RemoveField(
            model_name='notedislike',
            name='user',
        ),
        migrations.DeleteModel(
            name='LinkDislike',
        ),
        migrations.DeleteModel(
            name='NoteDislike',
        ),
    ]