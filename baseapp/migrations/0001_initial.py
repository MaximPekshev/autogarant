# Generated by Django 3.2.8 on 2021-12-15 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SEO_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=60, verbose_name='Страница')),
                ('title', models.CharField(blank=True, default='', max_length=70, null=True, verbose_name='Title, max 70 символов')),
                ('description', models.CharField(blank=True, default='', max_length=180, null=True, verbose_name='Description, max 180 символов')),
                ('keywords', models.CharField(blank=True, default='', max_length=512, null=True, verbose_name='Keywords, max 512 символов')),
            ],
            options={
                'verbose_name': 'СЕО',
                'verbose_name_plural': 'СЕО',
            },
        ),
    ]