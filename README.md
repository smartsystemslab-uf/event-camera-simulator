# event-camera-simulator

This is python-based simulator for an event-camera. The simulator draws visual attention on a region-level. This indicates that instead of identifying events for each pixel, the design flow labels each region based on the spatio-temporal relevance.  

## PREREQUISITES

````$ conda env create -f environment.yml -n new_env_name````
Remember to define a new environment name in this step.

````$ pip install opencv-python````
Install opencv library

## HOW TO RUN 
````
$ conda activate new_env_name # make sure you have done the PREQUISITES step
$ python main.py
$ conda deactivate # when done
````

It will take all the images provided in the image_data/ directory and generate spatial and temporally relevant data separately. Please put your image dataset in the image_data/ directory and pass appropriate function parameters to generate the output.

The relevant data is generated in the *_output folders.  

You can also use command line arguments such as:  
````$ python3 main.py -i ./image_data -o ./ -s MAD -t 0.09```` # this appears to be how results in the spatial_output dir (hash 212a17a7d0b6dce099a7b6a0a4ac9593a0a65374) were made  
See main.py for more details.

## DESCRIPTION

1. The spatial_redundancy function implements the method to identify spatially redundant regions. Currently, the design has two methods to identify relevant regions. Edge point based relevance detection and statistical method (mean absolute deviation). To add addtional methods please edit the spatial.py file.  
2. The temporal_redundancy function implements the method to identify region-level temporal events.  
3. The method resizes all the incoming images by default as given in the above mentioned function if resize value is 1
  *. The resize parameters can be changed by editing the corresponding lines on the given functions.

If you installed a new package, be sure to update the conda environment file: ````conda env export --no-builds > environment.yml````

## NOTE
The output images generated by the simulator can be used to train a CNN model for classification and detection task.

Please look at my other repository to see how the custom datasets can be used for training a classifier:

https://github.com/jubaer-pantho/transfer-learning-CNN

To use the custom dataset on the pretrained YOLOv3 object detector use the following repository:

https://github.com/jubaer-pantho/yolo-v3-full-tiny




