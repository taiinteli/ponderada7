import soundfile as sf
import simpleaudio as sa
import whisper
from txtai.pipeline import TextToSpeech

# carregando o modelo de transcrição de áudio
model = whisper.load_model("small")

# solicitando informações do usuário
audio_name = input("Digite o nome do arquivo de áudio: ")
audio_lang = input("Em qual linguagem está o áudio? ")

# Transcrevendo o áudio
results = model.transcribe(audio_name, language=audio_lang, task="translate")

# imprimindo o texto reconhecido
print("Texto Reconhecido:\n")
print(results["text"])

# inicializando o pipeline TextToSpeech
tts = TextToSpeech("NeuML/ljspeech-jets-onnx")

# utilizando o texto reconhecido para gerar fala
tts_text = results["text"]
speech = tts(tts_text)

# salvando a fala em um arquivo WAV
sf.write("out.wav", speech, 22050)

# lendo o arquivo WAV
wave_obj = sa.WaveObject.from_wave_file("out.wav")

# reproduzindo o áudio
play_obj = wave_obj.play()
play_obj.wait_done()