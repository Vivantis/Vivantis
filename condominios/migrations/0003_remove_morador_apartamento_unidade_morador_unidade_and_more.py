# Generated by Django 5.2 on 2025-04-10 00:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominios', '0002_apartamento_morador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='morador',
            name='apartamento',
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('bloco', models.CharField(blank=True, max_length=50, null=True)),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominios.condominio')),
            ],
        ),
        migrations.AddField(
            model_name='morador',
            name='unidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='condominios.unidade'),
        ),
        migrations.DeleteModel(
            name='Apartamento',
        ),
    ]
