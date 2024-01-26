# Generated by Django 4.2.5 on 2024-01-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM_Django', '0003_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactions',
            name='Interaction_ID',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='opportunities',
            name='Opportunity_ID',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Order_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='Task_ID',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
