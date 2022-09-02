from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px

from _histogram import *
from _map import *
from _controllers import *
from app import app

# ========================================
# Data ingestion
# ========================================

df_data = pd.read_csv("dataset/cleaned_data.csv", index_col = 0) #Importando dados
mean_lat = df_data["LATITUDE"].mean() #convertendo lat para melhor entendimento
mean_long = df_data["LONGITUDE"].mean() #convertendo lon para melhor entendimento

df_data["size_m2"] = df_data["GROSS SQUARE FEET"] / 10.764 #convertendo metragem para melhor entendimento
df_data = df_data[df_data["YEAR BUILT"]>0] # Filtrando anos zeradas
df_data["SALE DATE"] = pd.to_datetime(df_data["SALE DATE"]) # Convertendo data para datetime


# Normalizando os dados para estar harmonico no dash
df_data.loc[df_data["size_m2"]>10000, "size_m2"] = 10000
df_data.loc[df_data["SALE PRICE"]>50000000, "SALE PRICE"] = 50000000
df_data.loc[df_data["SALE PRICE"]<10000, "SALE PRICE"] = 10000


# ========================================
# Layout
# ========================================


# Container dbc
app.layout = dbc.Container(
        children=[
                dbc.Row([
                        dbc.Col([controllers], md=3),
                        dbc.Col([map, hist], md=9),
                ])

        ], fluid=True,)

# ========================================
# Callbacks
# ========================================

@app.callback([Output("hist-graph", 'figure'), Output("map-graph", 'figure')], 
                [Input("location-dropdown", 'value'),
                 Input("slider-square-size", 'value'),
                 Input("dropdown-color", 'value')])

def update_hist(location, square_size, color_map):
        if location is None:
                df_intermediale = df_data.copy()
        else:
                df_intermediale = df_data[df_data["BOROUGH"]== location] if location != 0 else df_data.copy()
                size_limit = slider_size[square_size] if square_size is not None else df_data["GROSS SQUARE FEET"].max()
                df_intermediale = df_intermediale[df_intermediale["GROSS SQUARE FEET"]<= size_limit]

        hist_fig = px.histogram(df_intermediale, x = color_map, opacity=0.75)
        hist_layout = go.Layout(
                margin = go.layout.Margin(l=10, r=0, t=0, b=50),
                showlegend = False, 
                template = "plotly_dark",
                paper_bgcolor = "rgba(0,0,0,0)")
        
        

        px.set_mapbox_access_token(open("Keys/mapbox_key").read())

        colors_rgb = px.colors.sequential.GnBu
        df_quantiles = df_data[color_map].quantile(np.linspace(0,1, len(colors_rgb))).to_frame()
        df_quantiles = (df_quantiles - df_quantiles.min()) / (df_quantiles.max() - df_quantiles.min()) #Normalização
        df_quantiles["colors"] = colors_rgb
        df_quantiles.set_index(color_map, inplace = True)

        color_scale = [[i,j] for i, j in df_quantiles['colors'].iteritems()]

        map_fig = px.scatter_mapbox(df_intermediale, lat="LATITUDE", lon="LONGITUDE", 
                color = color_map, size="size_m2", size_max= 15, zoom=10, opacity=0.4)

        map_fig.update_coloraxes(colorscale = color_scale)
        map_fig.update_layout(mapbox=dict(center=go.layout.mapbox.Center(lat=mean_lat, lon =mean_long)),
                template = "plotly_dark", paper_bgcolor = "rgba(0,0,0,0)",
                margin = go.layout.Margin(l=10, r=10, t=10, b=10),)

        hist_fig.layout = hist_layout
        return hist_fig, map_fig

if __name__ == '__main__':
    app.run_server(debug=False)
    #app.run_server(debug=True, port="8051")