# Generated by Django 3.2.5 on 2021-07-12 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_alter_trail_trail_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Comment Date')),
                ('description', models.TextField(max_length=250)),
                ('trail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.trail')),
            ],
        ),
    ]
