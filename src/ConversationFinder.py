"""

"""

def get_satisfying_conversations(script):
    """

    :return: A list of lists containing the conversations
    """
    # script = ["Mark","Sally", "Selina", "Sally", "Sally", "Selina", "Sally", "Jeremy", "Sally", "Selina", "Sally", "Selina", "Selina", "Sally"]
    menDict = {"Mark":5,"Jeremy":1}
    femDict = {"Sally":4, "Selina":8, "Bobby":5}
    # script = get_script()
    # menDict = get_men_dict()
    # femDict = get_fem_dict()
    counter = 0
    index = 0
    listConversations = []
    for line in script:
        if line in femDict:
            counter += 1

        if line in menDict:
            if counter >= 6:
                subList = slice(index-counter, index, 1)
                listConversations.append(script[subList])
            counter = 0

        index += 1

        if index == len(script):
            if counter >= 6:
                subList = slice(index - counter, index, 1)
                listConversations.append(script[subList])



    return listConversations

def pass_test2(script):
    return get_satisfying_conversations(script) != []

# print(get_satisfying_conversations())
print(pass_test2())


