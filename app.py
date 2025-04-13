import os
from flask import Flask, request, jsonify
import whisper

app = Flask(__name__)
model = whisper.load_model("base")  # Usando whisper original

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    file_path = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(file_path)
    try:
        result = model.transcribe(file_path)
        transcription = result["text"]
        os.remove(file_path)
        return jsonify({"transcription": transcription})
    except Exception as e:
        os.remove(file_path)
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return 'Whisper Transcription Service'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)