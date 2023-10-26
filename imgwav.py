from moviepy.editor import ImageClip, AudioFileClip, VideoFileClip

def combineimageaudio():
    image_path = 'C:/Users/Asha Rani K P/OneDrive/Documents/MD1/imaget.jpg'
    audio_path = 'C:/Users/Asha Rani K P/OneDrive/Documents/MD1/audio.wav'

# Load the image clip
    image_clip = ImageClip(image_path, duration=4)  # Set a default duration value

# Load the audio clip
    audio_clip = AudioFileClip(audio_path)

# Set the duration of the final video to match the longer of the two clips
    duration = max(image_clip.duration, audio_clip.duration)

# Set the audio clip to the duration of the final video
    audio_clip = audio_clip.set_duration(duration)

# Set the audio of the image clip
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.fps = 24

# Write the final video with the combined image and audio
    output_path = 'C:/Users/Asha Rani K P/OneDrive/Documents/MD1/record.mp4'
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

def combinevideoaudio():
    video_path = 'C:/Users/Asha Rani K P/OneDrive/Documents/MD1/video.mp4'
    audio_path = 'C:/Users/Asha Rani K P/OneDrive/Documents/MD1/audio.wav'

# Load the image clip
    video_clip = VideoFileClip(video_path)  # Set a default duration value

# Load the audio clip
    audio_clip = AudioFileClip(audio_path)

# Set the duration of the final video to match the longer of the two clips
    duration = max(video_clip.duration, audio_clip.duration)

# Set the audio clip to the duration of the final video
    audio_clip = audio_clip.set_duration(duration)

# Set the audio of the image clip
    video_clip1 = video_clip.set_audio(audio_clip)
    video_clip1.fps = 24

# Write the final video with the combined image and audio
    output_path = 'C:/Users/Asha Rani K P/OneDrive/Documents/MD1/record1.mp4'
    video_clip1.write_videofile(output_path, codec='libx264', audio_codec='aac')
