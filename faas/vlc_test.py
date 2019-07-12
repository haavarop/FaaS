import vlc
import time
video_path = "/video/egg_meow.mp4" # Path to video file
print("Playing important videos")

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(video_path)
Media.get_mrl()
player.set_media(Media)
player.play()
#player.toggle_fullscreen()
while True:
    time.sleep(0.01)
    if player.get_state() == vlc.State.Ended:
        print("Done")
        player.set_media(Media)
        player.play()

