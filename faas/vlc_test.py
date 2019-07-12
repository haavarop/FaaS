import vlc
video_path = "/video/important_video.mp4" # Path to video file 
print("Playing important videos")

Instance = vlc.Instance('--fullscreen')
player = Instance.media_player_new()
Media = Instance.media_new(video_path)
Media.get_mrl()
player.set_media(Media)
player.play()

while True:
    pass