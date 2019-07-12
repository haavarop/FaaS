import vlc
import time
video_path = "/video/important_video.mp4"  # Path to video file

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(video_path)
Media.get_mrl()
player.set_media(Media)
player.play()
# player.toggle_fullscreen()

is_playing = True
sensor_value = False


def sensor_read():
    # TODO: Add rpi GPIO
    pass


while True:
    time.sleep(0.01)
    if player.get_state() == vlc.State.Ended:
        print("Done")
        player.set_media(Media)
        player.play()

    if sensor_value != is_playing:
        if is_playing:
            print("Playing video")
        else:
            print("Pausing video")
        is_playing = sensor_value

    sensor_read()
