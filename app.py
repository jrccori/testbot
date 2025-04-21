from flask import Flask,session, render_template, request, jsonify,url_for,redirect
import whisper
import tempfile
import os
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import MarianMTModel, MarianTokenizer
import requests
import random
import os
app = Flask(__name__)

@app.route('/')
def home():
    return '¡Hola desde Flask en Railway! 🚂'
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)