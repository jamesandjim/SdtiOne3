# Generated by Django 2.2 on 2019-06-13 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='mjtype',
            field=models.CharField(choices=[('wg', 'KW控制板系列'), ('ZK', '门禁一体机系列'), ('bl', '云门禁系列')], default='wg', max_length=20, verbose_name='控制器系列'),
        ),
    ]
