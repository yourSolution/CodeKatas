def friend(list):
    friendList = []
    for name in list:
        if len(name) == 4:
            friendList.append(name)
    return friendList
