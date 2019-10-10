import logging, urllib
from flask import Blueprint, jsonify, request
from erdos.api.models.es import get_all_docs, get_pagination_docs, multi_search

blueprint = Blueprint('elasticsearch', __name__, url_prefix='/api/elasticsearch')


@blueprint.route('/ajax/<_type>/', methods=['POST', 'GET'])
def DTajax(_type):
    _query = request.args.get('search', '')
    _fields = request.args.get('fields', 'all')
    _size = request.args.get('length', 10)
    _from = request.args.get('start', 0)

    dummy = {
        'PID': '',
        'PrimaryOwnerFullName': '',
        'SitusAddress': '',
        'TaxBillMailingAddress': ''
    }
    if 'empty' in request.args:
        return jsonify({'data': [dummy], 'recordsTotal': 1, 'recordsFiltered': 1})
    try:
        total, documents = get_pagination_docs(_type, _query, _fields, _size, _from)
        if documents:
            d = {}
            d['recordsTotal'] = total
            d['recordsFiltered'] = total
            d['data'] = [documents[PID] for PID in documents]
            return jsonify(d)
        return jsonify({'data': [dummy], 'recordsTotal': 1, 'recordsFiltered': 1})
    except Exception as e:
        return jsonify(e)


@blueprint.route('/<_type>/', defaults={'_query': ''}, methods=['POST', 'GET'])
@blueprint.route('/<_type>/<_query>', methods=['POST', 'GET'])
def search(_type, _query=''):
    _fields = 'all'
    _size = request.args.get('size', 10)
    _from = request.args.get('from', 0)
    try:
        total, documents = get_pagination_docs(_type, _query, _fields, _size, _from)
        if documents:
            return jsonify(documents)
        return jsonify({})
    except Exception as e:
        return jsonify(e)

