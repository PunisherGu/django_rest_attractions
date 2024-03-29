# Generated by Django 2.2.4 on 2019-08-15 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190813_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='curso'),
        ),
        migrations.AlterField(
            model_name='pontoturistico',
            name='localizacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='localizacao.Localizacao'),
        ),
    ]
