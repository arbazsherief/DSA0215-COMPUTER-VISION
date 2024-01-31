import cv2
video_path = "C:\\Users\\arbaz\\Videos\\2024-01-16_1705393778110.mp4"
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open the video file.")
    exit()
frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()
for frame in reversed(frames):
    cv2.imshow("Video in Reverse", frame)
    if cv2.waitKey(30) & 0xFF == 27:
        break
cv2.destroyAllWindows()
play_video('your_video.mp4') 
 
