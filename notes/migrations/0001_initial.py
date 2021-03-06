# Generated by Django 3.2.12 on 2022-02-23 19:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0002_auto_20220223_2335'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ид')),
                ('text', models.TextField(max_length=1000, verbose_name='заметка')),
                ('status', models.CharField(choices=[('N', 'Новый'), ('P', 'В процессе'), ('S', 'Отложен'), ('D', 'Выполнено')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='обновлено')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='authors.author', verbose_name='Автор')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.project', verbose_name='проект')),
            ],
        ),
    ]
