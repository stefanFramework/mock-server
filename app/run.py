import random 
from flask import Flask, jsonify, request

app = Flask(__name__)

utils_prefix = '/utils'
application_prefix = '/<tenant>/<version>'
TRACKING_CODE_PADDING = '08d'

@app.route(utils_prefix + '/version')
def version():
    return jsonify({
        'version': '1.0',
        'comment': 'You are running Logistics Service MOCK application'
    }), 200


@app.route(utils_prefix + '/health')
def health():
    return jsonify({
        'status': 'Logistics Service MOCK is up and running'
    }), 200


@app.route(application_prefix + '/carriers')
def carriers(tenant, version):

    return jsonify([{
        'id': 1,
        'type': 'some-carrier',
        'name': 'SOME CARRIER',
        'logo': None,
        'integration_config': {},
        'general_config': {
            'icon': '',
            'template_name': 'GENERIC-ZPL-LABEL',
            'tracking_link': 'http://somecarrier.logistics.com/',
            'tracking_selection': 'external-selection',
            'tracking_identifier': 'SC'
        },
        'forward_logistics_enabled': True,
        'reverse_logistics_enabled': False,
        'created_at': '2021-01-01T12:40:00.000000',
        'updated_at': '2021-01-01T12:40:00.000000',
        'create_user': 'mock',
        'update_user': 'mock',
        'deleted_at': None,
        'tenant_id': tenant
    },
    {
        'id': 2,
        'type': 'some-other-carrier',
        'name': 'SOME OTHER CARRIER',
        'logo': None,
        'integration_config': {},
        'general_config': {
            'icon': '',
            'template_name': 'GENERIC-ZPL-LABEL',
            'tracking_link': 'http://someothercarrier.logistics.com/',
            'tracking_selection': 'external-selection',
            'tracking_identifier': 'SO'
        },
        'forward_logistics_enabled': True,
        'reverse_logistics_enabled': False,
        'created_at': '2021-01-01T12:40:00.000000',
        'updated_at': '2021-01-01T12:40:00.000000',
        'create_user': 'mock',
        'update_user': 'mock',
        'deleted_at': None,
        'tenant_id': tenant
    }
    ]), 200

@app.route(application_prefix + '/drop_codes_new', methods=['POST'])
def drop_code(tenant, version):
    return jsonify({
        'drop_code': random.randint(1600000000, 9999999999)
    }), 200

@app.route(application_prefix + '/forward_deliveries', methods=['POST'])
def forward_delivery(tenant, version):
    id = random.randint(100, 10000)
    client_reference = 123
    tracking_code_value = random.randint(1000000, 99999999)
    tracking_code = 'TC' + format(tracking_code_value, TRACKING_CODE_PADDING)

    label = ''

    carrier = {
        'id': 1,
        'type': 'some-carrier',
        'name': 'SOME CARRIER',
        'logo': None,
        'integration_config': {},
        'general_config': {
            'icon': '',
            'template_name': 'GENERIC-ZPL-LABEL',
            'tracking_link': 'http://somecarrier.logistics.com/',
            'tracking_selection': 'external-selection',
            'tracking_identifier': 'SC'
        },
        'forward_logistics_enabled': True,
        'reverse_logistics_enabled': False,
        'created_at': '2021-01-01T12:40:00.000000',
        'updated_at': '2021-01-01T12:40:00.000000',
        'create_user': 'mock',
        'update_user': 'mock',
        'deleted_at': None,
        'tenant_id': tenant
    }

    return jsonify({
            'id': id,
            'tracking_code': tracking_code,
            'label': label,
            'client_reference': client_reference,
            'carrier': carrier
        }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
