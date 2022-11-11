class device:
      def __init__(self,type):
            self.type = type

      def enable(self):
            print("Your device is enabled")
      def disable(self):
            print("Disabling the device")
      def update_drive(self):
            print("Drivers are updating...")

class audio_device(device):
      def __init__(self, type,name):
            self.name=name
            super().__init__(type,name)
      
      def turn_on(self):
            print("Turned ON")

      def turn_off(self):
            print("Turning OFF..")

class Microphone(audio_device):
      def __init__(self, type, name):
            super().__init__(type, name)

      def start_record(self):
            print("recording started :)")
      def stop_record(self):
            print("Saved your recording")

class speaker(audio_device):
      def __init__(self,type,name,volume):
            self.volume=volume
            self.name=name
            super().__init__(type,name)
            
      def play(self):
            print("Playing Man without Love")
      def current_volume(self):
            print(f"Current Volume is {self.volume}")
      def inc_volume(self,volume):
            volume+=20
            print(f"Your volume is increased to {volume}")
      def dec_volume(self,volume):
            volume-=20
            print(f"Your volume is decreased to {volume}")

boat = speaker("speaker","boat",20)
samsung= device("mobile")
jbl = audio_device("mic","jbl")
note=Microphone("built-in","device")

samsung.current_volume()
samsung.inc_volume()
samsung.dec_volume()
samsung.update_drive()
samsung.turn_off()