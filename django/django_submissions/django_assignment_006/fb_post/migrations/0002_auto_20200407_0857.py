# Generated by Django 3.0 on 2020-04-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb_post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reaction',
            name='reaction',
            field=models.CharField(choices=[('WOW', 'Wow'), ('LIT', 'Lit'), ('LOVE', 'Love'), ('HAHA', 'Haha'), ('THUMBS-UP', 'Thumbs-Up'), ('THUMBS-DOWN', 'Thumbs_Down'), ('ANGRY', 'Angry'), ('SAD', 'Sad')], default=None, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='commented_at',
            field=models.DateTimeField(verbose_name='auto-now'),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_at',
            field=models.DateTimeField(verbose_name='auto-now'),
        ),
        migrations.AlterField(
            model_name='reaction',
            name='reacted_at',
            field=models.DateTimeField(verbose_name='auto-now'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.TextField(verbose_name='auto-now'),
        ),
    ]
