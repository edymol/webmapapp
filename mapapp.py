import folium

mapa = folium.Map(location=[-2.307362, -78.120463], zoom_start=10, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name='My Map')
fg.add_child(folium.Marker(location=[-2.307362, -78.120463], popup="Marker", icon=folium.Icon(color='yellow')))
mapa.add_child(fg)
mapa.save("Map1.html")
print(type(mapa))
