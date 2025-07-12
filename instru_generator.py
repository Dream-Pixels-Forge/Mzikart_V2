import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

model = MusicGen.get_pretrained('melody')

def generate_instru(tags, output_path="static/musicgen.wav"):
    desc = f"{tags}, instrumental, atmospheric"
    wav = model.generate([desc])[0]
    audio_write(output_path.replace(".wav", ""), wav, model.sample_rate, strategy="loudness", format="wav")