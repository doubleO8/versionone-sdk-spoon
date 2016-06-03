"""
The external interface for the versio9 package.  Right now there is only one
class, "V1Meta", which exposes the types and operations found in a specified
VersionOne server (defaulting to localhost/VersionOne.Web).
"""

from v1meta import V1Meta

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
