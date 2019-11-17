import plotly.graph_objects as go
from plotly.subplots import make_subplots

class PieChart:
	def __init__(self, male, female):
		self.num_line= [sum(male.values()),sum(female.values())]
		self.num_prota = [len(male), len(female)]
		self.gender = ['Men','Women']
		self.fig = make_subplots (rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]], \
		 subplot_titles=['# of characters of each gender','# of lines of each gender'])
		self.fig.add_trace(go.Pie(labels=self.gender, values=self.num_prota, name=r"% of characters"), 1, 1)
		self.fig.add_trace(go.Pie(labels=self.gender,values=self.num_line, name = "Number of lines for "), 1, 2)
		self.fig.update_layout(
			title={
				'text' : "Results of Bechdel test for the movie",
				'x':0.5,
				'y':0.95,
			},
			font=dict(
				family="Courier New, monospace",
				size=15,
				color="#7f7f7f"
			)
		)
		self.fig.show()

if __name__ == '__main__':
	o1=PieChart({'Adam':250,'Steve':350,'Chad':100,'Bob':1},{'Eve':51,'Amy':100})