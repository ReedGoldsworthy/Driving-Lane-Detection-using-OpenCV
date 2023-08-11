# Real-Time Lane Detection with OpenCV

A python program that uses OpenCV to detect the lanes on a road from a video

## Dependencies

This project uses two external python libraries: opencv-python and numpy.
These can be downloaded by entering pip install opencv-python in the terminal if pip is installed

## Usage

1). Fill the `frames` folder with PNGs of the frames from the video you would like to run the program on.

2). run the program from the command line, as follows:

<pre>python main.py 
</pre>

After running the program, the output frames will be stored in the `output frames` folder and joined into a video stored as `output_video.mp4`

# Result

 ![ezgif com-optimize (1)](https://github.com/ReedGoldsworthy/Driving-Lane-Detection-using-OpenCV/assets/59662986/fa41426d-1bfd-4d47-ac89-50fc2337f2fb) ![ezgif com-optimize](https://github.com/ReedGoldsworthy/Driving-Lane-Detection-using-OpenCV/assets/59662986/0d570c3c-f503-4653-9855-fe83afcbcee7)



# How It Works

### First, we apply a mask to all the frames of our input video. This way we can ignore the unwanted objects from the driving scene.

![masking](https://github.com/ReedGoldsworthy/Driving-Lane-Detection-using-OpenCV/assets/59662986/9fb7f5ab-0d3c-4abc-b841-8403ee7f8fe3)


### Next, we apply image thresholding. This assigns a pixel a black or white value depending on a certain threshold.

![thresholding](https://github.com/ReedGoldsworthy/Driving-Lane-Detection-using-OpenCV/assets/59662986/f655700f-5c5d-4940-8996-19d5841a967e)


### Finally, we apply a [Hough Line Transformation](https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html) to detect the lane markings and draw the markings back onto the original frame

![transformation](https://github.com/ReedGoldsworthy/Driving-Lane-Detection-using-OpenCV/assets/59662986/7335010a-a5d3-49f1-8ce4-f82afbbf8e25)





  







