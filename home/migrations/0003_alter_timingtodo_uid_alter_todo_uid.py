# Generated by Django 4.1.4 on 2022-12-09 09:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_todo_uid_timingtodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timingtodo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('754756d7-cbb1-4f7e-9670-6a1d86e4c786'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('754756d7-cbb1-4f7e-9670-6a1d86e4c786'), editable=False, primary_key=True, serialize=False),
        ),
    ]
