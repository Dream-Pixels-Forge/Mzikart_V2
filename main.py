from flask import Flask, render_template, request, send_from_directory
from datetime import datetime
import os
from voice_generator import generate_voice
from instru_generator import generate_instru
from mixer import mix_audio

app = Flask(__name__)
LYRICS_DIR = "lyrics"
AUDIO_FILE = "static/output.wav"
MUSIC_FILE = "static/musicgen.wav"
FINAL_MP3 = "static/final_mix.mp3"

@app.route("/", methods=["GET", "POST"])
def index():
    lyrics_text = ""
    file_name = ""
    if request.method == "POST":
        verse = request.form.get("verse", "")
        chorus = request.form.get("chorus", "")
        bridge = request.form.get("bridge", "")
        tags = request.form.get("tags", "")
        title = request.form.get("title", "Mzikart_Song").replace(" ", "_")

        lyrics_text = generate_lyrics(title, verse, chorus, bridge, tags)
        file_name = f"{title}_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
        os.makedirs(LYRICS_DIR, exist_ok=True)
        with open(os.path.join(LYRICS_DIR, file_name), "w", encoding="utf-8") as f:
            f.write(lyrics_text)

        generate_voice(lyrics_text, AUDIO_FILE)
        generate_instru(tags, MUSIC_FILE)
        mix_audio(AUDIO_FILE, MUSIC_FILE, FINAL_MP3)

    return render_template("index.html", lyrics=lyrics_text, file_name=file_name, audio_file=FINAL_MP3 if lyrics_text else None)

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(LYRICS_DIR, filename, as_attachment=True)

def generate_lyrics(title, verse, chorus, bridge, tags):
    return f"""Title: {title.replace('_', ' ')}
Style: {tags}

[Verse 1]
{verse}

[Chorus]
{chorus}

[Verse 2]
{verse}

[Bridge]
{bridge}

[Final Chorus]
{chorus}
"""

if __name__ == "__main__":
    os.makedirs(LYRICS_DIR, exist_ok=True)
    app.run(debug=True)