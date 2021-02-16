#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 18:44:22 2020

@author: mattwear
"""

###Trappist-1 Illumination vs Gravity

#Assume creation of trappist df

trappist['P_GRAVITY_EST'] = ((G * Me * trappist['P_MASS_EST'])/((Re * trappist['P_RADIUS_EST'])**2))/9.8
trappist['P_SHORT_NAME'] = ['b','c','d','e','f','g','h']
hab = trappist[trappist['P_HABITABLE']==1]
unhab = trappist[trappist['P_HABITABLE']==0]


fig = go.Figure()

fig.add_trace(go.Scatter(x=[1, 1], y=[0.3, 1], mode='lines', showlegend=False,
                         hoverinfo="skip",
                         line=dict(color='#21f700', dash='dash', width=1)))
                                   
fig.add_trace(go.Scatter(x=[0, 1], y=[1, 1], mode='lines', showlegend=False,
                         hoverinfo="skip",
                         line=dict(color='#21f700', dash='dash', width=1)))  

fig.add_trace(go.Scatter(x=hab.P_FLUX, 
                              y=hab.P_GRAVITY_EST, 
                              mode='markers+text',
                              name='Habitable',
                              marker_color='#3ec1d3',
                              marker_size=40,
                              marker_opacity=1,
                              showlegend=True,
                              hoverinfo='skip',
                              text=hab.P_SHORT_NAME
                              #hovertemplate = "<b>TRAPPIST-1 %{text}</b><br>"+"Illumination: %{x:.2f}<br>"+"Gravity: %{y:.2f}<br>"+"<extra></extra>"
                              ))

fig.add_trace(go.Scatter(x=unhab.P_FLUX, 
                              y=unhab.P_GRAVITY_EST, 
                              mode='markers+text',
                              name='Uninhabitable',
                              marker_color='#ff165d',
                              marker_size=40,
                              marker_opacity=1,
                              showlegend=True,
                              hoverinfo='skip',
                              text=unhab.P_SHORT_NAME
                              #hovertemplate = "<b>TRAPPIST-1 %{text}</b><br>"+"Illumination: %{x:.2f}<br>"+"Gravity: %{y:.2f}<br>"+"<extra></extra>"
                              ))

fig.add_trace(go.Scatter(x=[1], y=[1],
                         mode='markers+text',
                         marker_color='#21f700',
                         marker_size=40,
                         marker_opacity=1,
                         showlegend=False,
                         name="Earth",
                         text='Earth',
                         hoverinfo='none'
                         #hovertemplate = "<b>Earth</b><br>"+"Illumination: %{x:.2f}<br>"+"Gravity: %{y:.2f}<br>"+"<extra></extra>"
                         ))
                                 

fig.update_layout(plot_bgcolor='#313332', paper_bgcolor='#313332',
                  font_color="black", width=800, height=500, dragmode=False,
                  title="<span style='color:#ffffff'>Comparison of Surface Gravity and Illumination of TRAPPIST-1 Planets</span>",
                  legend=dict(
                          yanchor="top",
                          y=0.99,
                          xanchor="left",
                          x=0.8,
                          font_color='white',
                          bgcolor="#404040",
                          itemclick=False
                  ))

fig.update_yaxes(title='Gravity (relative to Earth)',
                 color='#a8a8a8',title_font=dict(color='white'),linecolor='#a8a8a8',
                 showgrid=False, range=[0.5,1.4]) 
fig.update_xaxes(title='Illumination from Host Star (relative to Sun/Earth)',
                 color='#a8a8a8',title_font=dict(color='white'),linecolor='#a8a8a8',
                 showgrid=False, range=[0,5])  

config = {
        'displayModeBar': False
}

fig.write_html("Plots/fluxgravity.html", include_plotlyjs=False, full_html=False, config=config)