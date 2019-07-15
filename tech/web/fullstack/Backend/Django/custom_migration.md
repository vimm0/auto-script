create empty migration file
`./manage.py makemigrations --empty <app-name>`

paste file
```
from django.db import migrations
from django.contrib.auth.models import Group
from django.contrib.auth.admin import User


def create_superuser(apps, schema_editor):
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'admin'
    superuser.email = 'admin@admin.com'
    superuser.set_password('admin')
    superuser.save()


def add_teacher_group(apps, schema_editor):
    # Added Group Teacher assign permission
    group, created = Group.objects.get_or_create(name='<group-name>')
    # https://stackoverflow.com/questions/50114505/why-i-cant-assign-new-permission-to-group-in-the-same-migration-in-django


class Migration(migrations.Migration):
    dependencies = [
        ('<app-name>', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_teacher_group),
        migrations.RunPython(create_superuser),

    ]

```
