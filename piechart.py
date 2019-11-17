import plotly.graph_objects as go
from plotly.subplots import make_subplots

class Charac :
	
	def __init__(self, name, index) :
		self.name = name
		self.index = index

Bob = Charac("Bob", 100)
George = Charac("George", 5)
Simon = Charac("Simon", 1)
Pablo = Charac("Pablo", 20)
Peter = Charac("Peter", 50)
Liz = Charac("Liz", 10)
Jeanne = Charac("Jeanne", 30)
Mary = Charac("Mary", 5)

men_protagonists = { Bob, George, Simon, Pablo, Peter}
women_protagonists = {Liz,Jeanne, Mary}

def number_line (dictionary) :
	num = 0	
	for x in dictionary:
		num = num + x.index
	return num	

num_line_men = number_line(men_protagonists)

num_line_women = number_line(women_protagonists)

gender = ['Men','Women']
num_prota = [len(men_protagonists), len(women_protagonists)]
num_lines = [num_line_men, num_line_women]

fig = make_subplots (rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]], subplot_titles=['Characters of each gender','Number of lines for each gender'])
fig.add_trace(go.Pie(labels=gender, values=num_prota, name="Number of "), 1, 1)

fig.add_trace(go.Pie(labels=gender,values=num_lines, name = "Number of lines for "), 1, 2)

fig.update_layout(title_text="Results of Bechdel test for this movie")

fig.show()
