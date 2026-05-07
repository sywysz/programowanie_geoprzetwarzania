import arcpy

# arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\DANE_STUDENCI\ds'
# arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty'
arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\geoprzetwarzanie\geoprzetwarzanie.gdb'
arcpy.env.overwriteOutput = True

lista = arcpy.ListFeatureClasses()
print(lista)

lista.sort(reverse=True)
for el in lista:
    print(el)