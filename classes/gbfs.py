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
        # print(queue)
        # set of visited nodes
        self.visited.append(source)
        visited = True
        pq = PriorityQueue()
        pq.put((0, source))

        while not pq.empty():
            u = pq.get()[1]
            # Displaying the path having lowest cost
            print(u, end=" ")
            if u == target:
                break

            for v, c in queue:
                if not visited:
                    visited = True
                    pq.put((c, v))

        print()
