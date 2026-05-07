import arcpy

# arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\DANE_STUDENCI\ds'
arcpy.env.workspace = r'C:\Users\364264\Documents\skrypty\geoprzetwarzanie\geoprzetwarzanie.gdb'
arcpy.env.overwriteOutput = True

lista = ['roads92', 'rail92']
doc = 'docinana'

for el in lista:
    arcpy.analysis.Clip(el, 'wrocbuf', f'{doc}_{el}')

arcpy.management.Merge([f'{doc}_{el}' for el in lista], 'transport_wroc.shp')

stbuf = 'stacje_buf1000'
wrbuf = 'wrocbuf'
arcpy.analysis.Buffer('rstations92', stbuf, '1000 meters')
arcpy.analysis.Clip(stbuf, wrbuf, f'{stbuf}_{wrbuf}')
arcpy.analysis.Intersect(['transport_wroc', f'{stbuf}_{wrbuf}'], 'transport_przy_stacjach')

count = int(arcpy.management.GetCount('transport_przy_stacjach')[0])

if count > 0:
    print(f'Znaleziono elementy. Liczba elementów wynosi {count}.')
else:
    print('Nie znaleziono elementów')