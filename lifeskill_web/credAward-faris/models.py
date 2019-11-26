import datetime

import peewee as pw
from playhouse.postgres_ext import PostgresqlExtDatabase


db = PostgresqlExtDatabase('next-cred')


class Base(pw.Model):
    created_at = pw.DateTimeField(default=datetime.datetime.now())
    updated_at = pw.DateTimeField(default=datetime.datetime.now())

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(Base, self).save(*args, **kwargs)

    class Meta:
        database = db
        # Check this one out here http://docs.peewee-orm.com/en/latest/peewee/models.html#table-names
        legacy_table_names = False

class Student(Base):
    fullname = pw.CharField(null=False)
    creativity = pw.IntegerField(null=True)
    leadership = pw.IntegerField(null=True)
    respect = pw.IntegerField(null=True)
    accumulative = pw.IntegerField(null=True)


db.connect()
db.create_tables([Student])
