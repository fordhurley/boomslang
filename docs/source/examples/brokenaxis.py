plot = BrokenAxisPlot(break_points=(4,8))

bar = Bar()
bar.xValues = range(5)
bar.yValues = [2, 12, 3, 18.5, 13]

plot.add(bar)
plot.xLabel = "Widget ID"
plot.yLabel = "# Widgets Sold"

plot.save("brokenaxis.png")
