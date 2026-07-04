import cv2 as cv
import os 

N = int(input("Enter the number of frames you want to sample: "))
# Open your video file or stream
cap = cv.VideoCapture('outpy.avi')

if not cap.isOpened():
    print("Error: Could not open the video source.")
    exit()
framesObj = {}
total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

i = 1
while (True):
    ret,frame = cap.read()


    if i <= N:
        framesObj[f"frame_{i}.jpg"] = frame 
        i += 1
    else:
        break
    if not ret:
        print("Video playback finished.")
        break




cap.release()
cv.destroyAllWindows()
folder = "output"
for file_name,frame in framesObj.items():
    success = cv.imwrite(os.path.join(folder,file_name),frame)
    if success:
        print(f"Image saved successfully {file_name}!")
    else:
        print(f"Failed to save the image")
    print()

print(f"Total frames in video  : {total_frames}")
print(f"Frames sampled         : {i}")
print("Saved to                : output/")