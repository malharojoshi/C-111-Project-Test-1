import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

#plotting the graph
fig = ff.create_distplot([data],["reading_time"], show_hist= False)
fig.show()

#calculating the mean and standard deviation of the population data
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("mean of popultion:- ",mean)
print("Standard deviation of popultion:- ",std_deviation)



def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean



mean_list = []
for i in range(0,100):
    set_of_means= random_set_of_mean(30)
    mean_list.append(set_of_means)


fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN"))
fig.show()
z_score = (mean - set_of_means)/std_deviation
print("The z score is = ",z_score)
