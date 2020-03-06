import pyaudio

class Audio(pyaudio.PyAudio):
    def __init__(self, input):
        super().__init__()
        self.RATE       = 44111
        self.CHANNELS   = 1
        self.FORMAT     = pyaudio.paInt32
        self.CHUNK      = 1024
        self.stream     = self.open(
            format      = self.FORMAT,
            channels    = self.CHANNELS,
            rate        = self.RATE,
            input       = input,
            output      = not input
        )
        # device_count = self.get_device_count()
        # for i in range(0, device_count):
        #     print("Name:", self.get_device_info_by_index(i)["name"])
        #     print("Index:", self.get_device_info_by_index(i)["index"])
        #     print("\n")
        


    def read(self):
        return self.stream.read(self.CHUNK)

    def write(self, data):
        self.stream.write(data)

    def close(self):
        self.stream.start_stream()
        self.stream.close()
        self.terminate()