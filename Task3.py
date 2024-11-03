# Import modules and enable overwrite
import sys, os, arcpy
arcpy.env.overwriteOutput = True

# Set workspace environment
arcpy.env.workspace = "V:/env859_ps4/Data"

# Check arcpy license   
if arcpy.CheckProduct("ArcInfo") != "Available":
    msg = 'The proper ArcGIS license is not available'
    print(msg)
    sys.exit(msg)

# Create a list of all BMR feature classes
BMR_feature_classes = arcpy.ListFeatureClasses("BMR*", "", "")

# Create a loop to iterate through and split feature classes
for FC in BMR_feature_classes:

    # Create folder for each iteration, renaming each folder without the extension name 
    # (it took me a while to figure out that if the folder had a .shp as part of its name,
    # then the split function wouldn't correctly identify it as a workspace)
    out_folder_path = "V:/env859_ps4/Scratch"
    folder_name = FC[:-4]
    out_name = "{}".format(folder_name)
    new_folder = arcpy.management.CreateFolder(out_folder_path, out_name)

    # Define variables for split analysis
    in_features = "V:/env859_ps4/Data/{}".format(FC)
    split_features = "V:/env859_ps4/Data/TriCounties.shp"
    split_field = "CO_NAME"

    arcpy.analysis.Split(in_features, split_features, split_field, new_folder)
