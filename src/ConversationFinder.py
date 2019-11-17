from src.castlist import *

SLICE_MAX_LENGTH = 20
CONV_MIN_LENGTH = 6
NUM_OF_LINES = 10

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
            if counter >= CONV_MIN_LENGTH:
                subList = slice(index-counter, index, 1)
                listConversations.append(script[subList])
            counter = 0

        index += 1

        if index == len(script):
            if counter >= CONV_MIN_LENGTH:
                subList = slice(index - counter, index, 1)
                listConversations.append(script[subList])
    # listConversations = slice_conversation(listConversations)
    return listConversations

def slice_conversation(listConversations):
    for conversation in listConversations:
        if len(conversation) >= SLICE_MAX_LENGTH:
            list1 = slice(int(len(conversation)/2))
            list2 = slice(int(len(conversation)/2) , len(conversation), 1)
            listConversations.remove(conversation)
            listConversations.append(conversation[list1])
            listConversations.append(conversation[list2])

    for conversation in listConversations:
        if len(conversation) >= SLICE_MAX_LENGTH:
            list1 = slice(int(len(conversation)/2))
            list2 = slice(int(len(conversation)/2) , len(conversation), 1)
            listConversations.remove(conversation)
            listConversations.append(conversation[list1])
            listConversations.append(conversation[list2])

    return listConversations


def pass_test1(femDict):
    counter = 0
    for girl in femDict:
        if femDict[girl] >= NUM_OF_LINES:
            counter += 1
    return counter >= 2

def pass_test2(script, menDict, femDict):
    return get_satisfying_conversations(script, menDict, femDict) != []




