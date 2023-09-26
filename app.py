import webbrowser
from flask import Flask, request, jsonify
from flask_restful import Api
from flasgger import Swagger
from audioprocessor import AudioProcessor
from settings import (
    audio_folder_name
)

import log.messages as messages
import os

app = Flask(__name__)
Swagger(app, template_file='swagger/swagger.yaml')

@app.route('/extract', methods=['GET'])
def extract():
    try:
        input_path = request.args.get('file')
        input_filename = os.path.splitext(os.path.basename(input_path))[0]

        os.makedirs(audio_folder_name, exist_ok=True)
        messages.process_started_message(input_filename)
        audio = AudioProcessor(input_path)
        audio.extract_audio()
        
        return jsonify({"message": "Process completed successfully."}), 200

    except Exception as e:
        return jsonify({"error": e}), 500
    
if __name__ == '__main__':
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:5000/apidocs')

    app.run(host="127.0.0.1", port=5000, debug=True)

