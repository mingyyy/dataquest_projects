# tree = [1,[2,[3,[4,5]]]]
tree = [1, [None, [2,[3, None]]]]
# tree = [1]

def branch(root):
    origin = root[0]
    level, left, right = 1, None, None
    print(f'level {level}: {origin}')
    try:
        level += 1
        left = root[1][0]
        right = root[1][1]
    except:
        pass
    print(f'level {level}: /{left}/  /{right}/')
    return left, right

branch(tree)