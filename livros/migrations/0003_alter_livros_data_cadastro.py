# Generated by Django 4.1 on 2024-02-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_alter_livros_options_alter_livros_co_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateField(auto_now=True),
        ),
    ]