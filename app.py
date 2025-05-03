from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

moods = {
    "happy": {
        "message": "Yay! Keep smiling 😊",
        "bg": "linear-gradient(135deg, #FFD700, #FF69B4)"
    },
    "sad": {
        "message": "It's okay to feel sad 😢",
        "bg": "linear-gradient(135deg, #89CFF0, #708090)"
    },
    "excited": {
        "message": "Woohoo! Let's go! 🤩",
        "bg": "linear-gradient(135deg, #FF6F61, #FFA07A)"
    }
}

saved_notes = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mood', methods=['POST'])
def mood():
    data = request.json
    mood = data.get('mood')
    return jsonify(moods.get(mood, {}))

@app.route('/save_note', methods=['POST'])
def save_note():
    data = request.json
    note_entry = {
        "mood": data.get("mood"),
        "note": data.get("note"),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    saved_notes.append(note_entry)
    return jsonify({"status": "success"})

@app.route('/get_notes')
def get_notes():
    return jsonify(saved_notes)
if __name__ == '__main__':
    app.run(debug=True)