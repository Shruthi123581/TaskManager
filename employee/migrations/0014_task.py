# Generated by Django 3.2.9 on 2023-04-07 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_auto_20230406_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Started', 'Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='In Progress', max_length=50)),
                ('ptitle', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.project')),
            ],
        ),
    ]
