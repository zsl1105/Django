# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-27 06:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('recvi_name', models.CharField(max_length=100, verbose_name='收件人')),
                ('recvi_tel', models.CharField(max_length=50, verbose_name='收件人电话')),
                ('recvi_address', models.CharField(max_length=255, verbose_name='收件地址')),
                ('all_price', models.FloatField(verbose_name='订单总金额')),
                ('remark', models.CharField(max_length=255, verbose_name='订单备注')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='订单所属用户')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('good_id', models.IntegerField(verbose_name='商品编号')),
                ('goods_img', models.CharField(max_length=255, verbose_name='商品图片')),
                ('goods_name', models.CharField(max_length=100, verbose_name='商品名称')),
                ('goods_price', models.FloatField(verbose_name='商品价格')),
                ('goods_count', models.IntegerField(verbose_name='商品数量')),
                ('goods_price_all', models.FloatField(verbose_name='商品总价')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='订单')),
            ],
        ),
    ]
