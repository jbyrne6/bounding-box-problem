from turf import polygon, bbox, bbox_polygon
from turf.invariant import get_geometry_from_features, get_coords_from_geometry
import json

def getPolygonBoundingBox(polygonGeomToGetBBox):
    # accepts valid geojson polygon geometry
    # Do I have to do data validation or is it assumed that I have a good geojson polygon geometry input?

    # get the polygon feature needed for the bbox calculation from the inputed geometry
    polygonToGetBBox = polygon(get_coords_from_geometry(polygonGeomToGetBBox))
    # get the minimum bounding box feature as a polygon
    bboxPolygonFeature = bbox_polygon( bbox(polygonToGetBBox))
    # get the geometry of the bounding box polygon
    bboxPolygonGeometry = get_geometry_from_features(bboxPolygonFeature)
    # return the minimum bounding rectangle as a GeoJSON polygon geometry
    return bboxPolygonGeometry

print("Please paste or type a geojson polygon geometry below to find it's bounding box: ")

# get a multiline input
geomLines=[]
while True:
    geomLine=input()
    if geomLine:
        geomLines.append(geomLine)
    else:
        break
# concatenate the multiple lines into a single string
testingPolygonGeomString = '\n'.join(geomLines)
# convert the string input to json for geojson processing
testingPolygonGeomJson = json.loads(testingPolygonGeomString)
# call the function to find the minimum bounding box
testPolygonBoundingBox = getPolygonBoundingBox(testingPolygonGeomJson)

# print the results
print("Your resulting minimum bounding rectangle in a GeoJSON polygon geometry format is: ")
print(testPolygonBoundingBox)
