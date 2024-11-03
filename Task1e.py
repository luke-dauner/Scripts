# Import modules
import sys, os, arcpy

# Set workspace 
arcpy.env.workspace = "V:/env859_ps4/Data"

# Enable overwrite 
arcpy.env.overwriteOutput = True 

# Iterating through a range of buffer distances and producing a new output each time
for distance in range(100, 501, 100):
    in_features = "streams.shp"
    buff_dist = distance
    out_feature_class = "V:/env859_ps4/Scratch/buff_{}m.shp".format(buff_dist)

    # Run Buffer tool and print messages
    arcpy.Buffer_analysis(in_features, out_feature_class, buff_dist,"", "", "ALL", "", "PLANAR")
    print(arcpy.GetMessages())


