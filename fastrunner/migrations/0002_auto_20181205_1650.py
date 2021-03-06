# Generated by Django 2.1.3 on 2018-12-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastrunner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='length',
            field=models.IntegerField(default=0, verbose_name='teststep个数'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='api',
            name='name',
            field=models.CharField(max_length=100, verbose_name='接口名称'),
        ),
        migrations.AlterField(
            model_name='case',
            name='name',
            field=models.CharField(max_length=100, verbose_name='用例名称'),
        ),
        migrations.AlterField(
            model_name='casestep',
            name='name',
            field=models.CharField(max_length=100, verbose_name='用例名称'),
        ),
        migrations.AlterField(
            model_name='config',
            name='name',
            field=models.CharField(max_length=100, verbose_name='环境名称'),
        ),
        migrations.AlterField(
            model_name='database',
            name='name',
            field=models.CharField(max_length=100, verbose_name='数据库名称'),
        ),
        migrations.AlterField(
            model_name='filebinary',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='文件名称'),
        ),
    ]
