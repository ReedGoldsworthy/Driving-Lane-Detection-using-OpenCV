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
## &emsp;&emsp;&emsp; &emsp; &emsp; &emsp; &emsp; Before &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;        &emsp; &emsp;  &emsp;    After        

![ezgif com-optimize (1)](https://github.com/ReedGoldsworthy/Driving-Lane-Detection-using-OpenCV/assets/59662986/2fa61a80-9b6a-4002-8d68-b3d8093544e4) ![ezgif com-optimize](https://github.com/ReedGoldsworthy/Driving-Lane-Detection-using-OpenCV/assets/59662986/3d54c665-2b56-460f-8955-6b51527d2c23) 

# How It Works

### First, we apply a mask to all the frames of our input video. This way we can ignore the unwanted objects from the driving scene.

![image](https://github.com/ReedGoldsworthy/Driving-Lane-Detection-using-OpenCV/assets/59662986/289e1d8c-89b7-4013-ab0a-8d7f4810259f)

### Next, we apply image thresholding. This assigns a pixel a black or white value depending on a certain threshold.

![image](https://github.com/ReedGoldsworthy/Driving-Lane-Detection-using-OpenCV/assets/59662986/c98c7166-66de-4356-9d76-69fdffa0e9d6)

### Finally, we apply a [Hough Line Transformation](https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html) to detect the lane markings and draw the markings back onto the original frame

![image](https://github.com/ReedGoldsworthy/Driving-Lane-Detection-using-OpenCV/assets/59662986/ec8a24d7-affd-4c64-ac5a-b35b26c8ed94)




  







