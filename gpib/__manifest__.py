{
    'name': 'GPIB Management',
    'version': '1.o',
    'summary': 'GPIB Management Software',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
    'license': 'LGPL-3',
    'depends': [],
    'data': [
        'views/family_line.xml',
        'views/family_master.xml',
        'views/pelkat.xml',
        'views/sector_view.xml',
        'views/gpib_menuitem.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
