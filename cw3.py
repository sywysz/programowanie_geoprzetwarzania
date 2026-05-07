import arcpy

# arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\DANE_STUDENCI\ds'
# arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty'
arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\geoprzetwarzanie\geoprzetwarzanie.gdb'
arcpy.env.overwriteOutput = True

# if arcpy.Exists('nuts92'):
#     desc = arcpy.da.Describe('nuts92')
#     print(desc)
#     print(desc['baseName'])
#     print(desc['catalogPath'])
#     print(desc['shapeType'])
# else:
#     print('Warstwa nie istnieje')

lista = arcpy.ListFeatureClasses()
print(lista)