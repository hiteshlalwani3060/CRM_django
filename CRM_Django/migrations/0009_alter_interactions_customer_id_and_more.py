# Generated by Django 4.2.5 on 2024-01-25 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM_Django', '0008_alter_orders_date_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactions',
            name='Customer_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CRM_Django.record'),
        ),
        migrations.AlterField(
            model_name='opportunities',
            name='Customer_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CRM_Django.record'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Customer_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CRM_Django.record'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='Customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CRM_Django.record'),
        ),
    ]