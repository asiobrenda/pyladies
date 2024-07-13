from django.db import connection


class TruncateTableMixin(object):

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {} RESTART IDENTITY CASCADE'.format(cls._meta.db_table))
