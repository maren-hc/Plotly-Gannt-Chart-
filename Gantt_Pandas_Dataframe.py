import plotly.figure_factory as ff

import pandas as pd

from datetime import date



#data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gantt_example.csv')

#colors for legend
color = dict (A = 'rgb(46, 137, 205)',
              B = 'rgb(114, 44, 121)',
              C = 'rgb(198, 47, 105)')

#create chart with basic formatting
fig = ff.create_gantt(df, colors = color, index_col = 'Resource', 
                      show_colorbar = True, bar_width = 0.4, showgrid_x = True, showgrid_y = True, 
                      title = 'Example Chart With Data From Plotly',
                      show_hover_fill = True
                      )



#Add legend title
fig.update_layout(legend_title_text = 'Status:<br>(A=Complete<br>B=In progress<br>C=Not Started')

#create buttons/ pull down menu
button_layer_1_height = 1.08
fig.update_layout(
    updatemenus = [
        dict(
            active = 0,
            buttons = list([
                dict(label = 'Legend: On',
                    args = ['showlegend', True],
                    method = 'restyle'
                ),
                dict(label = 'Legend: Off',
                    args = ['showlegend', False],
                    method = 'restyle'
                )
            ]),
            direction = 'down',
            pad = dict({'r' : 10, 't' : 10}),
            showactive = True,
            x = 1,
            xanchor = 'left',
            y = 1.18,
            yanchor = 'top'
        ),
    ]
)

#format hovertext
fig.update_layout(
    hoverlabel = dict(
                      bgcolor = 'white', #background color
                      font_size = 16,
                      font_family = 'Rockwell',
                      bordercolor = 'black', #font color
                      align = 'right'
    ),
    hovermode = 'closest'
    )

#add today line 
today = date.today()
fig.update_layout(shapes = [
    dict(
        type = 'line',
        yref = 'paper', y0 = 0, y1 = 1,
        xref = 'x', x0 = today, x1 = today,
        name = 'today'
    ),
#add milestones using shape, somehow anchor to the data
    dict(
        type = 'rect',
        yref = 'paper', y0 = 0.20, y1 = 0.25,
        xref = 'x', x0 = '2009-02-26', x1 = '2009-03-01',
        fillcolor = 'black',
        name = 'due date'
    )
])
#determine locations for any permanent labels (can also use code to find middle date)
LabelDateA = '2009-02-01'
LabelDateB = '2009-03-20'
LabelDateC = '2009-04-01'
LabelDateD = '2009-04-01'
LabelDateE = '2009-04-01'


#add permanent labels
annots = [dict(x = LabelDateA, y = 0, align = 'center', text = 'Jean', showarrow = False, font = dict(color = 'white')),
          dict(x = LabelDateB, y = 1, align = 'center', text = 'Henry', showarrow = False, font = dict(color = 'white')),
          dict(x = LabelDateC, y = 2, align = 'center', text = 'Toby', showarrow = False, font = dict(color = 'white')),
          dict(x = LabelDateD, y = 3, align = 'center', text = 'Maren', showarrow = False, font = dict(color = 'white')),
          dict(x = LabelDateE, y = 4, align = 'center', text = 'Da', showarrow = False, font = dict(color = 'white')),
#add label to today line
          dict(showarrow = False, bordercolor = 'black', borderwidth = 2, bgcolor = 'white', opacity = 1, text = 'Today', align = 'left', x = today,
               xanchor = 'center', y = 4, yanchor = 'top', font = dict(color = 'black'))
          ]

fig.update_layout(annotations= annots)
    
#add and remove modebar buttons and plotly logo by using fig.show(config = ), can also use any of the other config options
fig.show(config = dict({
    'scrollZoom' : True,
    'displaylogo' : False,
    'displayModeBar' : True,
    'modeBarButtonsToRemove' : ['toggleSpikelines', 'lasso2d', 'resetScale2d']}))
