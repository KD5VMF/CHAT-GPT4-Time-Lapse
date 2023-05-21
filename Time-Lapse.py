import cv2
import numpy as np
import time
from datetime import datetime, timedelta
import os

RESOLUTION_OPTIONS = {
    1: (640, 480),
    2: (800, 600),
    3: (1024, 768),
    4: (1280, 720),
    5: (1280, 1024),
    6: (1920, 1080),
    7: (1920, 1440),
    8: (2560, 1440),
    9: (3840, 2160),
    10: (4096, 2160),
}

def get_project_folder(project_name):
    folder_name = os.path.join(os.getcwd(), project_name)

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    return folder_name

def save_image(frame, folder, project_name, timestamp):
    filename = f"{project_name}_{timestamp}.png"
    file_path = os.path.join(folder, filename)
    cv2.imwrite(file_path, frame)
    print(f"Saved image: {file_path}")

def set_camera_resolution(camera, width, height):
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    print(f"Camera resolution set to: {width}x{height}")

def select_resolution():
    print("Choose a resolution:")
    for option, resolution in RESOLUTION_OPTIONS.items():
        print(f"{option}: {resolution[0]}x{resolution[1]}")

    while True:
        try:
            user_choice = int(input("Enter the number corresponding to your desired resolution: "))
            if user_choice in RESOLUTION_OPTIONS:
                return RESOLUTION_OPTIONS[user_choice]
            else:
                print("Invalid selection. Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")

def input_time_between_photos():
    while True:
        try:
            time_str = input("Enter the time between photos in the format 'HH:MM:SS': ")
            time_parts = time_str.split(':')
            if len(time_parts) == 3:
                hours, minutes, seconds = map(int, time_parts)
                return timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()
            else:
                print("Invalid input. Please enter time in the format 'HH:MM:SS'.")
        except ValueError:
            print("Invalid input. Please enter time in the format 'HH:MM:SS'.")

def put_text_on_image(frame, text, position):
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 1
    color = (255, 255, 255)
    thickness = 2
    cv2.putText(frame, text, position, font, scale, color, thickness)

def main():
    project_name = input("Enter a project name: ")
    project_folder = get_project_folder(project_name)
    resolution = select_resolution()
    time_between_photos = input_time_between_photos()

    camera = cv2.VideoCapture(0)
    set_camera_resolution(camera, resolution[0], resolution[1])

    try:
        while True:
            ret, frame = camera.read()
            timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            display_timestamp = timestamp.replace('_', ' ')
            put_text_on_image(frame, display_timestamp, (10, 30))
            put_text_on_image(frame, f"{project_name}_{timestamp}", (10, 60))
            save_image(frame, project_folder, project_name, timestamp)
            time.sleep(time_between_photos)
    except KeyboardInterrupt:
        print("Exiting program.")
    finally:
        camera.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
