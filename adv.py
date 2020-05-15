from room import Room
from player import Player
from world import World
from util import Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#### CODE START HERE ####



def maze_mapper(world, traversal_path):
    # construct your own traversal graph You start in room 0, which contains exits
    # ['n', 's', 'w', 'e']. Your starting graph should look something like this:

    # create an empty stack
    stack = Stack()

    # initialize current room
    starting_room = 0
    visited = {0: {}}
    reverse = {
        'n': 's',
        's': 'n',
        'e': 'w',
        'w': 'e'
        }

    # Return the direction/s that is available in a visited room
    def available_move(visited, current_room):
        exits = visited[current_room.id]
        
        # n/s/e/w == '?' and the connecting room is not yet visited
        for direction in exits:
            if exits[direction] == '?' and current_room.get_room_in_direction(direction).id not in visited:
                # print('Room directions from available_move', direction)
                return direction
        return None

    # Search for a new room
    def new_room(traversal_path, visited, current_room, stack, reverse):

        while len(visited) < len(room_graph):
            # remove the last item in the stack
            next_move = stack.pop()
            
            # add the recently popped direction to the traversal_path
            traversal_path.append(next_move)

            # get the next room by calling get_room_in_direction from the current room
            next_room = current_room.get_room_in_direction(next_move)

            # checks if it still has any un-explored exits marked by '?'
            if '?' in visited[next_room.id].values():
                return next_room.id

            # set the current_room to the next room
            current_room = next_room

    # while there are still rooms not explored
    while len(visited) < len(room_graph):
        # initiate current_room
        current_room = world.rooms[starting_room]
        
        # checks and adds room to visited and sets direction values to be = '?'
        # ex: 0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
        if current_room not in visited:
            for direction in current_room.get_exits():
                visited[current_room.id][direction] = '?'
                # print('visited[current_room.id]',visited[current_room.id])

 
        next_move = available_move(visited, current_room)
        

        # When you hit a dead-end, ergo a room without an exit that leads to an unexplored room
        # Go back to the nearest room that does contain an exit to an unexplored path.
        # if next move is equal to None then start again from a new room
        if next_move is None:
            # pop off the room and continue to next room
            starting_room = new_room(traversal_path, visited, current_room, stack, reverse)

        else:
            # if it has a next move direction that leads to an unexplored room then append it to traversal_path
            traversal_path.append(next_move)

            # set the next_room from the current_room
            next_room = current_room.get_room_in_direction(next_move)
            # print('NEXT_ROOM:', next_room)

            # if next room is not in visited then mark as visited and values as empty
            if next_room.id not in visited:
                visited[next_room.id] = {}

            # push the reverse direction in the stack
            stack.push(reverse[next_move])
           


            # next loop starting_room will be the next room id
            starting_room = next_room.id
            print('next room will be', starting_room)

maze_mapper(world, traversal_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
