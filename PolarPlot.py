#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:13:44 2020

@author: mattwear
"""

import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

#Import and clean the data
phl_df = pd.read_csv("Data/phl_exoplanet_catalog.csv")
phl_df.loc[3779,'P_NAME'] = 'Proxima Centauri b'

close_df = phl_df[['P_HABITABLE', 'S_DISTANCE', 'P_NAME']].copy()
close_df = close_df[close_df.S_DISTANCE < 9.19].copy()
close_df['theta'] = np.random.rand(close_df.shape[0]) * 360
close_df.replace({'P_HABITABLE': 2}, 1, inplace=True)
close_df.replace({'P_HABITABLE': 1}, 'Habitable', inplace=True)
close_df.replace({'P_HABITABLE': 0}, 'Unhabitable', inplace=True)
close_df.loc[3779,'theta'] = 340

hab_df = close_df[close_df['P_HABITABLE'] == "Habitable"].copy()
unhab_df = close_df[close_df['P_HABITABLE'] == "Unhabitable"].copy()
    

fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=hab_df.S_DISTANCE*3.26156, 
                              theta=hab_df.theta, 
                              mode='markers',
                              name="Habitable",
                              marker_color='#3ec1d3',
                              showlegend=False,
                              hovertemplate='Planet: %{text}'+'<br>Light Years: %{r:.2f}'+'<extra></extra>',
                              text = list(hab_df['P_NAME'])
                              ))
fig.add_trace(go.Scatterpolar(r=unhab_df.S_DISTANCE*3.26156, 
                              theta=unhab_df.theta, 
                              mode='markers',
                              marker_color='#ff165d',
                              name='Not Habitable',
                              showlegend=False,
                              hovertemplate='Planet: %{text}'+'<br>Light Years: %{r:.2f}'+'<extra></extra>',
                              text = list(unhab_df['P_NAME'])))

fig.add_trace(go.Scatterpolar(r=[0], theta=[0], 
                              mode='markers', 
                              marker_size=20, 
                              marker_color='#21f700',
                              name='Habitable',
                              showlegend=False, 
                              hovertemplate='%{text}'+'<extra></extra>',
                              text = ['Earth']))


fig.add_annotation(text="Created by Matthew Wear. Data provided by the Planetary Habitability Laboratory.",
                  xref="paper", yref="paper",
                  font=dict(size=10, color='#a8a8a8'),
                  x=0, y=-0.1, showarrow=False)     

fig.update_layout(
    polar=dict(
        angularaxis = dict(
                showticklabels=False,
                ticks='',
                showgrid=False,
                showline=False
        ),
        radialaxis = dict(
                showline=False,
                showticklabels=False,
                ticks='',
                tickmode='array',
                tickvals=[5, 15, 29.9],
                gridcolor='#404040',
                range=[0,30]
        ),
        bgcolor='#313332'
   ),
   paper_bgcolor='#313332',
   title="Earth's Interstellar Neighbours<br><span style='font-size:14;'>All discovered <span style='color:#3ec1d3'>habitable</span> and <span style='color:#ff165d'>uninhabitable</span> exoplanets within 30 light years of <span style='color:#21f700'>Earth</span></span>",
   font_color="white",
   title_font_size=18,
   dragmode=False,
   width=800,
   height=800
)
        
config = {
        'displayModeBar': False
}

fig.write_html("Plots/polarplot.html", include_plotlyjs=False, full_html=False, config=config)


