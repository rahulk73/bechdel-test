
def get_satisfying_conversations(script, menDict, femDict):
    """

    :return: A list of lists containing the conversations
    """
    counter = 0
    index = 0
    listConversations = []
    for line in script:
        if line.name in femDict:
            counter += 1

        if line.name in menDict:
            if counter >= 6:
                subList = slice(index-counter, index, 1)
                listConversations.append(script[subList])
            counter = 0

        index += 1

        if index == len(script):
            if counter >= 6:
                subList = slice(index - counter, index, 1)
                listConversations.append(script[subList])

    for conversation in listConversations:
        if len(conversation) >= 20:
            list1 = slice(0, int(len(conversation)/2), 1)
            list2 = slice(int(len(conversation)/2) , len(conversation), 1)
            listConversations.remove(conversation)
            listConversations.append(conversation[list1])
            listConversations.append(conversation[list2])

    return listConversations


def pass_test1(femDict):
    counter = 0
    for girl in femDict:
        if femDict[girl] >= 10:
            counter += 1
    return counter >= 2

def pass_test2(script, menDict, femDict):
    return get_satisfying_conversations(script, menDict, femDict) != []




