# Generated by Django 4.2.9 on 2024-12-11 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cmscontexts', '0018_editorialboardlockuser_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebPathCdsCod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cds_cod', models.CharField(max_length=4)),
                ('webpath', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cmscontexts.webpath')),
            ],
        ),
    ]
