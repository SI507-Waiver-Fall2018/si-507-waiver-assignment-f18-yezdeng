# Name: Yezhi Deng 
# Uniq: yezdeng
# UMID: 43578445

# Imports -- you may add others but do not need to
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import csv


# plotly.__version__


## Code here should involve creation of the bar chart as specified in instructions
## And opening / using the CSV file you created earlier with noun data from tweets
plotly.tools.set_credentials_file(username='yezdeng', api_key='itysRSkfHLiiVj10Rlij')
plotly.tools.set_config_file(world_readable=True,
                             sharing='public')


## Read file 
f = open("noun_data.csv")
f_read = csv.reader(f)

## store nouns and their frequencies into two lists
noun = []
freq = []

for item in f_read:
	freq.append(item[1])
	noun.append(item[0])


## use plot to create bar chart
py.plot({
    "data": [go.Bar(x=noun, y=freq)],
    "layout": go.Layout(title="most used nouns")

})

f.close()