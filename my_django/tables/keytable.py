# -*- coding:utf-8 -*-
from my_django.models import Upload
from table import Table
from table.columns import Column

class KeyTable(Table):
    name = Column(field='username')
    key = Column(field='phrase')
    path = Column(field='headImg')
    date = Column(field='create_date')
    class Meta:
        model = Upload