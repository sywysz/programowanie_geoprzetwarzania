import arcpy

arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\geoprzetwarzanie\geoprzetwarzanie.gdb'
arcpy.env.overwriteOutput = True

# Ćwiczenie 1
# with arcpy.da.SearchCursor('rstations92', ['NAME', 'SHAPE@XY']) as s_kursor:
#     for row in s_kursor:
#         x,y = row[1]
#         print(f'Stacja {row[0]}, X: {x:.2f}, Y: {y:.2f}')

# Ćwiczenie 2
# total_pow: float = 0.0

# with arcpy.da.SearchCursor('powiatyds', ['POWIAT', 'SHAPE@AREA']) as search:
#     for row in search:
#         total_pow += row[1]

# pow_km2 = total_pow / 1000000

# print(f'Powierzchnia całkowita wynosi {pow_km2:.2f} km2.')

# Ćwiczenie 3
# road_length = 0

# with arcpy.da.SearchCursor('roads92', ['KL_ADMIN', 'NR_DROGA_N', 'SHAPE@LENGTH']) as search:
#     for row in search:
#         if row[0] in ['K', 'W'] and row[2] > 1000:
#             print(f'Droga {row[0]} o numerze {row[1]}, długość {row[2] / 1000} km.')
#             road_length += row[2]

# print(f'Długość wszystkich dróg to {road_length / 1000} km.')

# Ćwiczenie 4
# geom = 'geom_python'
geom = 'geom_python_multi'

with arcpy.da.SearchCursor('geom_python', ['OID@', 'SHAPE@']) as search:
    for row in search:
        print(f'Obiekt {row[0]}')
        for point in row[1].getPart(0):
            print(f'X: {point.X}, Y: {point.Y}')