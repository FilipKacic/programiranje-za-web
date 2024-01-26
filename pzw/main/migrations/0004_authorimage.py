# Generated by Django 3.2.12 on 2024-01-26 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_book_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='main/static/main/images/')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.author')),
            ],
        ),
    ]
