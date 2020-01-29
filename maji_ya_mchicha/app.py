import logging
from logging import Formatter, FileHandler
from flask import Flask, make_response, jsonify
from maji_ya_mchicha import restaurants


app = Flask(__name__)


@app.route('/restaurants', methods=['GET'])
def restaurants_all():
    """Returns all restaurants objects"""
    restaurant_objects = restaurants.load_restaurants()
    return jsonify(restaurant_objects)


@app.route('/restaurants/search', methods=['GET'])
def restaurants_search():
    """Accepts request objects q=query, lat=latitude, and lon=longitude,
    and returns JSON object containing restaurant matches"""

    return make_response('search...', 200)


@app.errorhandler(404)
def not_found_error(error):
    return make_response('Resource not found', 404)


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')


if __name__ == '__main__':
    app.run()
