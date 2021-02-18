"""
Arango Database backend for Django

Requires: python-arango #https://github.com/Joowani/python-arango
"""

from django.db.backends.base.base import BaseDatabaseWrapper
from django.core.exceptions import ImproperlyConfigured

from abc import ABC

try:
    from arango import ArangoClient
except ImportError as e:
    raise ImproperlyConfigured("Error loading python-arango module: %s" % e)


class DatabaseWrapper(BaseDatabaseWrapper, ABC):
    vendor = 'arangodb'
    display_name = 'ArangoDB'

    def get_connection_params(self):
        settings_dict = self.settings_dict