# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150715_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='activity',
            new_name='lesson',
        ),
    ]
