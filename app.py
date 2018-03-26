import json
import subprocess

from flask import Flask, render_template, request, make_response, abort, jsonify


app = Flask(__name__)


@route('/volume/<adjustment>', methods=["POST"])
def adjust_volume(adjustment=None):
    """ Adjust the volume on the local machine """

    if adjustment = "up":
        subprocess.call('./scripts/volume_up.sh')
    elif adjustment = "down":
        subprocess.call('./scripts/volume_down.sh')
