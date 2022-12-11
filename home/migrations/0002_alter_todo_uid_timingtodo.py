# Generated by Django 4.1.4 on 2022-12-08 13:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('c4c392ac-557a-43b7-83ac-e546d8b6109a'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='TimingTodo',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('c4c392ac-557a-43b7-83ac-e546d8b6109a'), editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('timing', models.DateField()),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.todo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]