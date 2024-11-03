# Import modules and enable overwrite
import sys, os, arcpy
arcpy.env.overwriteOutput = True 

# Split road type multi-value string into a list
roads_type = "0;201;203" 
roads_type_list = roads_type.split(";")

# Loop through the road types and select to make separate feature classes
for type in roads_type_list:
    roads_in = "V:/env859_ps4/Data/Roads.shp"
    where_clause = "ROAD_TYPE = {}".format(type)
    output_FC = "V:/env859_ps4/Scratch/roads_{}.shp".format(type)
   
    # Execute Select
    arcpy.Select_analysis(roads_in, output_FC, where_clause)