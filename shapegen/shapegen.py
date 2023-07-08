import fiona
import pandas as pd
import sentinelhub as sh

config = sh.SHConfig()
config.sh_client_id= r'9bd0a46d-3d5b-4dc0-98b5-546b3635f9f3'
config.sh_client_secret = r'~)x%O:RiSc|F5i+SIL}^fZUlWOa.;E^{_:&!J6@:'
config.save()

gt = pd.read_csv("essential_gt_2012_tester.csv")

schema_props = ""
for col in list(gt.columns):
    schema_props += f"('{col}','str'),"

schema = {
    'geometry':'Point',
    'properties':[('pedlabsampnum','str'),('observation_date','int'),('date','date'),('ca_nh4_ph_7','float'),('mg_nh4_ph_7','float'),('na_nh4_ph_7','float'),('k_nh4_ph_7','float'),('exchangeable_sodium','float'),('cec7_clay_ratio','float'),('cec_nh4_ph_7','float'),('ph_cacl2','str')]
}

pointShp = fiona.open('../essential_2012/points_tester.shp', mode='w', driver='ESRI Shapefile', schema = schema, crs = "WGS84")

for index, row in gt.iterrows():
    
    dict_row_info = row.to_dict()
    del(dict_row_info["latitude_std_decimal_degrees"])
    del(dict_row_info["longitude_std_decimal_degrees"])

    row_dict = {
        "geometry": {'type':'Point', 'coordinates': (row["longitude_std_decimal_degrees"],row["latitude_std_decimal_degrees"])},
        "properties": dict_row_info
    }
    pointShp.write(row_dict)
pointShp.close()