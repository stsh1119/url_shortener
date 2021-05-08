from functools import wraps
from hashlib import sha256
from random import choices
from flask import request, jsonify, abort, make_response


def json_body_required(original_function):
    """Checks, that an incoming http request has a json body, returns an error if not."""
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        if not request.json:
            abort(make_response(jsonify(message="Missing request body"), 400))
        return original_function(*args, **kwargs)
    return


def generate_short_string(string: str) -> str:
    """Generates short, random 5-symbol string based on the sha256 hash of given long string."""
    hashed_sting = sha256(string.encode()).hexdigest()
    short_string = ''.join(choices(hashed_sting, k=5))

    return short_string
