import logging
from logging import Formatter, FileHandler
from flask import Flask, make_response, jsonify, request
from flask_app import restaurants


app = Flask(__name__)


@app.route('/restaurants', methods=['GET'])
def restaurants_all() -> str:
    """Returns all restaurants objects in JSON"""
    restaurant_objects = restaurants.load_restaurants()
    return jsonify(restaurant_objects)


@app.route('/restaurants/search', methods=['GET'])
def restaurants_search() -> str:
    """Accepts request objects q=query, lat=latitude, and lon=longitude,
    and returns restaurant matches in JSON"""
    args = request.args
    if 'q' in args and 'lat' in args and 'lon' in args:  # check if correct params are given
        if len(args['q']) > 0 and len(args['lat']) > 0 and len(args['lon']) > 0:  # check that
            # params satisfy length requirements
            try:
                q = args['q']
                location = (float(args['lat']), float(args['lon']))
            except ValueError:  # Expects Float type
                return make_response('Malformed request', 404)
            restaurant_object_matches = restaurants.search(q, location)
            return jsonify(restaurant_object_matches)
    return make_response('Malformed request', 404)


@app.errorhandler(404)
def not_found_error(error) -> str:
    return make_response('Resource not found', 404)


# for situations not handled by 404, log line number where error occured
if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)


if __name__ == '__main__':
    app.run()
