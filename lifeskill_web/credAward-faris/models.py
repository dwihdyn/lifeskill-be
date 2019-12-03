import datetime

import peewee as pw
from playhouse.postgres_ext import PostgresqlExtDatabase


db = PostgresqlExtDatabase('lifeskill_be')


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
    id_number = pw.IntegerField(unique=True)
    full_name = pw.CharField()
    password = pw.CharField()
    creativity_score = pw.IntegerField()
    leadership_score = pw.IntegerField()
    respect_score = pw.IntegerField()


db.connect()
db.create_tables([Student])
