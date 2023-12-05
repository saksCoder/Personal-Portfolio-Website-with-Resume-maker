# Generated by Django 4.2.4 on 2023-10-23 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(default='Shoubhit', max_length=20)),
                ('tags', models.CharField(default='Django, Wordpress, Bootstrap', max_length=40)),
                ('date', models.CharField(default='Oct 23, 2023', max_length=30)),
                ('content', models.TextField()),
                ('short_desc', models.CharField(default='', max_length=300)),
                ('slug', models.CharField(max_length=100)),
                ('image', models.ImageField(default='', upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='Author',
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]