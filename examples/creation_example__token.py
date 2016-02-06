#!/usr/bin/env python
# -*- coding: utf-8 -*-
from credentials import INSTANCE_URL, TOKEN
from v1pysdk import V1Meta

v1 = V1Meta(
        instance_url=INSTANCE_URL,
        token=TOKEN)

new_story = v1.Story.create(
        Name="New Story",
        Scope=v1.Scope(0),
)

new_story.Owners = list(v1.Member.where(Name="Admin"))

v1.commit()
