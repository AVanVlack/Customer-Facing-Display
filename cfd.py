import serial
from configs import pos7300 as config
import binascii


class CD5220:
    """Simple lib for working with 2x20 customer displays"""

    def __init__(self, port, buad=9600):
        self.port = port
        self.buad = buad

    def connect(self):
        self.serial = serial.Serial(self.port)
        self.init()
        # self.serial.write(b'Display is connected====================')

    def init(self):
        self.serial.write(config.INIT)

    def close(self):
        self.serial.close()

    def clear(self):
        self.serial.write(config.CLEAR_DISPLAY)

    def brightness(self, level):
        brightness = bytearray(b'\x1b\x2a\x01')
        self.serial.write(brightness)

    def write_top(self, text, scroll=0):
        byte_text = str.encode(text)
        command = config.TOP_LINE_SCROLL if scroll == 1 else config.TOP_LINE
        self.serial.write(command + byte_text + config.LINE_END)

    def write_bottom(self, text):
        byte_text = str.encode(text)
        top_line = bytearray(b'\x1b\x51\x42') + byte_text + bytearray(b'\x0D')
        self.serial.write(top_line)

    def set_mode(self, mode):  # overwrite, vertical, horizontal
        mode_config = mode.upper() + "_MODE"
        self.serial.write(getattr(config, mode_config))

    def settings(self):
        self.serial.write(config.COMMAND_SET)

    def self_test(self):
        self.serial.write(config.SELF_TEST)

    def demo(self):
        self.serial.write(config.DEMO)

    def blink_screen(self, rate):  # TODO: Easyer rate veriable
        self.serial.write(config.BLINK + bytes.fromhex(rate))

    def curser_absolute(self, x, y):
        self.serial.write(config.SET_CURSER_POSITION)
        # self.raw_write(config.SET_CURSER_POSITION + bytes(str(x),
        #                                                  'ascii') + bytes(str(y), 'ascii'))

    def show_curser(self, is_shown):
        showing = b'1' if is_shown else b'0'
        self.serial.write(config.SHOW_CURSER + showing)

    def write(self, text):
        self.serial.write(str.encode(text))

    def raw_write(self, raw):
        print(binascii.hexlify(raw, ' '))
        self.serial.write(raw)
