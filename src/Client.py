from src.castlist import *
from src.ConversationFinder import *
from src.Classifier import *
from src.piechart import *

castlist = CastList("../Scripts/TheHelp.pdf")
menDict = castlist.get_male()
femDict = castlist.get_female()
PieChart(menDict, femDict)
script = castlist.get_dialogues()
all_conv = get_satisfying_conversations(script, menDict, femDict)
all_conv_sliced = slice_conversation(all_conv)

assert pass_test1(femDict), "Test1: Failed"
assert pass_test2(script, menDict, femDict), "Test2: Failed"
assert pass_test3(all_conv, menDict), "Test3: Failed"


print("YAY!")



