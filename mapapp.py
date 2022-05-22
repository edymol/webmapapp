import folium
import pandas

data = pandas.read_csv("CoordData.csv")
lat = list(data["lat"])
lon = list(data["lon"])
elev = list(data["elevation"])


# to add elevation to map, create an elevation variable
# el = list(data.elevation)

def point_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# this creates a map location based on coordinates provided, places zoom % and what type of map "Bright Box" or current
mapa = folium.Map(location=[-2.307362, -78.120463], zoom_start=8, tiles="Stamen Terrain")

# Creating a variable to implement FeaturesGroup
fg = folium.FeatureGroup(name='My Map')

# Adding marker to variable created above
for lt, ln, el in zip(lat, lon, elev):  # add el to this iteration
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el) + " m",
                                     fill_color=point_color(el), color='grey', fill_opacity=0.7))
    # add el to popup = str(el) + " m"

# Passing fg variable changes to mapa variable.
mapa.add_child(fg)

# Saving changes.
mapa.save("Map1.html")
