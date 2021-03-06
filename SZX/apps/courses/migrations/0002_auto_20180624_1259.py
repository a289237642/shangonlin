# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-24 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinfo',
            name='need_know',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='课程须知'),
        ),
        migrations.AddField(
            model_name='courseinfo',
            name='teacher_say',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='老师告知'),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='category',
            field=models.CharField(choices=[('前端', '前端'), ('后台', '后台')], max_length=5, verbose_name='课程类别'),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='desc',
            field=models.CharField(max_length=200, verbose_name='课程简介'),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='image',
            field=models.ImageField(upload_to='course/%y/%m', verbose_name='课程图片'),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='level',
            field=models.CharField(choices=[('初级', '初级'), ('中级', '中级'), ('高级', '高级')], default='初级', max_length=5, verbose_name='课程难度'),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='name',
            field=models.CharField(max_length=20, verbose_name='课程名称'),
        ),
        migrations.AlterField(
            model_name='lessoninfo',
            name='name',
            field=models.CharField(max_length=50, verbose_name='章节名称'),
        ),
        migrations.AlterField(
            model_name='sourceinfo',
            name='file_addr',
            field=models.FileField(max_length=200, upload_to='source/%y/%m', verbose_name='资源地址'),
        ),
        migrations.AlterField(
            model_name='sourceinfo',
            name='name',
            field=models.CharField(max_length=20, verbose_name='资源名称'),
        ),
        migrations.AlterField(
            model_name='videoinfo',
            name='url',
            field=models.URLField(default='http://video.atguigu.com/ce182d3e92d24c08ada798ed75236efe/64240d5f98c849d7a48a701646314ef0-abb0a550e0a4e1bd89390a178f91a577-ld.mp4', verbose_name='视频连接'),
        ),
    ]
