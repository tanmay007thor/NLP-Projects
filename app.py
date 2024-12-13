import spacy
from textblob import TextBlob
from flask import Flask, request, jsonify, render_template


nlp = spacy.load("en_core_web_sm")


def classify_emotion(comment):
    """
    Classify the emotion of a given comment into 5 categories:
    ['happy', 'sad', 'angry', 'fearful', 'neutral']
    """
    
    blob = TextBlob(comment)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    
    if polarity > 0.5:
        return "happy"
    elif polarity > 0 and polarity <= 0.5:
        return "neutral"
    elif polarity < 0 and polarity >= -0.5:
        return "sad"
    elif polarity < -0.5:
        return "angry"
    else:
        return "fearful"

def emotion_to_emoji(emotion):
    """Convert an emotion label to an emoji."""
    emoji_map = {
        "happy": "\U0001F604",  
        "sad": "\U0001F622",    
        "angry": "\U0001F621",  
        "fearful": "\U0001F628", 
        "neutral": "\U0001F610"  
    }
    return emoji_map.get(emotion, "\U0001F610")  


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    comment = data.get("comment", "")
    emotion = classify_emotion(comment)
    emoji = emotion_to_emoji(emotion)
    return jsonify({"comment": comment, "emotion": emotion, "emoji": emoji})

if __name__ == "__main__":
    app.run(debug=True)
