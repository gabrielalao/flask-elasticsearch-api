import logging, urllib
from flask import Blueprint, jsonify, request
from erdos.api.models.es import get_all_docs, get_pagination_docs, multi_search
from erdos.api.models import TargetAPI
from erdos.api.models import AttomTax, AttomRec, AttomForeclosure, AttomAvm, Cass, RawQuery

from erdos.api.models.recent_sales_results import RecentSalesResults

blueprint = Blueprint('db', __name__, url_prefix='/api/db')


@blueprint.route('/cass/<pid>', methods=['POST', 'GET'])
def cass(pid):
    return Cass(pid).generate_results()


@blueprint.route('/recent_sales_results', methods=['GET'])
def recent_sales_results():
    return RecentSalesResults().generate_results()


@blueprint.route('/tax/<pid>', methods=['POST', 'GET'])
def tax(pid):
    """
    http://localhost:5000/api/database/tax/1
    """
    try:
        tax = AttomTax.query.filter(AttomTax.pid == pid).first()
        if tax:
            return jsonify(tax.serialize)
        return jsonify({})
    except Exception as e:
        return jsonify(e)


@blueprint.route('/tax_full/<pid>', methods=['POST', 'GET'])
def tax_full(pid):
    try:
        tax = AttomTax.query.filter(AttomTax.pid == pid).first()
        if tax:
            atts = [str(key)[10:] for key in tax.__table__.c]
            d = {}
            for att in atts:
                d[att] = str(getattr(tax, att, ''))
            return jsonify(d)
        return jsonify({})
    except Exception as e:
        return jsonify(e)


@blueprint.route('/rec/<pid>', methods=['POST', 'GET'])
def get_rec(pid):
    try:
        output = []
        rec = AttomRec.query.filter(AttomRec.pid == pid).all()
        for row in rec:
            output.append(row.serialize)
        return jsonify(output)
    except Exception as e:
        return jsonify(e)


@blueprint.route('/foreclosure/<pid>', methods=['POST', 'GET'])
def get_foreclosure(pid):
    try:
        foreclosure = AttomForeclosure.query.filter(AttomForeclosure.pid == pid).first()
        if foreclosure:
            atts = [str(key)[18:] for key in foreclosure.__table__.c]
            d = {}
            for att in atts:
                d[att] = str(getattr(foreclosure, att, ''))
            return jsonify(d)
        return jsonify({})
    except Exception as e:
        return jsonify(e)


@blueprint.route('/avm/<pid>', methods=['POST', 'GET'])
def get_avm(pid):
    try:
        avm = AttomAvm.query.filter(AttomAvm.pid == pid).first()
        if avm:
            atts = [str(key)[10:] for key in avm.__table__.c]
            d = {}
            for att in atts:
                d[att] = str(getattr(avm, att, ''))
            return jsonify(d)
        return jsonify({})
    except Exception as e:
        return jsonify(e)
