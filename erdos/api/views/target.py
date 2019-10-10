import logging, urllib
from flask import Blueprint, jsonify, request
from erdos.api.models.es import get_all_docs, get_pagination_docs, multi_search
from erdos.api.models import TargetAPI

blueprint = Blueprint('target', __name__, url_prefix='/api/target')


@blueprint.route('/target/pid/<pid>/did/<did>', methods=['GET'])
def target(pid, did):
    """
    pid = 143899
    did = 577923220
    target_value = 0
    """
    try:
        # x = request.args.to_dict()
        # pid = request.args.get('pid', 0)
        # did = request.args.get('did', 0)

        target = TargetAPI.query.filter(
            TargetAPI.pid == pid,
            TargetAPI.did == did).first()

        if target:
            d = {"pid": target.RTPropertyUniqueIdentifier,
                 "did": target.RTDocumentIdentifier,
                 "target": target.target}
            return jsonify(d)

        return jsonify({})
    except Exception as e:
        return jsonify(e)
