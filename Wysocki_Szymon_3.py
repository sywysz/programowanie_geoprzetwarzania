import arcpy

# arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\DANE_STUDENCI\raster — kopia'
arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\geoprzetwarzanie\geoprzetwarzanie_kopia.gdb'
arcpy.env.overwriteOutput = True

lista_linie = arcpy.ListFeatureClasses(feature_type='Line')
lista_poligony = arcpy.ListFeatureClasses(feature_type='Polygon')
# Zad 1
for line in lista_linie:
    for polygon in lista_poligony:
        arcpy.analysis.Clip(line, polygon, f'{polygon}_{line}')