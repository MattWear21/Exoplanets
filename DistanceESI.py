#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 13:36:05 2020

@author: mattwear
"""

###Scatter Plot: Distance vs ESI
df = phl_df[['P_ESI', 'P_NAME', 'S_DISTANCE', 'P_TYPE']].copy()
df.dropna(inplace=True)
df = df[df.S_DISTANCE < 10].copy()

terran = df[df['P_TYPE'] == 'Terran']
superterran = df[df['P_TYPE'] == 'Superterran']
neptunian = df[df['P_TYPE'] == 'Neptunian']
jovian = df[df['P_TYPE'] == 'Jovian']

fig = go.Figure()

fig.add_trace(go.Scatter(x=terran.S_DISTANCE, y=terran.P_ESI, mode='markers',
                         name='Earth-size'))
fig.add_trace(go.Scatter(x=superterran.S_DISTANCE, y=superterran.P_ESI, mode='markers',
                         name='Super-Earth'))
fig.add_trace(go.Scatter(x=neptunian.S_DISTANCE, y=neptunian.P_ESI, mode='markers',
                         name='Neptunian'))
fig.add_trace(go.Scatter(x=jovian.S_DISTANCE, y=jovian.P_ESI, mode='markers',
                         name='Jovian'))

fig.update_layout(
   dragmode=False
)

fig.update_xaxes(title_text='Distance (light years)',
                 showgrid=False)
fig.update_yaxes(title_text='Earth Similarity Index',
                 tickvals=[0, 0.2, 0.4, 0.6, 0.8, 1],
                 showgrid=False)

config = {
        'displayModeBar': False
}

fig.write_html("Plots/distanceESI.html", include_plotlyjs=False, full_html=False, config=config)


#More Viz Ideas
#A tour of the Trappist-1 solar system (polar plot)
#https://public.tableau.com/profile/brandon.pike#!/vizhome/TRAPPIST-1/INNERPLANETS
#A stat comparison of Proxima Centauri and/or Teegardens Star b to Earth (Bullet chart)
#Journey time to Proxima with various technologies (Bar Chart of time vs tech)