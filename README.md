# CHAT-GPT4-Time-Lapse

This is a Python program that automates the process of taking periodic images from a webcam and saving them with appropriate timestamps and labels. It is primarily designed for time-lapse photography projects or other similar applications where automated, periodic image capturing is required. 

Here's a step-by-step rundown of what the program does:

1. **Defining Resolution Options**: A predefined dictionary, `RESOLUTION_OPTIONS`, is created that allows users to choose from ten different image resolution options for the photos taken by the program.

2. **Creating Project Directory**: The `get_project_folder` function creates a new folder in the current working directory with a user-specified project name. If a directory with the same name already exists, it doesn't create a new one, instead uses the existing one. 

3. **Saving the Image**: The `save_image` function writes the image frame captured by the webcam to a file in PNG format. The file is saved in the project folder and is named with the project name and the timestamp of when the image was taken.

4. **Setting Camera Resolution**: The `set_camera_resolution` function adjusts the camera's resolution according to the user's choice.

5. **Selecting the Resolution**: The `select_resolution` function prompts the user to choose a resolution for the images. They have to input a number corresponding to one of the ten options. If they input an invalid number, the program asks them to enter it again until they provide a valid number.

6. **Specifying Time Between Photos**: The `input_time_between_photos` function allows the user to define the time interval between each photo taken. The user should enter the time in an 'HH:MM:SS' format.

7. **Adding Text to the Image**: The `put_text_on_image` function is used to overlay text on the image frames. This function is used to display the current timestamp and the project name on each image.

8. **Main Execution**: In the main function, the program prompts the user to enter a project name and then uses that name to create a new folder. The program then asks the user to select a resolution for the images and specify the time between photos. Once these inputs are provided, the program initiates the webcam, sets the resolution, and then enters a continuous loop where it captures an image, adds the timestamp and project name, saves the image, and then waits for the specified time before capturing the next image. This process continues until the user manually stops the program.

9. **Ending the Program**: The program can be stopped by a KeyboardInterrupt, commonly by pressing Ctrl+C. Once this happens, the camera is released, and any windows opened by OpenCV (the library used for the camera interface and image processing) are destroyed.

This program provides a simple yet powerful tool for automated image capturing from a webcam. It can be particularly useful for projects like time-lapse photography, monitoring systems, or any other application where periodic image capture is required. It's written in Python, which makes it relatively accessible for customization or further development according to specific user needs.
