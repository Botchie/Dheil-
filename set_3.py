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

    Please see "set_3_sample_data.py" for sample data. The social graph
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
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def relationship_status(from_member, to_member, social_graph):
        from_follows = social_graph[from_member]["following"]
        to_follows = social_graph[to_member]["following"]

        if to_member in from_follows and from_member in to_follows:
            return "friends"
        elif to_member in from_follows:
            return "follower"
        elif from_member in to_follows:
            return "followed by"
        else:
            return "no relationship"



def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "set_3_sample_data.py" for sample data. The board will adhere
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
    def tic_tac_toe(board):
        size = len(board)

        for row in board:
            if row.count(row[0]) == size and row[0] != "":
                return row[0]

        for column in range(size):
            check_column = []
        for row in range(size):
            check_column.append(board[row][column])
        if check_column.count(check_column[0]) == size and check_column[0] != "":
                return check_column[0]

        main_diagonal = []
        for i in range(size):
            main_diagonal.append(board[i][i])
        if main_diagonal.count(main_diagonal[0]) == size and main_diagonal[0] != "":
            return main_diagonal[0]

        anti_diagonal = []
        for i in range(size):
            anti_diagonal.append(board[i][size -1 - i])
        if anti_diagonal.count(anti_diagonal[0]) == size and anti_diagonal[0] != "":
            return anti_diagonal[0]

        return "NO WINNER"



def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "set_3_sample_data.py" for sample data. The route map will
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
    def eta(first_stop, second_stop, route_map):
        amount_time = 0
        current_stop = first_stop

        while current_stop != second_stop:
            for place in route_map:
                start = place[0]
                end = place[1]
                if start == current_stop:
                    travel_time = route_map[place]["travel_time_mins"]
                    amount_time += travel_time
                    current_stop = end
                    break
        return amount_time
