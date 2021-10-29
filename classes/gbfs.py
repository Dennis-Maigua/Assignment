from queue import PriorityQueue


class GBfsTraverser:

    # Constructor
    def __init__(self):
        self.visited = []
        self.end_search = False

    # Function For Implementing Best First Search
    # Gives output path having lowest cost

    def gbfs(self, graph, source, target):
        queue = [source]
        pq = PriorityQueue()
        pq.put((0, source))
        self.visited.append(source)

        while not pq.empty():
            u = pq.get()[1]
            # Dequeue a vertex from
            s = queue.pop(0)

            for i in list(graph[u]):
                if i not in self.visited:
                    print("Command; Drive to ", i, " Parking Lot", end="\n")
                if i is target:
                    print("We have reached ", i, " the final destination")
                    self.visited.append(i)
                    self.end_search = True
                    break
                else:
                    # print("Here",self.end_search)
                    queue.append(i)
                    # visited[i] = True
                    self.visited.append(i)
