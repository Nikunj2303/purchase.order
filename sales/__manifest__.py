{
    'name': 'Sale Receipt Status',
    'version': '15.0.0.2',
    'license': 'LGPL-3',
    'sequence': 1,
    'category': 'Sales',
    'depends': ['product', 'purchase','sale'],
    'data': ['view\purchase_order_views.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
