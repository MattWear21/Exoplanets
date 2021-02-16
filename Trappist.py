#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 18:54:58 2020

@author: mattwear
"""

###Trappist Polar Plot

trappist = phl_df[phl_df['S_NAME'] == 'TRAPPIST-1'].copy()
theta = np.linspace(0, 360, trappist.shape[0])
np.random.shuffle(theta)
trappist['theta'] = theta

trappist['P_GRAVITY_EST'] = ((G * Me * trappist['P_MASS_EST'])/((Re * trappist['P_RADIUS_EST'])**2))/9.8

hab = trappist[trappist['P_HABITABLE']==1]
unhab = trappist[trappist['P_HABITABLE']==0]

def get_text(df): 
    hab_text = []
    for i in df.index:
        text = '<b>' + df['P_NAME'][i] + '</b><br>'+'Equilibrium Temperature: ' + str((df['P_TEMP_EQUIL'][i]/255).round(3)) + '<br>'+ 'Gravity: ' + str(df['P_GRAVITY_EST'][i].round(3))+ '<br>' + 'Radius: ' + str(df['P_RADIUS_EST'][i].round(3)) + '<br>'+'ESI: '+str(df['P_ESI'][i].round(3))+'<br>'
        hab_text.append(text)
        
    return hab_text

hab_text = get_text(hab)
unhab_text = get_text(unhab)
    

fig = go.Figure()

#Habitable Zone highlight
hab_zone_min = trappist['S_HZ_OPT_MIN'][3806]
hab_zone_max = trappist['S_HZ_OPT_MAX'][3806]

fig.add_trace(go.Scatter(x=[hab_zone_min,hab_zone_min,hab_zone_max,hab_zone_max], y=[0,2,2,0],
                    fill='toself', fillcolor = 'rgba(09, 237, 28, 0.2)',
                    hoveron='fills',
                    line_color='rgba(9, 237, 28, 0.2)',
                    text="Habitable Zone",
                    hoverinfo='text+x+y',
                    mode='lines',
                    showlegend=False))

#Habitable Planets
fig.add_trace(go.Scatter(x=hab.P_DISTANCE, 
                              y=[0.5,0.5,0.5,0.5], 
                              mode='markers',
                              name='Habitable',
                              marker_color='#3ec1d3',
                              marker_size=list(np.floor(hab.P_RADIUS*40).astype(int)),
                              marker_opacity=1,
                              marker_line_color='#3ec1d3',
                              showlegend=False,
                              text=hab_text,
                              hovertemplate = "%{text}"+"<extra></extra>"
                              ))

#Not Habitable Planets
fig.add_trace(go.Scatter(x=unhab.P_DISTANCE, 
                              y=[0.5,0.5,0.5], 
                              mode='markers',
                              name="Uninhabitable",
                              marker_color='#ff165d',
                              marker_line_color='#ff165d',
                              marker_size=list(np.floor(unhab.P_RADIUS*40).astype(int)),
                              marker_opacity=1,
                              showlegend=False,
                              text=unhab_text,
                              hovertemplate = "%{text}"+"<extra></extra>"
                              ))

fig.add_annotation(text="Planetary data is relative to Earth. Created by Matthew Wear. Data provided by the Planetary Habitability Laboratory",
                  xref="paper", yref="paper",
                  font=dict(color='#a8a8a8',size=10),
                  x=-0.06, y=-0.6, showarrow=False) 
                  
fig.update_yaxes(range=[0, 1], showgrid=False, mirror=True, showline=True,
                 linecolor='#a8a8a8',
                 showticklabels=False, ticks='') 
fig.update_xaxes(showgrid=False, title='Distance from TRAPPIST-1 (AU)',
                 mirror=True, showline=True, linecolor='#a8a8a8',
                 color='#a8a8a8',title_font=dict(color='white'))                          

fig.update_layout(dragmode=False, width=800, height=300, 
                  plot_bgcolor='#313332', paper_bgcolor='#313332',
                  font_color="white",
                  title_font_size=22,
                  title="The TRAPPIST-1 Solar System<br><span style='font-size:13;'>This system holds 4 <span style='color:#3ec1d3'>habitable planets</span>, lying within the <span style='color:rgba(9, 237, 28, 0.5)'>habitable zone</span>, and 3 <span style='color:#ff165d'>uninhabitable planets</span></span>")
        
config = {
        'displayModeBar': False
}

fig.write_html("Plots/trappist.html", include_plotlyjs=False, full_html=False, config=config)