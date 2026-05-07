import arcpy

arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\geoprzetwarzanie\geoprzetwarzanie.gdb'
arcpy.env.overwriteOutput = True

# with arcpy.da.SearchCursor('powiatyds', ['POWIAT', 'LUDN_1998']) as kursor:
#     for row in kursor:
#         print(f'Powiat {row[0]}, liczba ludności: {row[1]} mieszkańców.')


# # with arcpy.da.InsertCursor('powiatyds', ['POWIAT', 'LUDN_1998']) as insert_kursor:
# #    insert_kursor.insertRow(['Nowy powiat 2', 100000])

# with arcpy.da.SearchCursor('powiatyds', ['POWIAT', 'LUDN_1998']) as search_kursor:
#     for row in search_kursor:
#         print(f'Powiat: {row[0]}, liczba ludności {row[1]}')

# with arcpy.da.UpdateCursor('powiatyds', ['POWIAT']) as update_kursor:
#     for row in update_kursor:
#         if row[0] == 'Nowy powiat' or row[0] == 'Nowy powiat 2':
#             update_kursor.deleteRow()

# Ćwiczenie 6
# arcpy.management.AddField('powiatyds', 'typ', 'TEXT')

# with arcpy.da.UpdateCursor('powiatyds', ['LUDN_1998', 'typ']) as update_kursor:
#     for row in update_kursor:
#         if row[0] > 100000:
#             row[1] = 'duży powiat'
#         else:
#             row[1] = 'mały powiat'
#         update_kursor.updateRow(row)

# Ćwiczenie 8

# arcpy.management.AddField('powiatyds', 'upper', 'TEXT')

# with arcpy.da.UpdateCursor('powiatyds', ['POWIAT', 'upper']) as update_kursor:
#     for row in update_kursor:
#         row[1] = row[0].upper()
#         update_kursor.updateRow(row)

# Ćwiczenie 9

with arcpy.da.SearchCursor('powiatyds', ['POWIAT', 'LUDN_1998', 'POW_HA']) as search_kursor:
    for row in search_kursor:
        pop_density = row[1] / row[2]
        arcpy.analysis.Select('powiatyds', 'temp', f'"POWIAT" = \'{row[0]}\'')
        arcpy.analysis.Buffer('temp', f'{row[0]}_bufor', f'{100 * pop_density} METERS')
        arcpy.management.Delete('temp')