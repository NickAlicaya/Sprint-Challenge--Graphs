class Queue():
    def __init__(self):
        self.queue = []
    # adds to back    
    def enqueue(self, value):
        self.queue.append(value)
    # removes from front    
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    #adds to tail    
    def push(self, value):
        self.stack.append(value)
    #removes from tail    
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

        

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist')    

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        qq = Queue()
        # add starting_vertex to Queue, note enqueue adds to the tail
        qq.enqueue(starting_vertex)
        # print({starting_vertex})
        # keep track of visited nodes
        visited = set()

        # repeat until queue is empty
        while qq.size() > 0:

            # dequeue first vert(remember dequeue pops the head)
            v = qq.dequeue()

            # if its not visited
            if v not in visited:
                print(v)
                # then adds or marks it as visited
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    qq.enqueue(next_vert)
                    # print({next_vert})


    def dft(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # s = Stack()
        print(starting_vertex)

        if visited is None:
            visited = set()

        visited.add(starting_vertex)

        for child in self.vertices[starting_vertex]:
            if child not in visited:
                self.dft_recursive(child, visited)    

  
    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # checks if visited is None then initiates as empty set()
        if visited is None:
            visited = set()

        print(starting_vertex)    

        # track visited nodes
        visited.add(starting_vertex)

        #call the function recursively
        for child in self.get_neighbors(starting_vertex):
            if child not in visited:
                self.dft_recursive(child, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()
        # enqueue A PATH TO the starting vertex ID
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            cur_path = q.dequeue()
            print('CURRENT_PATH_XXXXXXX',cur_path)
            # Grab the last vertex from the PATH
            cur_path_last_vertex = cur_path[-1]
            # CHECK IF IT'S THE TARGET
            if cur_path_last_vertex == destination_vertex:
                # IF SO, RETURN PATH
                return cur_path

            # If that vertex has not been visited...
            if cur_path_last_vertex not in visited:
                    
           
                # Mark it as visited...
                visited.add(cur_path_last_vertex)

                # Then add A PATH TO its neighbors to the back of the queue
                for n in self.get_neighbors(cur_path_last_vertex):
                    # _COPY_ THE PATH
                    new_path = list(cur_path) 
                    # APPEND THE NEIGHOR 
                    new_path.append(n)
                    # add the new path
                    q.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            path = s.pop()
            # if last item in list of path not in visited
            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path

                visited.add(path[-1])

            for child in self.get_neighbors(path[-1]):
                # makes a copy of path
                new_path = list(path)
                # adds child to list
                new_path.append(child)
                # add to stack to keep while loop going
                s.push(new_path)        

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if path is None:
            path = []
        
        visited.add(starting_vertex)
        # makes a copy of path
        new_path = path+[starting_vertex]

        if starting_vertex == destination_vertex:
            return new_path

        for child in self.get_neighbors(starting_vertex):
            if child not in visited:
                child_path = self.dfs_recursive(child, destination_vertex, visited, new_path)
                if child_path:
                    return child_path    

        return None