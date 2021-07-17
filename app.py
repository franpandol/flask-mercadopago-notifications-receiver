import os
import json
import logging
import sys

from flask import Flask, request, abort, Response


# Initialize Flask app
app = Flask(__name__)

app.config.from_object('config.ProductionConfig')

logger = logging.getLogger(__name__)


@app.route('/notifications', methods=['POST'])
def notifications():

    if not request.args.get('topic') == 'payment' or not request.args.get('id'):

        logger.exception("Missing fields")
        return Response(status=200)

    payment_id = request.args.get('id')
    return Response(status=200)
