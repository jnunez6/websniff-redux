# Generated by Django 2.1.4 on 2020-03-17 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sniffapp', '0008_delete_gwcandidate'),
    ]

    operations = [
        migrations.CreateModel(
            name='GWCandidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_id', models.CharField(max_length=64)),
                ('ra', models.CharField(max_length=64)),
                ('dec', models.CharField(max_length=64)),
                ('field', models.CharField(max_length=64)),
                ('gwevent', models.CharField(max_length=64)),
            ],
        ),
    ]
