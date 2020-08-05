from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
# from bokeh.palettes import Blues8
from bokeh.embed import components
import pandas

# Read in csv
df = pandas.read_csv('crime.csv')

# Create ColumnDataSource from data frame
source = ColumnDataSource(df)

output_file('index.html')

# crime list
crime_list = source.data

# Add plot
p = figure(
    x_range=sorted(set(df['OFFENSE_CODE'])),
    plot_width=800,
    plot_height=600,
    title='Data Visualization of Crime Report',
    x_axis_label='Day of the week',
    y_axis_label='Offense Code',
    tools="pan,box_select,zoom_in,zoom_out,save,reset"
)
p.circle(df["OFFENSE_CODE"],df["DAY_OF_WEEK"],size=10,color="red",alpha=0.5,)

# Render glyph
# p.hbar(
#     y='OFFENSE_CODE',
#     right='Day of the Week',
#     left='Offense Code',
#     height=0.4,
#     # fill_color=factor_cmap(
#     #   'crime',
#     #   palette=Blues8,
#     #   factors=crime_list
#     # ),
#     # fill_alpha=0.9,
#     source=source,
#     legend_group='OFFENSE_CODE'
# )

# # Add Legend
# p.legend.orientation = 'vertical'
# p.legend.location = 'top_right'

# Add Tooltips
hover = HoverTool()
hover.tooltips = """
  <div>
    <h3>@INCIDENT_NUMBER</h3>
    <div><strong>Offense Group: </strong>@OFFENSE_CODE_GROUP</div>
  
  </div>
"""
p.add_tools(hover)

# Show results
show(p)

# Save file
# save(p)

# Print out div and script
# script, div = components(p)
# print(div)
# print(script)