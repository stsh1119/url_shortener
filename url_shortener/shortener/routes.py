from flask import Blueprint, redirect, jsonify, request
from pydantic import ValidationError
from ..utils import json_body_required
from .dto import CreateNewLinkDto
from . import service


shortener = Blueprint('shortener', __name__)


@json_body_required
@shortener.route('/', methods=['POST'])
def get_a_shortcut_for_new_url():
    try:
        new_link_creation_data = CreateNewLinkDto.parse_obj(request.json)
        short_url = service.create_short_url(new_link_creation_data)
        return jsonify(short_url), 201

    except ValidationError as e:
        return e.json(), 400


@shortener.route('/<string:short_url>', methods=['GET'])
def redirect_to_long_url(short_url):
    original_url = service.view_original_url(short_url)
    if original_url:
        return redirect(original_url), 200

    return jsonify(msg='No such URL')
