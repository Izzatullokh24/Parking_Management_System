# Parking Management System
 
This project is a Parking Management System that uses computer vision to detect and count parked cars in a parking lot. The system processes video footage to identify free and occupied parking spaces, providing a real-time count of available and occupied spots.

## Features

- Detects and counts parked cars in real-time using video footage.
- Displays the number of free and occupied parking spaces on the video feed.
- Allows for the manual addition and removal of parking spaces through mouse clicks on an image.

## Installation

1. **Clone the repository:**

    ```bash
    git https://github.com/Izzatullokh24/Parking_Management_System.git
    cd parking-management-system
    ```

2. **Install the required dependencies:**

    Ensure you have Python and `pip` installed, then run:

    ```bash
    pip install -r requirements.txt
    ```

    Create a `requirements.txt` file with the following content:

    ```plaintext
    opencv-python
    cvzone
    numpy
    ```
3. ** Prepare the Parking Space Positions:**

-Run parkingspacecounter.py to set up the parking spaces.
-Click on the parking spots in the carParkImg.png image to add them.
-Right-click on a parking spot to remove it.
-Positions are saved in the CarParkPos file.
