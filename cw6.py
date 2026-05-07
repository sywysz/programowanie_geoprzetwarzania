import arcpy

# arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\DANE_STUDENCI\raster — kopia'
# arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty'
arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\geoprzetwarzanie\geoprzetwarzanie.gdb'
arcpy.env.overwriteOutput = True

for field in arcpy.ListFields('nuts92'):
    print(f'Kolumna {field.name} ma typ {field.type}.')

print('\n')

for field in arcpy.ListFields('nuts92', field_type='String'):
    print(f'Kolumna {field.name} ma typ {field.type}.')