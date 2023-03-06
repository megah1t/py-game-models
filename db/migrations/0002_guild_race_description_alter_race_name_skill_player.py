# Generated by Django 4.0.2 on 2023-03-06 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('bonus', models.CharField(max_length=255, verbose_name='Field describes what kind of bonus the player can get from it.')),
                ('race', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skill_races', to='db.race')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('bio', models.CharField(max_length=255, verbose_name='Short description provided by a user about himself/herself.')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('guild', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guilds', to='db.guild')),
                ('race', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_races', to='db.race')),
            ],
        ),
    ]