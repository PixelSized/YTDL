import youtube_dl
import time as time
import os
import subprocess
from pathlib import Path

m4a = '140'

mp4_144p = '160'
mp4_240p = '133'
mp4_360p = '134'
mp4_480p = '135'
mp4_720p = '136'
mp4_1080p = '137'

gp3_176_144 = '36'
gp3_320_240 = '36'
flv = '5'
webm = '43'
mp4_640_360 = '18'
mp4_1280_720 = '22'

path = str(os.path.join(Path.home(), "Downloads"))

print("╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
print(r"""  __   _______ _   _ _____ _   _______ _____  ______ _____  _    _ _   _  _     _____  ___ ______ ___________ 
  \ \ / /  _  | | | |_   _| | | | ___ \  ___| |  _  \  _  || |  | | \ | || |   |  _  |/ _ \|  _  \  ___| ___ \
   \ V /| | | | | | | | | | | | | |_/ / |__   | | | | | | || |  | |  \| || |   | | | / /_\ \ | | | |__ | |_/ /
    \ / | | | | | | | | | | | | | ___ \  __|  | | | | | | || |/\| | . ` || |   | | | |  _  | | | |  __||    / 
    | | \ \_/ / |_| | | | | |_| | |_/ / |___  | |/ /\ \_/ /\  /\  / |\  || |___\ \_/ / | | | |/ /| |___| |\ \ 
    \_/  \___/ \___/  \_/  \___/\____/\____/  |___/  \___/  \/  \/\_| \_/\_____/\___/\_| |_/___/ \____/\_| \_|
    """)
print("╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝ \n")

a = input("\n What is the youtube videos URL? \n E.G: https://www.youtube.com/watch?v=dQw4w9WgXcQ \n →")


def run_command(command):
    p = subprocess.Popen(command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')




ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    meta = ydl.extract_info(
         a, download=False)
    formats = meta.get('formats', [meta])
for f in formats:
    print("\n " + f["format_id"] + ": | " + f['ext'] + " - " +f["format_note"])
 


b = input("\n\n What is the format you would like to download in? (see above numbers) \n")
print("Storing path as " + path)
try:
    with youtube_dl.YoutubeDL({'format': b, 'outtmpl':path + '/%(title)s.%(ext)s'}) as ydl:
        ydl.download([a])
        
except:
    print("\n\nThe youtube URL does not have this as an accepted format, review the video and check its accepted formats. \n Restarting in 5 seconds")

time.sleep(5)
print("\033[H\033[J")
   






