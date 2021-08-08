import random
import statistics
randomRolls=[]
import plotly.figure_factory as ff
import plotly.graph_objects as go
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    sum=dice1+dice2
    randomRolls.append(sum)

print(randomRolls)
mean=statistics.mean(randomRolls)
stdD=statistics.stdev(randomRolls)
firstStdDStart,firstStdDEnd=mean-stdD,mean+stdD
secondStdDStart,secondStdDEnd=mean-2*stdD,mean+2*stdD
thirdStdDStart,thirdStdDEnd=mean-3*stdD,mean+3*stdD
fig=ff.create_distplot([randomRolls],["Results"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.14],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[firstStdDStart,firstStdDStart],y=[0,0.14],mode="lines",name="fds"))
fig.add_trace(go.Scatter(x=[firstStdDEnd,firstStdDEnd],y=[0,0.14],mode="lines",name="fde"))
fig.add_trace(go.Scatter(x=[secondStdDStart,secondStdDStart],y=[0,0.14],mode="lines",name="sds"))
fig.add_trace(go.Scatter(x=[secondStdDEnd,secondStdDEnd],y=[0,0.14],mode="lines",name="sde"))
fig.add_trace(go.Scatter(x=[thirdStdDStart,thirdStdDStart],y=[0,0.14],mode="lines",name="tds"))
fig.add_trace(go.Scatter(x=[thirdStdDEnd,thirdStdDEnd],y=[0,0.14],mode="lines",name="tde"))
fig.show()
print(mean)
print(stdD)