import os
import cv2
from ultralytics import YOLO
from twilio.rest import Client

account_sid = "###############################"
auth_token = "################################"
client = Client(account_sid, auth_token)

call = client.calls.create(
  url="http://demo.twilio.com/docs/voice.xml",
  to="##########",
  from_="##########"
)

classes =['Pig','Elephant','Dog','Fox','Tiger']
VIDEOS_DIR = os.path.join('.', 'videos')
OUTPUT_DIR = os.path.join('.', 'output_images')

video_path = os.path.join(VIDEOS_DIR, 'tiger_test.mp4')
video_out_path = 'elephant_test_out.mp4'.format(video_path)

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()

# Check if frame is None
if frame is None:
    print("Error: Could not read the first frame from the video.")
    exit()

H, W, _ = frame.shape
out = cv2.VideoWriter(video_out_path, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

model_path = os.path.join('.', 'runs', 'detect', 'train', 'weights', 'best.pt')

# Load a model
model = YOLO(model_path) # load a custom model

threshold = 0.6
frame_count = 0

while ret:

    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            label = f"{results.names[int(class_id)]}: {score:.2f}"
            cv2.putText(frame, label, (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)           
            if results.names[int(class_id)].upper() in classes:
                print(call.sid)
                

    # Save the annotated frame as an image
    output_image_path = os.path.join(OUTPUT_DIR, f'frame_{frame_count}.jpg')
    cv2.imwrite(output_image_path, frame)

    # Display the frame in a window
    cv2.imshow('Processed Video', frame)

    out.write(frame)
    ret, frame = cap.read()
    frame_count += 1

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
