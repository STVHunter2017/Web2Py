# -*- coding: utf-8 -*-
db.define ('products',
    Field('product_name', requires=IS_NOT_EMPTY() ),
    Field('product_price', requires=IS_NOT_EMPTY() ),
    Field('product_image', requires=IS_URL() ),
    Field('product_status', requires=IS_IN_SET (['active', 'inactive'])),
    Field('farm_name', requires=IS_NOT_EMPTY() ),
    Field('farm_address',  requires=IS_NOT_EMPTY() ),
    Field('farm_website', requires=IS_URL()),
    auth.signature
    )


db.define ('profile',
    Field('farm_name', requires=IS_NOT_EMPTY() ),
    Field('farm_address', requires=IS_NOT_EMPTY() ),
    Field('farm_website', requires=IS_URL()),
    auth.signature
    )

db.define ('internet_orders',
    Field('productId', type='intger' ),
    Field('qty', type='intger'),
    Field('userId', type='intger'),
    Field('status'),
    Field('date_ordered')
    )
