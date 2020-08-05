from bokeh.plotting import figure, output_file, show
import pandas


df = pandas.read_csv("crime.csv")

# label =  sorted(set(df['OFFENSE_CODE']))

p = figure(x_range=list(df['OFFENSE_CODE'],title="Crime Report Observation",plot_width=800, plot_height=800, x_axis_label='Day of the Week', y_axis_label='Offense Code')

# p.circle(df["OFFENSE_CODE"],df["DAY_OF_WEEK"],size=10,color="red",alpha=0.5,)

show(p)