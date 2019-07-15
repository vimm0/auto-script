class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename


class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print("playing {} as mp3".format(self.filename))


class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print("playing {} as wav".format(self.filename))


class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print("playing {} as ogg".format(self.filename))

# >>> ogg = OggFile("myfile.ogg")
# >>> ogg.play()
# playing myfile.ogg as ogg
# >>> mp3 = MP3File("myfile.mp3")
# >>> mp3.play()
# playing myfile.mp3 as mp3
# >>> not_an_mp3 = MP3File("myfile.ogg")
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "polymorphic_audio.py", line 4, in __init__
#  raise Exception("Invalid file format")
# Exception: Invalid file format
