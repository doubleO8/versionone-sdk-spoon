#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

try:
    from lxml.etree import ElementTree
    from lxml.etree.ElementTree import Element
except ImportError:
    from xml.etree import ElementTree
    from xml.etree.ElementTree import Element

#: instance URL
INSTANCE_URL = os.getenv('VERSIONONE_INSTANCE_URL')
#: versionone token
TOKEN = os.getenv('VERSIONONE_TOKEN')

from versio9.client import V1Server


class TestV1Connection(unittest.TestCase):
    def test_connect(self):
        server = V1Server(instance_url=INSTANCE_URL, token=TOKEN)
        code, body = server.fetch('/rest-1.v1/Data/Story?sel=Name')
        # self.assertEquals(200, code)
        # print "\n\nCode: ", code
        # print "Body: ", body
        elem = ElementTree.fromstring(body)
        self.assertEquals(elem.tag, 'Assets')


if __name__ == '__main__':
    unittest.main()
