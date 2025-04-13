# Generated by Django 5.2 on 2025-04-13 20:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominios', '0018_perfilusuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditoria',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='autorizacaoentrada',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='autorizacaoentrada',
            name='respondido_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='condominios.morador'),
        ),
        migrations.AlterField(
            model_name='autorizacaoentrada',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('aprovada', 'Aprovada'), ('recusada', 'Recusada')], default='pendente', max_length=20),
        ),
        migrations.AlterField(
            model_name='autorizacaoentrada',
            name='unidade_destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominios.unidade'),
        ),
        migrations.AlterField(
            model_name='aviso',
            name='condominio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominios.condominio'),
        ),
        migrations.AlterField(
            model_name='aviso',
            name='publicado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comprovantepagamento',
            name='validado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comprovantes_validados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='documento',
            name='condominio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominios.condominio'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='enviado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='visitante',
            name='morador_responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominios.morador'),
        ),
        migrations.AlterField(
            model_name='visitante',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominios.unidade'),
        ),
    ]
