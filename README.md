# Face Recognition Project
## Overview
My first image recognition project
Face recognition of base image and false positives/negatives

![image](https://github.com/barakshalit/facerecognition/assets/76451972/89a817ea-a687-42b7-aed8-aa0dc7196afd)

## Project’s goal:
The project’s goal is to write a code that could detect my face within 100 random images of people. 
While doing so, calculate the number of correct matches, false positive and false negative.

## Project’s structure:
#### Code and environment:
The code is written in Python, and i used the following libraries:
1.	face_recognition library (using dlib library)
2.	pygame - for displaying the current image that being tested and some live stats and rates regarding the detection.
The program is running on Unix machine (Ubunto 16.04.2 LTS).

#### Premises:
1.	The program will only get 1 image of myself to use as a reference during the project.
2.	The program will go through 100 images of random people (males and females, different skin tones, face structures, positions and ages).
3.	Although the program will only get 1 image of myself as base, I ran the program twice, each time with different base image of myself, to check deviations.
(In the attached files: “1.jpg” is the better base image and “falsepositiveBASE.jpg” will cause 1 false positive.

## Project’s results:
The program was able to detect my images in a very high accuracy, with both of the base images:
#### With “1.jpg” as base:  
100% accuracy, no false positive, no false negative.
#### With “falsepositiveBASE.jpg”:
99% accuracy (only 1 image: “3.jpg” was detected as match (false positive), although – this was an image of a mail with sunglasses, tilted to the right so only his profile was detected)


