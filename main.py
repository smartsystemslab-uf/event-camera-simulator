import cv2
import numpy as np
from matplotlib import pyplot as plt
import os, glob
import spatial_op
import tif2jpg
import frame_gen
import temporal_op
import argparse

#use this module in case the images are given in "tif" format
#tif2jpg.tif2jpg_conv("image_data/")


#use this module to extract camera frames from video
#frame_gen.frame_generate("project.avi", "image_data/")

#default values
input_dir = './image_data/'
output_dir = './'
output_dir_spatial = output_dir + "spatial_output/"
output_dir_temporal = output_dir + "temporal_output/"
spatial_feature = 'edge'
threshold = 5
size = 8
resize = 1

# parse command line arguments
parser = argparse.ArgumentParser(description='run saliency/HARP on images')
parser.add_argument('-i','--input', help='input directory', required=False)
parser.add_argument('-o','--output', help='output directory', required=False)
parser.add_argument('-s','--spatial_feature', help='spatial feature', required=False)
parser.add_argument('-t','--threshold', help='threshold', required=False)
parser.add_argument('-z','--size', help='size', required=False)
parser.add_argument('-r','--resize', help='resize', required=False)

# trace
args = vars(parser.parse_args())
print( "command line arguments")
for k in args.keys():
  print( "{}: {}".format( k, args[k] ) )

# handle command line arg's (error checking, etc.)
if ( args["input"] ):
    input_dir = args["input"]
    if ( not os.path.exists(input_dir) ):
        print( "input_dir does not exist; exiting" )
        exit
if ( args["output"] ):
    output_dir = args["output"]    
    output_dir_spatial = output_dir + "spatial_output/"
    if ( not os.path.exists(output_dir_spatial) ):
        os.makedirs( output_dir_spatial )
    output_dir_temporal = output_dir + "temporal_output/"
    if ( not os.path.exists(output_dir_temporal) ):
        os.makedirs( output_dir_temporal )
if ( args["threshold"] ):
    tmp = float(args["threshold"])
    if ( tmp < 0 ):
        print( "threshold must be > 0; using default value" )
    else:
      threshold = tmp      
if ( args["spatial_feature"] ):
    spatial_feature = args["spatial_feature"]    
if ( args["size"] ):
    tmp = int(args["size"])
    if ( tmp < 0 ):
        print( "size must be >0; using default value" )
    else:
      size = tmp
if ( args["resize"] ):
    tmp = int(args["resize"])
    if ( tmp != 0 ):
        resize = 1
    else:
      resize = tmp      
print( "" )

#Please set the 'size' parameter in spatial and temporal folder if you want to resize the dataset images 
spatial_op.spatial_redundancy( input_dir, output_dir_spatial, spatial_feature, threshold, size, resize, filetype="*.png")
temporal_op.temporal_redundancy( input_dir, output_dir_temporal, threshold, size, resize, filetype="*.png")