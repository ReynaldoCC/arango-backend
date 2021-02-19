from abc import ABC

from django.db.backends.base.operations import BaseDatabaseOperations


class DatabaseOperations(BaseDatabaseOperations, ABC):
    pass
