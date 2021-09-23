import cfd
import time


# Setup and connect
display = cfd.CD5220("/dev/tty.usbmodemNT20091014001")
display.connect()
display.clear()

time.sleep(1)

# Line writing mode (Must call clear/init to continue other commands)


def line_modes():
    display.write_top("WILDHAR PNUT BTTR")
    display.write_bottom("               $3.99")
    time.sleep(2)
    display.clear()

# Write modes


def write_modes():
    display.set_mode("horizontal")  # overwrite, vertical, horizontal
    type_me = "Welcome to the little market!"
    for x in type_me:
        display.write(x)
        time.sleep(.2)
    time.sleep(2)
    display.clear()

# Curser position


def curser_position():
    display.curser_absolute(5, 1)
    display.write("44")
    display.curser_absolute(2, 2)
    display.write("Hello")
    time.sleep(2)

# Blink and scroll animations


def animations():
    display.write("Blink.... Blink... Blink")
    display.blink_screen("11")
    time.sleep(5)
    display.blink_screen("00")
    time.sleep(2)
    display.clear()
    display.write_top(" Top line scrolling ", 1)


# line_modes()
# write_modes()
# curser_position()
# animations()
# display.self_test()
display.raw_write(b'\x1b\x46\x44' +
                  str.encode("hello how are you doing today?     ") + b'\x0D')


# Close serial connection to display
display.close()
