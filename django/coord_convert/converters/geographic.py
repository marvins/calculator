#

#  Pyproj
from pyproj import Proj, Transformer

def convert_coordinates( input_coord ):

    #  Get coordinate type
    pass


def geographic_to_ecef( lat_deg:    float,
                        lon_deg:    float,
                        elev_m:     float = 0,
                        datum:      str   = 'WGS84',
                        ellipsoid:  str   = 'WGS84' ):

    ecf_proj = Proj( proj = 'geocent', ellps = ellipsoid, datum = datum )
    geo_proj = Proj( proj = 'latlong', ellps = ellipsoid, datum = datum )
    
    xform = Transformer.from_proj( geo_proj, ecf_proj, always_xy=True )
    x, y, z = xform.transform( lon_deg, lat_deg, elev_m, radians=False )

    return { 'x': x, 'y': y, 'z': z }


