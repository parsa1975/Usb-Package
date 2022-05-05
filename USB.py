from os.path import exists as remain
class Usb():
  def __init__(self,usbAddress:str):
    self.l = usbAddress
  def check(self):
    return remain(self.l)
