import plotly.figure_factory as ff

import pandas as pd


#data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gantt_example.csv')

#colors for legend
color = dict (A = 'rgb(46, 137, 205)',
              B = 'rgb(114, 44, 121)',
              C = 'rgb(198, 47, 105)')

#create chart with basic formatting
fig = ff.create_gantt(df, colors = color, index_col = 'Resource', 
                      show_colorbar = True, bar_width = 0.4, showgrid_x = True, showgrid_y = True, 
                      title = 'Example Chart With Data From Plotly'   
                      )



#Add legend title
fig.update_layout(legend_title_text = "Status:<br>(A=Complete<br>B=In progress<br>C=Not Started")

#create buttons/ pull down menu
button_layer_1_height = 1.08
fig.update_layout(
    updatemenus=[
        dict(
            active = 0,
            buttons = list([
                dict(label = "Legend: On",
                    args = ["showlegend", True],
                    method = "restyle"
                ),
                dict(label = "Legend: Off",
                    args = ["showlegend", False],
                    method = "restyle"
                )
            ]),
            direction = "down",
            pad = {"r":10, "t":10},
            showactive = True,
            x = 1,
            xanchor = "left",
            y = 1.18,
            yanchor = "top"
        ),
    ]
)

#add any annotations for button/dropdown and format hovertext
fig.update_layout(
    #annotations=[
        #dict(text="Show<br>Legend?", x=1, xref="paper", y=0.95, yref="paper", align="left", showarrow= False)
    #],
    hoverlabel = dict(
                      bgcolor = "white", #background color
                      font_size = 16,
                      font_family = "Rockwell",
                      bordercolor = 'black', #font color
                      align = 'right'
    ),
    #hovermode = 'y',
    )

#determine locations for any permanent labels (can also use code to find middle date)
LabelDateA = '2009-02-01'
LabelDateB = '2009-03-20'
LabelDateC = '2009-04-01'
LabelDateD = '2009-04-01'
LabelDateE = '2009-04-01'


#add permanent labels
annots = [dict(x = LabelDateA, y = 0, align = "center", text = "Jean", showarrow = False, font = dict(color = 'white')),
          dict(x = LabelDateB, y = 1, align = "center", text = "Henry", showarrow = False, font = dict(color = 'white')),
          dict(x = LabelDateC, y = 2, align = "center", text = "Toby", showarrow = False, font = dict(color = 'white')),
          dict(x = LabelDateD, y = 3, align = "center", text = "Maren", showarrow = False, font = dict(color = 'white')),
          dict(x = LabelDateE, y = 4, align = "center", text = "Da", showarrow = False, font = dict(color = 'white'))]

fig['layout']['annotations'] = annots

#add today line (need to research if we can tie this to a date/time somehow so it will move with time)
fig.update_layout(shapes = [
    dict(
        type = 'line',
        yref = 'paper', y0 = 0, y1 = 1,
        xref = 'x', x0 = '2009-04-01', x1 = '2009-04-01',
        name = "today"
        ),
    dict(
        type = 'rect',
        yref = 'paper', y0 = 'Job A', y1 = 'JobA',
        xref = 'x', x0 = '2009-01-01', x1 = '2009-01-01',
    )
])

#add milestones using shape

fig.show()