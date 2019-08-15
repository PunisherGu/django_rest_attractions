# Generated by Django 2.2.4 on 2019-08-13 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_pontoturistico_localizacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pontoturistico',
            old_name='dedescricao',
            new_name='descricao',
        ),
        migrations.AlterField(
            model_name='pontoturistico',
            name='localizacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localizacao.Localizacao'),
        ),
    ]
