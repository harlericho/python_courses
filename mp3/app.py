from gtts import gTTS
from io import BytesIO
# Convert text to speech audio
tts = gTTS(text='Hola como estas, Harlericho', lang='es')
tts.save('audio.mp3')
mp3 = BytesIO()
tts = gTTS(text='Hola como estas, Harlericho', lang='es')
tts.write_to_fp(mp3)


# Listen audio mp3
import pyglet
music = pyglet.resource.media('audio.mp3')
music.play()
pyglet.app.run()