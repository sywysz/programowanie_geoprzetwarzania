import arcpy

# arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\DANE_STUDENCI\ds'
# arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty'
arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\geoprzetwarzanie\geoprzetwarzanie.gdb'
arcpy.env.overwriteOutput = True
# print(arcpy.da.Describe('roads92')['shapeType'])
# proj = arcpy.Describe('nuts92.shp').spatialReference
# arcpy.management.CreateFeatureclass(r'C:\Users\364264\Documents\skrypty',
#                                     'lines.shp',
#                                     'POLYLINE',
#                                     spatial_reference=proj)

# if arcpy.Exists(r'C:\Users\364264\Documents\skrypty\lines.shp'):
#     print('Warstwa lines.shp istnieje.')
# else:
#     print('Warstwa lines.shp nie istnieje.')

infc = 'roads92'
clipfc = 'wrocbuf'
outfc = 'wroc_roads'

if arcpy.da.Describe(clipfc)['shapeType'] == 'Polygon':
    print(f'Warstwa {clipfc} jest poligonem.')
    arcpy.analysis.Clip(infc, clipfc, outfc)
    print(f'Stworzono warstwę {outfc}.')
else:
    print(f'Warstwa {clipfc} nie jest poligonem.')