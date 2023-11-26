import cv2
from PIL import Image, ImageDraw, ImageFont
import time
import numpy as np

# Function to add text to an image
def add_text(image, text, position, font_size=30, font_color=(255, 255, 255)):
    image = Image.fromarray(image)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", font_size)  # You may need to adjust the font file path
    draw.text(position, text, font=font, fill=font_color)
    return image

# Function to create a video with text and background
def create_video(output_path, text_list, background_path, video_duration=10, frame_rate=30, text_duration=1):
    background = cv2.imread(background_path)
    width, height = background.shape[1], background.shape[0]
    
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video = cv2.VideoWriter(output_path, fourcc, frame_rate, (width, height))

    for text in text_list:
        for i in range(int(frame_rate * text_duration)):
            frame = background.copy()

            # Add text to the frame
            position = (width // 4, height // 2)
            frame_with_text = add_text(frame, text, position)

            # Write the frame to the video
            video.write(cv2.cvtColor(np.array(frame_with_text), cv2.COLOR_RGB2BGR))
            
            # Sleep for the specified duration
            time.sleep(1 / frame_rate)

    video.release()

# Example usage
text_list = ["Hello, Toutube!", "Python  is awesome!", "You Know."]




background_path = "background.jpg"
create_video("output_video.mp4", text_list, background_path)
