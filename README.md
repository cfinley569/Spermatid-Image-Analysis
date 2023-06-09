# Spermatid Image Analysis
The Spermatid Identification Model is a nueral network that can be used to predict the step of spermatids that have been stained with DAPI to mark nucleic material.  Manually identifying these spermatids can be inaccurate, tedious, time-expensive and so developing a method of accurately performing this process can be very beneficial. The Spermatid Identification Model allows for this identification with realistic accuracy and consistency. The model specifically identifies spermatids in stages 8-15+.   Trained on TODO images, the model was tested on a data set of TODO images from each step and achieved an accuracy of TODO.  The model is a standard convolutional nueral network with 3 convolutional layers and 2 dense layers and takes in 800x800 color images in jpg format.  The model can take larger images, but it will simply resize to 800x800.  In order to download and use the model follow the instructions outlined in this overview.  

## How to use
In order to use the model, download this repository and open a terminal or virtual environment with access to the standard python library.  For users umfamiliar with this process, it is recommended to download anaconda which includes several tools but specifically the standard python library and an easy to use terminal.  In order to do this follow this [link](https://www.anaconda.com/download) and download the correct version for your operating system.

From there open the Anaconda Prompt from the windows search bar.  This terminal will be the main interface for the model.  Once the terminal is opened navigate to the SIM folder (unzip the folder first) by typing the following command, replacing the example path shown with your path to the folder.
```
(base) C:\Users\Cristian Finley> cd C:\Users\Downloads\Spermatid-Image-Analysis
```
Once within the SIM folder you can begin running files according to the process needed.  These files are outlined in the commands section below.

## Commands
There are three main commands available to users:  `SIMpredict.py`, `SIMpredictbatch.py`, and `SIMtraining.py`.  Descriptions and examples of each of these commands will be show here.  SIMpredict evaluates a single image, SIMpredictbatch evaluates a folder of images and returns a csv of the results, and SIMtraining allows for easy training of the model.  Each process has a description that can be seen by calling the command and `--help`


#### SIMpredict
To use SIMpredict type `SIMpredict.py` followed by the `imagepath` of the image you wish to predict on.  To use another nueral network or set of weights, the flags `--altmodel` and `--weights` can be called with the corresponding path added after the call.  

Example 1(suggested model and weights):
```
(base) C:\Users\Cristian Finley\Documents\GitHub\Spermatid-Image-Analysis>  python SIMpredict.py C:\Users\Cristian Finley\Downloads\image1
 ```
        
Example 2(alt model):
```
(base) C:\Users\Cristian Finley\Documents\GitHub\Spermatid-Image-Analysis>  python SIMpredict.py C:\Users\Cristian Finley\Downloads\image1 --altmodel alternatemodels\model2 --weights alternatemodels\model2weights
```

SIMpredict should be used to ensure that the model is working satisfactorily and to get acquinted with the output of the model.  Once familiar with the process proceed to SIMpredictbatch to predict on many images at once.

#### SIMpredictbatch
To use SIMpredictbatch, you first must create a folder with all of the images to be predicted on.  The images must be in jpg format and there cannot be any other files within the folder.  Once this is complete, run the file `SIMpredictbatch.py` followed by the path to the folder of images and the desired name of the output csv file.   Optional flags for using a different model and weights are available as `--altmodel` and `--weights`.

Example:
```
(base) C:\Users\Cristian Finley\Documents\GitHub\Spermatid-Image-Analysis>  python SIMpredictbatch.py C:\Users\Cristian Finley\Downloads\imagefolder resultsfile --altmodel \alternatemodels\model2 --weights alternatemodels\model2weights
```

#### SIMtraining
To train the model on a different or more extensive set of data, the SIMtraining function is available for this purpose.  Training an image analysis model often requires a large data set so be careful of training with fewer than 100 datapoints per class.  To train, run the file `SIMtraining.py` in the python prompt.  Following this, input an integer value for the number of `epochs` or total times the model train over the data set and the desired name of the image file containing the results of the training.

Optional flags allow for specification of the optimization function, loss function, model, and weights.

The training uses images in the folders testing images and training images, so adding or removing images to these folders will affect training.  For more information regarding training options refer to Tensorflow documentation to determine the desired optimizer, loss function, etc.

Example:
```
(base) C:\Users\Cristian Finley\Documents\GitHub\Spermatid-Image-Analysis>  python SIMtraining 10 resultsfile
```


-----


The Spermatid Identification Model is a work in progress, please post issues, suggestions, or data contributions and I will try to respond as soon as possible.  
