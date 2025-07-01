'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    social_status=""
    if from_member not in social_graph or to_member not in social_graph:
        social_status="no relationship"
    elif to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        social_status ="friends"
    elif to_member in social_graph[from_member]["following"] and from_member not in social_graph[to_member]["following"]:
        social_status ="follower"
    elif to_member not in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        social_status ="followed by"
    else:
        social_status ="no relationship"
    return social_status


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.


#thoughts make sure the row diagonal and column has the same thing and its not ''
    for i in range(len(board)):
        row = board[i]
        if len(set(row)) == 1 and row[0]!= '':
            return row[0]
    for i in range(len(board)):
        if board[0][i]!= '' and all(board[j][i] ==board[0][i] for j in range(len(board))):
            return board[0][i]
    for i in range(len(board)):
        if board[0][0]!='' and all(board[j][j]==board[0][0] for j in range(len(board))):
            return board[0][0]
    for i in range(len(board)):
        if board[len(board)-1][0]!='' and all(board[len(board)-1][0]==board[len(board)-1-j][j] for j in range(len(board))):
            return board[len(board)-1][0]
    return "NO WINNER"
            

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    #if the stops are not in the route_map then "N/a"
    """ else: routemap[f"{first stop}, {second stop}"]["travel_time_mins"]"""
    first_stop = first_stop.lower()
    second_stop = second_stop.lower() 
    time_total=0
    current=first_stop
    while current!=second_stop:
        for (first, end_stop), leg in route_map.items():
            if first == current:
                time_total += leg["travel_time_mins"]
                current = end_stop
                break
    return time_total