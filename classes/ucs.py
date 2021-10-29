from queue import PriorityQueue


class UcsTraverser:

    def ucs(problem):
        frontier = PriorityQueue()
        fringe = []
        path = []
        visited = set([])
        priority = 0
        dict = {}
        start_node = problem.getStartState()

        if problem.isGoalState(start_node):
            return 'We have reached destination'
        else:
            frontier.push((start_node, path), priority)
            dict[start_node] = 0
            visited.add(start_node)

            while frontier:
                curr, path = frontier.pop()

                if problem.isGoalState(curr):
                    return path
                else:
                    next = problem.getSuccessors(curr)

                    for node in frontier.heap:
                        fringe.append(node[0])
                    for states in next:
                        if states[0] not in (key for key in dict):
                            cost = problem.getCostOfActions(path + [states[1]])
                            frontier.push((states[0], path + [states[1]]), cost)
                            dict[states[0]] = cost
                            visited.add(states[0])

        print()
