import client, audio

class VoiceClient(client.Client):
    def __init__(self):
        super().__init__("127.0.0.1", 8080)
        
        self.input_audio    = audio.Audio(True)
        self.output_audio   = audio.Audio(False)

        self.send_audio()

    def handle_data(self, data):
        self.output_audio.write(data)

    def send_audio(self):
        while True:
            try:
                msg = self.input_audio.read()

                self.send(msg)
            except KeyboardInterrupt:
                self.close()
                break