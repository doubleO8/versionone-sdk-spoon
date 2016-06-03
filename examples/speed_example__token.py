#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from credentials import INSTANCE_URL, TOKEN
from versio9 import V1Meta

meta = V1Meta(
        instance_url=INSTANCE_URL,
        token=TOKEN)

t0 = time.time()


def process_queries():
    for query in (meta.asset_class(type.Name) for type in meta.AssetType):
        print query
        for asset in query:
            try:
                asset._v1_refresh()
                yield str(asset)
            except Exception, e:
                yield 'Error! %s(%s)' % (
                    asset._v1_asset_type_name, asset._v1_oid)


all_assets = list(process_queries())

t1 = time.time()

elapsed = t1 - t0
count = len(all_assets)

print "%d assets in %0.4fs (%0.4fs/asset)" % (count, elapsed, elapsed / count)

out = open('output.txt', 'w').write('\n'.join([str(a) for a in all_assets]))
