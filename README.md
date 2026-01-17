# Cattle Shed Surveillance System

## Overview
The Cattle Shed Surveillance System is an innovative project designed to revolutionize dairy farming practices in Kerala. It utilizes advanced surveillance technology and object detection algorithms to monitor cattle health, behavior, and safety in real-time.

## Features
- Real-time monitoring of cattle movement and behavior
- Detection of signs of discomfort, stress, and disease symptoms
- Predator detection for enhanced cattle safety
- Automated alert system for timely intervention
- 24/7 surveillance capabilities

## Technologies Used
- Python
- OpenCV (cv2)
- YOLO (You Only Look Once) object detection algorithm
- Twilio API for alert notifications

## Dataset
The predator detection model was trained using a dataset available at:
https://app.roboflow.com/college2yr/predator_detection/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true

## Installation
1. Clone the repository:

git clone [https://github.com/nikzeeiiy/Cattle-Shed-Surveillance-System-]

2. Install the required dependencies:

pip install -r requirements.txt

3. Set up Twilio account and obtain API credentials.

## Usage
1. Run the predator detection script:

python predator.py

2. Run the pose estimation script:

python pose.py

## Configuration
- Update the Twilio account credentials in `predator.py`:
```python
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"


Adjust detection thresholds and parameters as needed in both scripts.

Project Structure

predator.py: Script for predator detection and alert system
pose.py: Script for cattle pose estimation and behavior analysis
videos/: Directory for input video files
output_images/: Directory for processed output images
runs/detect/train/: Directory containing the trained model details

Model Details
The trained model details can be found in the runs/detect/train/ directory. This includes model weights and configuration files.
Contributing
Contributions to improve the system are welcome. Please follow these steps:

Fork the repository
Create a new branch
Make your changes and commit them
Push to your fork and submit a pull request
