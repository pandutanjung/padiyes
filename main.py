import json
import pandas as pd
import plotly.express as px

with open("indonesia.geojson") as f:
    geojson = json.load(f)

df = pd.read_csv("padiyes.csv")

df_reshaped = df.melt(
    id_vars=["Provinsi"],
    var_name="Year",
    value_name="Produktivitas Padi"
)

df_reshaped["Produktivitas Padi"] = pd.to_numeric(df_reshaped["Produktivitas Padi"].str.replace(",", ""), errors='coerce')

custom_colorscale = [           
    (0, "red"),
    (0.15, "yellow"),
    (1, "green")
]

fig = px.choropleth(
    df_reshaped,
    geojson=geojson,
    locations="Provinsi",
    featureidkey="properties.state",
    animation_frame="Year",
    color="Produktivitas Padi",
    color_continuous_scale=custom_colorscale,
    labels={"Produktivitas Padi": "Produktivitas Padi (Ton)"},
)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
    title={
        "text": "Produktivitas Padi di Indonesia",
        "xanchor": "center",
        "x": 0.5,
        "yanchor": "top",
        "y": 0.9,
    }
)
fig.show()

# simpan ke file HTML
fig.write_html("peta_interaktif.html")