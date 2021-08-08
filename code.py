import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
df=pd.read_csv("data.csv")
print(df)

h=df["Height(Inches)"].tolist()
print(h)
mean=statistics.mean(h)
stdD=statistics.stdev(h)
first_std_d_start,first_std_d_end=mean-stdD,mean+stdD
second_std_d_start,second_std_d_end=mean-2*stdD,mean+2*stdD
third_std_d_start,third_std_d_end=mean-3*stdD,mean+3*stdD
fig=ff.create_distplot([h],["index"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_std_d_start,first_std_d_start],y=[0,0.2],mode="lines",name="fds"))
fig.add_trace(go.Scatter(x=[first_std_d_end,first_std_d_end],y=[0,0.2],mode="lines",name="fde"))
fig.add_trace(go.Scatter(x=[second_std_d_start,second_std_d_start],y=[0,0.2],mode="lines",name="sds"))
fig.add_trace(go.Scatter(x=[second_std_d_end,second_std_d_end],y=[0,0.2],mode="lines",name="sde"))
fig.add_trace(go.Scatter(x=[third_std_d_start,third_std_d_start],y=[0,0.2],mode="lines",name="fds"))
fig.add_trace(go.Scatter(x=[third_std_d_end,third_std_d_end],y=[0,0.2],mode="lines",name="fde"))
fig.show()

height_data_within_fstdD=[result for result in h if result>first_std_d_start and result<first_std_d_end]
print(f"percentage of data within first stdD:{len(height_data_within_fstdD)*100/len(h)}%")

height_data_within_sstdD=[result for result in h if result>second_std_d_start and result<second_std_d_end]
print(f"percentage of data within second stdD:{len(height_data_within_sstdD)*100/len(h)}%")

height_data_within_tstdD=[result for result in h if result>third_std_d_start and result<third_std_d_end]
print(f"percentage of data within third stdD:{len(height_data_within_tstdD)*100/len(h)}%")
