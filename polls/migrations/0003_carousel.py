# Generated by Django 4.0.4 on 2022-06-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_question_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=250)),
                ('tags', models.CharField(max_length=100)),
            ],
        ),
    ]
