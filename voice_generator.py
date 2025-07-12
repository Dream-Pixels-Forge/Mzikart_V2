from TTS.api import TTS

tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

def generate_voice(text, output_path="static/output.wav"):
    tts.tts_to_file(text=text, language="fr", file_path=output_path)