# Generated by Django 4.2 on 2024-03-07 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review_report', to=settings.AUTH_USER_MODEL)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_report', to='campaign.review')),
            ],
        ),
        migrations.CreateModel(
            name='ReportProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_report', to='campaign.project')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_project_report', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
