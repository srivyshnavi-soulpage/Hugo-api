# Generated by Django 3.2.3 on 2021-07-12 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_ticket_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('approval', models.BooleanField(default=False)),
                ('rejected', models.BooleanField(default=False)),
                ('reason_for_reject', models.TextField(blank=True)),
                ('is_half_day', models.BooleanField(blank=True, default=False)),
                ('attachment', models.FileField(blank=True, upload_to='hugo_users/')),
                ('approval_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approval_from', to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Request Ticket',
                'verbose_name_plural': 'Request Tickets',
                'db_table': 'request_tickets',
            },
        ),
    ]
