import arcpy

arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\geoprzetwarzanie\geoprzetwarzanie_kopia.gdb'
arcpy.env.overwriteOutput = True

kursor = arcpy.da.SearchCursor('powiatyds', ['POWIAT'])

for row in kursor:
    print(f'Powiat {row[0]}')

