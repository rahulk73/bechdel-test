from src.castlist import *
from src.ConversationFinder import *
from src.Classifier import *

castlist = CastList("../Scripts/TheHelp.pdf")
menDict = castlist.get_male()
femDict = castlist.get_female()
script = castlist.get_dialogues()

assert pass_test1(femDict) == True

all_conv = get_satisfying_conversations(script, menDict, femDict)

assert pass_test2(script, menDict, femDict) == True

print(all_conv)
print(pass_test3(all_conv, menDict))

print("yay")



