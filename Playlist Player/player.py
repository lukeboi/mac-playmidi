import os
import subprocess
import atexit
import signal

def exit_handler():
    cmd = ['pkill -f playmidi-single']
    subprocess.Popen(cmd).wait()

atexit.register(exit_handler)
signal.signal(signal.SIGTERM, exit_handler)
signal.signal(signal.SIGINT, exit_handler)

directory = r'./Playlist'
while True:
    for filename in os.listdir(directory):
        if filename.endswith(".mid"):
            print(os.path.join(directory, filename))
            cmd = ['./playmidi-single', os.path.join(directory, filename)]
            subprocess.Popen(cmd).wait()
        else:
            continue


