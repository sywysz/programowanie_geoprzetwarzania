import arcpy

arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\DANE_STUDENCI\raster — kopia'
# arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty'
# arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\geoprzetwarzanie\geoprzetwarzanie.gdb'
arcpy.env.overwriteOutput = True

for raster in arcpy.ListRasters():
    arcpy.management.BuildPyramids(raster)