# import the necessary packages
import os
import re
import cv2
import numpy as np
import matplotlib.pyplot as plt
from os.path import isfile, join

#function that takes a folder of frames and an output video path and outputs the joined frames into a video with custom frame rate
def create_video_from_frames(frame_folder, output_video_path, frame_rate=30):
    frame_files = os.listdir('output frames/')
    frame_files.sort(key=lambda f: int(re.sub('\D', '', f)))

    if len(frame_files) == 0:
        print("No image files found in the folder.")
        return

    frame = cv2.imread(os.path.join(frame_folder, frame_files[0]))
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (width, height))

    for frame_file in frame_files:
        frame_path = os.path.join(frame_folder, frame_file)
        frame = cv2.imread(frame_path)
        out.write(frame)

#get frame file paths in sorted order
col_frames = os.listdir('frames/')
col_frames.sort(key=lambda f: int(re.sub('\D', '', f)))

col_images=[]

#reads every png inside of frames and saves the img np array into col_images
for file_path in col_frames:
    img = cv2.imread('frames/'+file_path)
    col_images.append(img)


# Create polygon mask
# create a zero array
stencil = np.zeros_like(col_images[300][:,:,0])
width, height, _ = col_images[0].shape
size = (width,height)

# specify coordinates of the polygon
polygon = np.array([[50,270], [220,160], [360,160], [480,270]])

# fill polygon with ones
cv2.fillConvexPoly(stencil, polygon, 1)



cnt = 0

#go through each frame as an image np array
for img in col_images:

    # apply polygon as a mask on the frame
    masked = cv2.bitwise_and(img[:,:,0], img[:,:,0], mask=stencil)
    

    # apply image thresholding
    ret, thresh = cv2.threshold(masked, 130, 145, cv2.THRESH_BINARY)

    # apply Hough Line Transformation
    lines = cv2.HoughLinesP(thresh, 1, np.pi/180, 30, maxLineGap=200)
    dmy = img.copy()


    # write the resulting image into output frames
    try:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(dmy, (x1, y1), (x2, y2), (0, 0, 255), 3)
        cv2.imwrite('output frames/'+str(cnt)+'.png',dmy)
  
    except TypeError: 
        cv2.imwrite('output frames/'+str(cnt)+'.png',img)

    cnt += 1


#takes the frames from input folder and joins them into mp4 video saved to output_video with the fps value
input_folder = "output frames/"
output_video = "output_video.mp4"
fps = 30

create_video_from_frames(input_folder, output_video, fps)

print("all done")