# Spermatid-Image-Analysis
The Spermatid Identification Model is a nueral network that can be used to predict the step of spermatids that have been stained with DAPI to mark nucleic material.  Manually identifying these spermatids can be inaccurate, tedious, time-expensive and so developing a method of accurately performing this process can be very beneficial. The Spermatid Identification Model allows for this identification with realistic accuracy and consistency. The model specifically identifies spermatids in stages 8-15+ and with an accuracy of TODO.   Trained on TODO images, the model was tested on a data set of TODO images from each step.  The model is a standard convolutional nueral network with 3 convolutional layers and 2 dense layers and takes in 800x800 color images in jpg format.  However the model can take larger images it will simply resize to 800x800.  In order to download and use the model follow the instructions outlined in this overview.  

## How to use
In order to use the model, download this repository and open a terminal or virtual environment with access to the standard python library.  For users umfamiliar with this process, it is recommended to download anaconda which includes several tools but specifically the standard python library and an easy to use terminal.  In order to do this follow this [link](https://www.anaconda.com/download) and download the correct version for your operating system.

From there open the Anaconda Prompt from the windows search bar.  This terminal will be the main interface for the model.  Once the terminal is opened navigate to the SIM folder (unzip the folder first) by typing the following command, replacing 'example path' with the path to the folder.
```
(base) C:\Users\Cristian Finley> cd C:\Users\Download\Spermatid-Image-Analysis
```
Once within the SIM folder begin a python prompt by typing python in the prompt, as shown below.  Once this is completed you should see `>>>` and this is where all commands for predicting on images or training will be entered.
```
(base) C:\Users\CristianFinley\Downloads\Spermatid-Image-Analysis> python
    >>>
```

## Commands
There are three main commands available to users:  `SIMpredict.py`, `SIMpredictbatch.py`, and `SIMtraining.py`.  Descriptions and examples of each of these commands will be show here.  SIMpredict evaluates a single image, SIMpredictbatch evaluates a folder of images and returns a csv of the results, and SIMtraining allows for easy training of the model.  Each process has a description that can be seen by calling the command and `--help`


#### SIMpredict

