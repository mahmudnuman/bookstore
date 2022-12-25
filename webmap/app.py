import folium
map=folium.Map(location=[23.82368, 90.3605], zoom_start=12, tiles="OpenStreetMap")

feature_group=folium.FeatureGroup(name="Python Practice Maps")

coordinates=[[23.823783751620876, 90.36045035484473],
 [23.822838343980305, 90.36355074522358],
 [23.822779985252616, 90.36194951480202]]

for coordinate in coordinates:
    

    feature_group.add_child(folium.Marker(location=coordinate,
                            popup="Hello I am here",
                            icon=folium.Icon(color="pink")))

map.add_child(feature_group)

map.save("map1.html");