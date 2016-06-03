#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
from credentials import INSTANCE_URL, TOKEN
from versio9 import V1Meta

v1 = V1Meta(
        instance_url=INSTANCE_URL,
        token=TOKEN)

story_name = 'Some-Story-{uuid}'.format(uuid=uuid.uuid4().hex)
new_story = v1.Story.create(
        Name=story_name,
        Scope=v1.Scope(0),
)

new_story.Owners = list(v1.Member.where(Name="Administrator"))

v1.commit()

# print dir(new_story)

print new_story.Name
# 'New Story 2'
print new_story.Owners
# [<versio9.v1meta.Member object at 0x02AD9710>]
print new_story.Scope
# <versio9.v1meta.Scope object at 0x02AB2550>


for my_story in v1.Story.where(Name=story_name):
    print my_story.Name
