# pip install youtube-dl pafy python-vlc
#-----------------------------------------------
import pafy
import vlc
from time import sleep

url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
video = pafy.new(url)
best = video.getbest()
playUrl = best.url

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playUrl)
Media.get_mrl()
player.set_media(Media)
print("before play")
player.play()
print("after play")

# prevent end of the run, so that there is time to run
# OTOH: now the video-window does not react to any "close button" anymore
sleep(6)
while player.is_playing():
    sleep(1)

#---------------------------
# outcome: works, but really awkward, there are no "controls" and nothing else to do
# but: this player could be used to schedule plays of the found song-videos ..
