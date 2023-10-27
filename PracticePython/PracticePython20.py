def get_number(li, s):
    for i in li:
        if s in li:
            return True
        else:
            return False
        

c = get_number([1,5,9,15,25,47, 360], 3)
print(c)


def get_number_binary(li, s):
    if s < li[(len(li)/2)]:
        