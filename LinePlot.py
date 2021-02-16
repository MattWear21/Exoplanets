#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 11:58:49 2020

@author: mattwear
"""

###Line plot of total exoplanets discovered

#nasa_df = pd.read_csv("Data/nasa_archive.csv", skiprows=126)
phl_df = pd.read_csv("Data/phl_exoplanet_catalog.csv")


#Bar chart of number of exoplanets discovered against year
#Maybe change to cumulative graph or line graph
bar_df = pd.DataFrame(phl_df['P_YEAR'].value_counts())
#Set the missing years 
bar_df.loc[1990, 'P_YEAR'] = 0
bar_df.loc[1991, 'P_YEAR'] = 0
bar_df.loc[1993, 'P_YEAR'] = 0
bar_df.sort_index(inplace=True)

bar_df['CumulativeTotalExoplanets'] = bar_df['P_YEAR'].cumsum()


#Habitable exoplanets
hab_df = phl_df[phl_df['P_HABITABLE'] >= 1]
hab_value_counts = pd.DataFrame(hab_df['P_YEAR'].value_counts())
years = list(range(1989, 2011))
years.append(2012)

for y in years:
    hab_value_counts.loc[y, 'P_YEAR'] = 0
hab_value_counts.sort_index(inplace=True)

bar_df['CumulativeTotalHabitableExoplanets'] = hab_value_counts['P_YEAR'].cumsum()


#Plot
hab_colour = '#3ec1d3'
background = '#313332'

fig = go.Figure()

fig.add_trace(go.Scatter(x=[2009.25, 2009.25], y=[0, 4050], mode='lines', showlegend=False,
                         hoverinfo="skip",
                         line=dict(color='#a8a8a8', 
                              dash='dash')))

fig.add_annotation(x=2008.7, y=2600,
            text="Kepler Space Telescope is Launched",
            showarrow=False,
            textangle=270,
            font=dict(
                    size=11,
                    color="#a8a8a8"
            ))

fig.add_trace(go.Scatter(x=np.array(bar_df.index), y=bar_df['CumulativeTotalExoplanets'],
                    mode='lines+markers',
                    name='Total',
                    showlegend=False,
                    marker=dict(color='#ff9a00')))
fig.add_trace(go.Scatter(x=np.array(bar_df.index), y=bar_df['CumulativeTotalHabitableExoplanets'],
                    mode='lines+markers',
                    name='Habitable',
                    showlegend=False,
                    marker=dict(color=hab_colour)))

fig.update_layout(xaxis_title='Year', yaxis_title='Cumulative Total of Exoplanets Discovered',
                  hovermode="x unified", dragmode=False,
                  title="Time Series of <span style='color:#ff9a00'>Total</span> and <span style='color:#3ec1d3'>Habitable</span> Exoplanets Discovered",
                  plot_bgcolor=background,
                  paper_bgcolor=background,
                  #font_family="Courier New",
                  font_color="white",
                  #title_font_family="Times New Roman",
                  #title_font_color="white",
                  title_font_size=16,
                  width=800,
                  height=500,
                  hoverlabel=dict(bgcolor="white", font_color='black'),
                  legend=dict(
                          orientation="h",
                          yanchor="bottom",
                          y=1.02,
                          xanchor="right",
                          x=1))

fig.add_annotation(text="Created by Matthew Wear. Data provided by the Planetary Habitability Laboratory.",
                  xref="paper", yref="paper",
                  font=dict(size=10, color='#a8a8a8'),
                  x=-0.1, y=-0.25, showarrow=False)                     

fig.update_xaxes(showgrid=False, linecolor='#a8a8a8', spikecolor="#a8a8a8",
                 color='#a8a8a8',title_font=dict(color='white'))
fig.update_yaxes(showgrid=False, linecolor='#a8a8a8', zerolinecolor = '#404040',
                 color='#a8a8a8',title_font=dict(color='white'))

config = {
        'displayModeBar': False
}

fig.write_html("Plots/lineplot.html", include_plotlyjs=False, full_html=False, config=config)
























