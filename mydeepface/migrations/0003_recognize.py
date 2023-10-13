# Generated by Django 4.2.6 on 2023-10-13 20:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mydeepface', '0002_alter_enroll_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recognize',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='mydeepface/uploads/')),
            ],
        ),
    ]