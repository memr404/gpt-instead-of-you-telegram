from speechkit import ShortAudioRecognition, Session
from os import system, remove

def voice(oauth_token, catalog_id, name):
	session = Session.from_yandex_passport_oauth_token(oauth_token, catalog_id)
	system(f'ffmpeg -i {name} {name[:-4]}.wav')

	with open(f"{name[:-4]}.wav", 'rb') as f:
		data = f.read()

	recognizeShortAudio = ShortAudioRecognition(session)

	text = recognizeShortAudio.recognize(data, format='lpcm', sampleRateHertz='48000')
	remove(f"{name[:-4]}.wav")
	remove(f"{name}")
	return text