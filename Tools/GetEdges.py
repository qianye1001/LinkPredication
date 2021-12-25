def GetEdges(path, num=-1):
    with open(path, 'r', encoding='utf8') as f:
        lines = f.readlines(num)
        edges = []
        for x in lines:
            start_node = int(x.strip('\n').split(" ")[0])
            end_node = int(x.strip('\n').split(" ")[1])
            edges.append((start_node, end_node))
    return edges


