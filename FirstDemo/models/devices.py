# -*- coding: utf-8 -*-
db.define_table('device',
          Field('DeviceName', 'string'),
          Field('Ip', 'string'),
          Field('Port', 'string'),
          Field('Status', requires=IS_IN_SET(['A','B','C','D']))
          )
