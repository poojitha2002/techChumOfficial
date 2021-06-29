# Generated by Django 3.2.4 on 2021-06-29 15:28

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Codeforces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('cfhandle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_name', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=100)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ContestSubmission',
            fields=[
                ('author', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='courses/')),
                ('content', models.TextField(default='Content to be displayed')),
            ],
        ),
        migrations.CreateModel(
            name='CoursesForInterviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='ci/')),
                ('content', models.TextField(default='Content to be displayed')),
            ],
        ),
        migrations.CreateModel(
            name='Fellowships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='gifts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Amazon Voucher worth', max_length=100)),
                ('image', models.ImageField(upload_to='gifts/')),
                ('coins', models.IntegerField(default=0)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Goodies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coins', models.IntegerField(default=0)),
                ('author', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Internships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='KLCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='ckl/')),
                ('content', models.TextField(default='Content to be displayed')),
            ],
        ),
        migrations.CreateModel(
            name='Memes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='memes/')),
            ],
        ),
        migrations.CreateModel(
            name='Scholorships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='ScholorshipTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('url', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CoursesForInterviewsContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(default='Day 1', max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.coursesforinterviews')),
            ],
        ),
        migrations.CreateModel(
            name='ContestQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_desc', models.TextField()),
                ('img', models.ImageField(upload_to='cq/')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.contest')),
            ],
        ),
        migrations.CreateModel(
            name='clgModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clg', models.CharField(max_length=100)),
                ('author', models.ForeignKey(default='author', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Allfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(default='Content to be displayed', max_length=200)),
                ('file', models.FileField(upload_to='')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.klcourse')),
            ],
        ),
    ]
