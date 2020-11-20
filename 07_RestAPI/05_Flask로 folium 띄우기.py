from flask import Flask

import folium

app = Flask(__name__)

# nodejs웹 실행하듯이 cmd에서 실행

@app.route('/')
def index():
    start_coords = (37.550966, 126.849532)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)
