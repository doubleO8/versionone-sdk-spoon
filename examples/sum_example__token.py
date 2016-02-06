#!/usr/bin/env python
# -*- coding: utf-8 -*-
from credentials import INSTANCE_URL, TOKEN
from v1pysdk import V1Meta

v1 = V1Meta(
        instance_url=INSTANCE_URL,
        token=TOKEN)

term = "Actuals.Value.@Sum"
for task in v1.Task.select("Name", term):
    if 'Actuals.Value.@Sum' in task.data:
        print task['Name']
        print task['Actuals.Value.@Sum']
