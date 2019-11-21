# Generated by Django 2.1.11 on 2019-10-20 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191020_1107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['title']},
        ),
        migrations.RenameField(
            model_name='link',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='topic',
            new_name='title',
        ),
        migrations.AlterUniqueTogether(
            name='link',
            unique_together={('title', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='note',
            unique_together={('title', 'user')},
        ),
    ]
