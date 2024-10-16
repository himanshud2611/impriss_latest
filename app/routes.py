import os, sys
# from flask import Flask, jsonify, request
import fal_client
import datetime as dt
from flask import (
    Flask,
    render_template,
    url_for,
    redirect,
    request,
    make_response,
    abort,
    jsonify,
    session,
    flash)
from app import app
from app.helpers import *
from app.forms import *
from app.models import *


# Home route
FAL_KEY = ""
YOUTUBE_API_KEY = ""

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json.get('prompt', '')
    width = request.json.get('width', 1280)  # Default to 1024 if not specified
    height = request.json.get('height', 720)
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    handler = fal_client.submit(
        "fal-ai/flux/dev",
        arguments={
            "prompt": prompt,
               "image_size": "landscape_16_9"
        },
    )

    result = handler.get()
    print(result)
    return jsonify(result)

@app.route('/')
def index():
    return render_template('index.html')

