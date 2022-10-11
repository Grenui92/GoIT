import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    result = []
    if isinstance(cats[0], tuple):
        for i in cats:
            obj = {}
            obj['nickname'] = i.nickname
            obj['age'] = i.age
            obj['owner'] = i.owner
            result.append(obj)
        return result
    else:
        for i in cats:
            obj = Cat(i['nickname'], i['age'], i['owner'])
            result.append(obj)
        return result




print(convert_list([Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]))