# Import modules and enable overwrite
import sys, os, arcpy

# Allow for user to select a dataset, and then describe the dataset
dataset = arcpy.GetParameterAsText(0)
description = arcpy.da.Describe(dataset)

# Acess the minimums and maximums for the extent within the dataset, rounded to the tenths place
xmin = round(description["extent"].XMin, 1)
ymin = round(description["extent"].YMin, 1)
xmax = round(description["extent"].XMax, 1)
ymax = round(description["extent"].YMax, 1)

# Adding catalog path from description dictionary
arcpy.AddMessage("The catalog path is " + description["catalogPath"])

# Adding extent values after converting to string variables because they are retrieved as float type data
arcpy.AddMessage("XMin: " + str(xmin))
arcpy.AddMessage("YMin: " + str(ymin))
arcpy.AddMessage("XMax: " + str(xmax))
arcpy.AddMessage("YMax: " + str(ymax))

# Differentiating between feature classes and raster types, returning different variables for each
if description["datasetType"] == "FeatureClass":
    arcpy.AddWarning("Shape Type : " + description["shapeType"])
elif description["datasetType"] == "RasterDataset":
    arcpy.AddWarning("Format: " + description["format"])
    arcpy.AddWarning("# of rows: " + str(description["height"]))
    arcpy.AddWarning("# of cols: " + str(description["width"]))

