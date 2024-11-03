# Import modules
import sys, os, arcpy

# Set workspace 
arcpy.env.workspace = "V:/env859_ps4/Data"

# Enable overwrite 
arcpy.env.overwriteOutput = True 

# Setting local variables
in_features = "streams.shp"

# Allowing user input for parameters (and specifying meters as unit)
buffer_distance = arcpy.GetParameterAsText(0) + " meters"
out_feature_class = arcpy.GetParameterAsText(1)

# Run Buffer tool and print messages
arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance,"", "", "ALL", "", "PLANAR")
print(arcpy.GetMessages())


