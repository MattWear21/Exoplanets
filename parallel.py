#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 23:20:47 2020

@author: mattwear
"""

###Paralell coordinates plot of habitable exoplanets
#highlight proxima, teegaarden and perhaps some of the trappist planets
#Brush out the other planets
#Green baseline for Earth as a reference

parallel_df = phl_df[phl_df['P_HABITABLE']>=1].copy()
parallel_df['P_GRAVITY_EST'] = ((G * Me * parallel_df['P_MASS_EST'])/((Re * parallel_df['P_RADIUS_EST'])**2))/9.8
parallel_df['Colour'] = 0
parallel_df.loc[3818, 'Colour'] = 1
parallel_df.loc[3779, 'Colour'] = 0.5

fig = go.Figure(data=
    go.Parcoords(
        line = dict(color = parallel_df['Colour'],
                   colorscale = [[0,'#dbdbdb'],[0.5,'blue'],[1,'purple']]),
        dimensions = list([
            dict(range = [0,2],
                label = 'Gravity', values = parallel_df['P_GRAVITY_EST']),
            dict(range = [0,2],
                label = 'Illumination', values = parallel_df['P_FLUX']),
            dict(range = [0,2],
                label = 'Temperature', values = parallel_df['P_TEMP_EQUIL']/255)
        ])
    )
)

#fig.update_layout(
#    plot_bgcolor = 'white',
#    paper_bgcolor = 'white',
#    dragmode=False
#)

config = {
        'displayModeBar': False
}

fig.write_html("Plots/parallel.html", include_plotlyjs=False, full_html=False, config=config)

fig.show()