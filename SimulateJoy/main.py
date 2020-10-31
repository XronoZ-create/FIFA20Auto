from device import DS4Device
import keyboard

def foo():
    print('key')
    DEVICES['localhost'].send('left-stick-Y', -1)


def foo2():
    print('key2')
    DEVICES['localhost'].send('left-stick-Y', 1)

DEVICES = {}

DEVICES['localhost'] = DS4Device('Windows', 'localhost')

keyboard.add_hotkey('w', foo)
keyboard.add_hotkey('q', foo2)
keyboard.wait('Ctrl + Q')


# for a in range(1,500):
#     DEVICES['localhost'].send('down-button', True)
#     time.sleep(1)

# device = DEVICES.pop(sid)
# device.close()