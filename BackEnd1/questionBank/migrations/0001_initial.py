# Generated by Django 4.0.3 on 2022-07-30 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='questionBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', max_length=400)),
                ('answerA', models.CharField(default='', max_length=100)),
                ('answerB', models.CharField(default='', max_length=100)),
                ('answerC', models.CharField(default='', max_length=100)),
                ('answerD', models.CharField(default='', max_length=100)),
                ('correctAnswer', models.CharField(default='', max_length=100)),
                ('lessoneId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.lessone')),
            ],
        ),
    ]
