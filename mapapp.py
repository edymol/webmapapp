import folium

# this creates a map location based on coordinates provided, places zoom % and what type of map "Bright Box" or current
mapa = folium.Map(location=[-2.307362, -78.120463], zoom_start=10, tiles="Stamen Terrain")

# Creating a variable to implement FeaturesGroup
fg = folium.FeatureGroup(name='My Map')

# Adding marker to variable created above
fg.add_child(folium.Marker(location=[-2.307362, -78.120463], popup="Marker", icon=folium.Icon(color='lightgray')))

# Passing fg variable changes to mapa variable.
mapa.add_child(fg)

# Saving changes.
mapa.save("Map1.html")

