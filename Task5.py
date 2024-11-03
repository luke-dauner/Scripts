# Import modules and enable overwrite
import sys, os, arcpy

# Allow for user to select a dataset, and then describe the dataset
feature_class = arcpy.GetParameterAsText(0)
user_field = arcpy.GetParameterAsText(1)

# Create a point object
new_point = arcpy.Point(X=590000, Y=230000)

# Create a search cursor to look for user identified feature class and field
search_rows = arcpy.da.SearchCursor(feature_class,["Shape@", user_field])
  
# Use a For loop to iterate through all features in the feature class
for row in search_rows:
    recShape = row[0]
    
    # Determine if point falls within record shape, and print field attributes if so
    if recShape.contains(new_point) == True: 
        field_attribute = row[1]
        arcpy.AddMessage("The value for {} is {}".format(user_field, field_attribute))
