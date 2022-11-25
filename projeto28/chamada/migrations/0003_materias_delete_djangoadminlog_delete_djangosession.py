# Generated by Django 4.1.1 on 2022-11-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamada', '0002_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('matcodigo', models.AutoField(primary_key=True, serialize=False)),
                ('matnome', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'materias',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
    ]
