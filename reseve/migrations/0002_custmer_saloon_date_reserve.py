# Generated by Django 4.0.5 on 2022-06-29 08:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reseve', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='saloon',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='reseve.custmer')),
                ('saloon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='reseve.saloon')),
            ],
        ),
    ]