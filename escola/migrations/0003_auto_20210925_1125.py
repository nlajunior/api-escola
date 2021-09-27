# Generated by Django 3.2.5 on 2021-09-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_auto_20210712_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='celular',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('A', 'Avançado'), ('I', 'Intermediário'), ('B', 'Básico')], default='B', max_length=1),
        ),
    ]
