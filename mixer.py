from pydub import AudioSegment

def mix_audio(voice_path, instru_path, output_path):
    voice = AudioSegment.from_file(voice_path)
    instru = AudioSegment.from_file(instru_path)

    instru = instru - 4
    voice = voice + 2

    instru = instru[:len(voice)] if len(instru) > len(voice) else instru * (len(voice) // len(instru) + 1)
    instru = instru[:len(voice)]

    mixed = instru.overlay(voice)
    mixed.export(output_path, format="mp3")