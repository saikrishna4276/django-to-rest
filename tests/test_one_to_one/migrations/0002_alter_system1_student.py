# Generated by Django 4.0.5 on 2022-09-29 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_one_to_one', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system1',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='test_one_to_one.student1'),
        ),
    ]