# Generated by Django 3.1.2 on 2021-05-20 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст')),
                ('published_at', models.DateTimeField(verbose_name='Дата публикации')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=256, verbose_name='Название раздела')),
            ],
        ),
        migrations.CreateModel(
            name='ScopesInArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False, verbose_name='Главный раздел')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article', verbose_name='Article')),
                ('scope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.scope', verbose_name='Scope')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='Scope', through='articles.ScopesInArticle', to='articles.Scope'),
        ),
    ]
