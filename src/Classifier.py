
def pass_test3(all_conv, menDict):
    hePronouns = {"he", "him", "his", "himself", "mr.", "sir", "mister"}
    for conv in all_conv:
        counter = 0
        for dialogue in conv:
            words = dialogue.text.split()
            for word in words:
                if word in menDict or word.lower() in hePronouns:
                    counter += 1
        if counter == 0:
            return True
    return False
