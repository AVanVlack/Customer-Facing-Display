# -- Inital Commands --
INIT = bytearray(b'\x1b\x40')
CLEAR_DISPLAY = bytearray(b'\x0C')
CLEAR_LINE = bytearray(b'\x18')
SELF_TEST = bytearray(b'\x1F\x40')

# -- Write Mode Commands --
OVERWRITE_MODE = bytearray(b'\x1B\x11')
VERTICAL_MODE = bytearray(b'\x1B\x12')
HORIZONTAL_MODE = bytearray(b'\x1b\x13')

# -- Line Write Commands --
BOTTOM_LINE = bytearray(b'\x1b\x51\x42')
TOP_LINE = bytearray(b'\x1b\x51\x41')
TOP_LINE_SCROLL = bytearray(b'\x1b\x51\x44')
LINE_END = bytearray(b'\x0D')

# -- Motion Commands --
BLINK_LINE = b'\x1f\x11'
BLINK_LINE_CLEAR = b'\x1f\x12'
BLINK = bytearray(b'\x1F\x45')

# -- Time Commands --
DISPLAY_TIME = b'\x1b\x54'

# -- Curser Commands --
SET_CURSER_POSITION = bytearray(b'\x1B\x6C\x02')
MOVE_CURSER_UP = bytearray(b'\x1B\x5B\x41')
MOVE_CURSER_DOWN = bytearray(b'\x1B\x5B\x42')
MOVE_CURSER_LEFT = bytearray(b'\x1B\x5B\x44')
MOVE_CURSER_RIGHT = bytearray(b'\x1B\x5B\x43')
MOVE_CURSER_HOME = bytearray(b'\x1B\x5B\x48')
SHOW_CURSER = bytearray(b'\x1B\x5F')


# -- Device Setup Commands (ROM Setup) --
# Buadrate [02h][05h][42h] n [03h] 31 = 9600
BAUD = bytearray(b'\x02\x05\x42\x31\x03')
# Char Set [02h][05h][54h] n [03h] 00 = USA
CHAR_SET = bytearray(b'\x02\x05\x54\x00\x03')
# Command Set [02h][05h][43h] n [03h] 37 = CD5220
COMMAND_SET = bytearray(b'\x02\x05\x43\x30\x03')
DEMO = bytearray(b'\x02\x05\x44\x08\x03')         # [02h][05h][44h][08h][03h]
FIRMWARE = bytearray(b'\x02\x05\x56\x01\x03')     # [02h][05h][56h][01h][03h]
