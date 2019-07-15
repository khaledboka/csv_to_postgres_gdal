from osgeo import ogr
ogr.UseExceptions()

inDataSource = ogr.Open("power_towers.vrt")
lyr = inDataSource.GetLayer('power_towers')
for feat in lyr:
    geom = feat.GetGeometryRef()
    print geom.ExportToWkt()

# Dump CSV file into Postgres
# ogr2ogr -nln power_towers -f PostgreSQL PG:"dbname='te_data' host='localhost' port='5432'  user='postgres' password='123456'" -lco schema='new_one' power_towers.vrt

# -nln power_towers : new output table layer name
# -f PostgreSQL : Driver Name
# PG:"dbname='te_data' host='localhost' port='5432'  user='postgres' password='123456'" : Connection String
# -lco schema='new_one' : Layer creation options
# power_towers.vrt : predefined .vrt file for existing csv