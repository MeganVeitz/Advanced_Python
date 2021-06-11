# Playing with args vs kwargs

def keywordfunction(**kwargs):
#    for key, value in kwargs.items():
#        print("The key is: {} the value is: {}".format(key, value))
    a_list = func1(**kwargs)
    #print(a_list)
    return a_list


def func1(**kwargs):
    awesome_list = []
    for key, value in kwargs.items():
        if 'awesome' in value.lower():
            awesome_list.append((key, value))
    #print(awesome_list)
    return awesome_list


print(keywordfunction(meg="is awesome!", A_87="megs patience", awesome="not as good", good="This is awesome!"))
print("call to: ")
print(keywordfunction(dave="captain awesome sauce"))

