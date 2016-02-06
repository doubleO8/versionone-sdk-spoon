#!/usr/bin/python
# -*- coding: utf-8 -*-
#: instance URL
INSTANCE_URL = None
#: versionone token
TOKEN = None

if not INSTANCE_URL or not TOKEN:
    raise ValueError(
        "Please define INSTANCE_URL and TOKEN in {me_myself_and_i}".format(
            me_myself_and_i=__file__))
