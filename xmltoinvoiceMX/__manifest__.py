
{

    'name': "XML To Invoice MXN",

    'version': '0.0.1',

    'summary': "Module to convert an XML CFDI file to an Odoo invoice",

    'description': """
    Module to convert an XML CFDI file to an Odoo invoice
    """,

    'author': "Jose Manuel Fabela Vilchis",

    'website': "https://www.linkedin.com/in/josemanuelvilchis/",

    'category': 'Uncategorized',

    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}