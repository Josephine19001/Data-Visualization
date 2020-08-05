from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
x= [1,2,3,4,5]
y =  [4,6,3,4,5,]

output_file('test.html')

#Add Plot
p = figure(
  title= "Simple Example",
  x_axis_label= "X Axis",
  y_axis_label= "Y Axis",
)

# Render glyph
p.line(x,y, legend="Test", line_width=2)

#Show results
save(p)