# This is a sample Python script.
import folium


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def mapapp(app):
    mapa = folium.Map(location=[-2.307362, -78.120463], zoom_start=15)
    mapa.save("Map1.html")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mapapp(mapa)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
