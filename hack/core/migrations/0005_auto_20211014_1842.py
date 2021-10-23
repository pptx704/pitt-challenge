# Generated by Django 3.2.8 on 2021-10-14 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_evidence_choice_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialist',
            name='patients',
        ),
        migrations.AddField(
            model_name='patient',
            name='specialist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patients', to='core.specialist'),
        ),
    ]