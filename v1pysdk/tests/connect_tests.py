import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../.."))

try:
    from lxml.etree import ElementTree
    from lxml.etree.ElementTree import Element
except ImportError:
    from xml.etree import ElementTree
    from xml.etree.ElementTree import Element

from examples.credentials import INSTANCE_URL, TOKEN
from v1pysdk.client import V1Server


class TestV1Connection(unittest.TestCase):
    def test_connect(self, username='admin', password='admin'):
        server = V1Server(instance_url=INSTANCE_URL, token=TOKEN)
        code, body = server.fetch('/rest-1.v1/Data/Story?sel=Name')
        print "\n\nCode: ", code
        print "Body: ", body
        elem = ElementTree.fromstring(body)
        self.assertEquals(elem.tag, 'Assets')


if __name__ == '__main__':
    unittest.main()
