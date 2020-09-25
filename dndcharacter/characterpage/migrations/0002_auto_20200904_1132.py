# Generated by Django 3.1 on 2020-09-04 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('characterpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attackspell',
            name='range',
        ),
        migrations.AddField(
            model_name='attackspell',
            name='r',
            field=models.IntegerField(default=5, verbose_name='range'),
        ),
        migrations.AlterField(
            model_name='attackspell',
            name='damage',
            field=models.CharField(default='', max_length=20, verbose_name='damage/type'),
        ),
        migrations.AlterField(
            model_name='attackspell',
            name='hit_dc',
            field=models.CharField(default='0', max_length=10, verbose_name='hit/dc'),
        ),
        migrations.AlterField(
            model_name='attackspell',
            name='name',
            field=models.CharField(default='', max_length=30, verbose_name='attack name'),
        ),
        migrations.AlterField(
            model_name='character',
            name='alignment',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='character',
            name='bg',
            field=models.CharField(default='', max_length=20, verbose_name='background'),
        ),
        migrations.AlterField(
            model_name='character',
            name='char_class',
            field=models.CharField(default='', max_length=20, verbose_name='class'),
        ),
        migrations.AlterField(
            model_name='character',
            name='creator',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='character',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='character',
            name='feats_traits',
            field=models.TextField(default='', verbose_name='features and traits'),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='character',
            name='profs_lang',
            field=models.TextField(default='', verbose_name='proficiencies and languages'),
        ),
        migrations.AlterField(
            model_name='character',
            name='race',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='character',
            name='spell_abl',
            field=models.CharField(default='', max_length=10, verbose_name='spellcasting ability'),
        ),
        migrations.AlterField(
            model_name='charspells',
            name='name',
            field=models.CharField(default='', max_length=30, verbose_name='Spell Name'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='equipment'),
        ),
    ]
