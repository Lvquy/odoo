# -*- coding: utf-8 -*-
{
    'name': 'ThiCong',
    'version': '1',
    'category': 'category_xxx',
    'live_test_url': 'live_test_url_xxx',
    'summary': 'summary_xxx',
    'author': 'author_xxx',
    'company': 'company_xxx',
    'website': 'website_xxx',
    'depends': 'depends_xxx',
    'data': [
        'data/sequence.xml',
        # security
        'security/module_name_groups.xml',
        'security/ir.model.access.csv',

        # views
        'views/xxx.xml',

        # report
        'report/xxx.xml',

    ],
    'assets': {
        'web.assets_backend': [],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
}

