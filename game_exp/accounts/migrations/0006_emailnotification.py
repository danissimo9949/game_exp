# Generated by Django 5.1.1 on 2024-10-10 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_token_gameexpuser_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_never_send', models.BooleanField(default=False)),
                ('buy_notification', models.BooleanField(default=True)),
                ('follow_notification', models.BooleanField(default=True)),
                ('reply_notification', models.BooleanField(default=True)),
                ('sales_notification', models.BooleanField(default=True)),
                ('new_features_announced', models.BooleanField(default=True)),
                ('new_game_jams', models.BooleanField(default=True)),
                ('new_devblogs_following', models.BooleanField(default=True)),
                ('new_uploads_add', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.gameexpuser')),
            ],
            options={
                'verbose_name': 'Email notification',
                'verbose_name_plural': 'Email notifications',
            },
        ),
    ]
