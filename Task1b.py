# Import modules
import sys, os, arcpy

# Set workspace 
arcpy.env.workspace = "V:/env859_ps4/Data"

# Enable overwrite 
arcpy.env.overwriteOutput = True 

# Setting local variables
in_features = "streams.shp"
buffer_distance = "1000 meters"
out_feature_class = "V:/env859_ps4/Scratch/StrmBuff1km.shp"

# Run Buffer tool and print messages
arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance,"", "", "ALL", "", "PLANAR")
print(arcpy.GetMessages())


