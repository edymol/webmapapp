import folium

mapa = folium.Map(location=[-2.307362, -78.120463], zoom_start=15)
mapa.save("Map1.html")
print(type(mapa))
