# Generated by Django 4.1.7 on 2023-04-09 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0002_rename_birthday_actor_birth_day_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='cast',
            new_name='actor',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='photo',
            new_name='poster',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='duration',
            new_name='runtime',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='birth_day',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='country',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='director',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='director',
            name='birth_day',
        ),
        migrations.RemoveField(
            model_name='director',
            name='country',
        ),
        migrations.RemoveField(
            model_name='director',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='description',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favorite_movies',
        ),
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.FloatField(),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeApp.movie'),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeApp.user'),
        ),
        migrations.AddField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='HomeApp.movie'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeApp.user'),
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeApp.movie'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomeApp.user'),
        ),
    ]
