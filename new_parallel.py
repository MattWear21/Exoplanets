#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:43:33 2021

@author: mattwear
"""

###Custom Parallel Coordinates Chart

parallel_df = phl_df[phl_df['P_HABITABLE']>=1].copy()
parallel_df['P_GRAVITY_EST'] = ((G * Me * parallel_df['P_MASS_EST'])/((Re * parallel_df['P_RADIUS_EST'])**2))/9.8
parallel_df = parallel_df[['P_NAME','P_GRAVITY_EST','P_FLUX','P_TEMP_EQUIL']].copy()
parallel_df['P_TEMP_EQUIL'] = parallel_df['P_TEMP_EQUIL']/255

teegarden = parallel_df[parallel_df['P_NAME']=="Teegarden's Star b"]
proxima = parallel_df[parallel_df['P_NAME']=="Proxima Cen b"]
trappd = parallel_df[parallel_df['P_NAME']=="TRAPPIST-1 d"]
parallel_df.drop([3818, 3779], inplace=True)

#Plot
fig = go.Figure()

for i in parallel_df.index:
    x_cur = [0, 1, 2]
    y_cur = [parallel_df.loc[i, 'P_GRAVITY_EST'],parallel_df.loc[i, 'P_FLUX'],parallel_df.loc[i, 'P_TEMP_EQUIL']]
    
    fig.add_trace(go.Scatter(x=x_cur, y=y_cur,
                        mode='lines',
                        name='Brush',
                        showlegend=False,
                        hoverinfo="skip",
                        line=dict(width=2),
                        marker=dict(color='#474747')))
   
fig.add_trace(go.Scatter(x=[0,1,2], y=[1,1,1],
                    mode='lines',
                    name='Earth',
                    showlegend=False,
                    hoverinfo="skip",
                    line=dict(width=2),
                    marker=dict(color='#21f700')))
                                
fig.add_trace(go.Scatter(x=[0,1,2], y=[1.00506,1.22411,1.04874],
                    mode='lines',
                    name='Teegarden',
                    showlegend=False,
                    hoverinfo="skip",
                    line=dict(width=4),
                    marker=dict(color='#aedefc')))
                                
fig.add_trace(go.Scatter(x=[0,1,2], y=[1.09425,0.689663,0.888649],
                    mode='lines',
                    name='Proxima',
                    showlegend=False,
                    hoverinfo="skip",
                    line=dict(width=4),
                    marker=dict(color='#f9a1bc')))
                                
fig.add_trace(go.Scatter(x=[0,1,2], y=[0.685223,1.196561,1.026146],
                    mode='lines',
                    name='Trappist',
                    showlegend=False,
                    hoverinfo="skip",
                    line=dict(width=4),
                    marker=dict(color='#ffaa64'))) 
                                
fig.add_trace(go.Scatter(x=[1,1], y=[0,2],
                    mode='lines',
                    name='Grid1',
                    showlegend=False,
                    hoverinfo="skip",
                    marker=dict(color='white')))
fig.add_trace(go.Scatter(x=[2,2], y=[0,2],
                    mode='lines',
                    name='Grid2',
                    showlegend=False,
                    hoverinfo="skip",
                    marker=dict(color='white')))

fig.add_annotation(text="Created by Matthew Wear. Data provided by the Planetary Habitability Laboratory",
                  xref="paper", yref="paper",
                  font=dict(color='#a8a8a8',size=10),
                  x=-0.06, y=-0.2, showarrow=False) 
                                
fig.update_layout(plot_bgcolor='#313332',paper_bgcolor='#313332',
                  width=800, height=500,
                  dragmode=False,
                  font_color="white",
                  title="What would it feel like to live on an exoplanet, compared to <span style='color:#21f700'>Earth</span>?<br><span style='font-size:12;'>All habitable exoplanets are shown, with <span style='color:#f9a1bc'>Proxima Centauri b</span>, <span style='color:#aedefc'>Teegarden's Star b</span> and <span style='color:#ffaa64'>TRAPPIST-1 d</span> highlighted</span>")

fig.update_xaxes(showline=False, showgrid=False,
                 zeroline=False,
                 ticks='', tickmode='array', tickvals=[0,1,2],
                 ticktext = ['Gravity','Illumination','Temperature'], 
                 tickfont=dict(size=14),
                 range=[0,2.01])

fig.update_yaxes(showline=True, linewidth=2, linecolor='white', showgrid=False,
                 zeroline=False,
                 tickvals=[0.03,1,1.97], range=[0,2], ticktext=['0','1','2'])

config = {
        'displayModeBar': False
}

fig.write_html("Plots/new_parallel.html", include_plotlyjs=False, full_html=False, config=config)

