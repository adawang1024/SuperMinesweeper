

#!/usr/bin/env python3

# import typing
import doctest

# NO ADDITIONAL IMPORTS ALLOWED!


def dump(game):
    """
    Prints a human-readable version of a game (provided as a dictionary)
    """
    for key, val in sorted(game.items()):
        if isinstance(val, list) and val and isinstance(val[0], list):
            print(f"{key}:")
            for inner in val:
                print(f"    {inner}")
        else:
            print(f"{key}:", val)


# 2-D IMPLEMENTATION


def new_game_2d(num_rows, num_cols, bombs):
    """
    Start a new game.

    Return a game state dictionary, with the 'dimensions', 'state', 'board' and
    'hidden' fields adequately initialized.

    Parameters:
       num_rows (int): Number of rows
       num_cols (int): Number of columns
       bombs (list): List of bombs, given in (row, column) pairs, which are
                     tuples

    Returns:
       A game state dictionary

    >>> dump(new_game_2d(2, 4, [(0, 0), (1, 0), (1, 1)]))
    board:
        ['.', 3, 1, 0]
        ['.', '.', 1, 0]
    dimensions: (2, 4)
    hidden:
        [True, True, True, True]
        [True, True, True, True]
    state: ongoing
    """
    dimensions = (num_rows, num_cols)
    return new_game_nd(dimensions, bombs)
    # board = []
    # board_row = [0]*num_cols
    # for row in range(num_rows):
    #     board.append(board_row.copy())

    # hidden = []
    # for r in range(num_rows):
    #     hidden.append([True]*num_cols)
    #     for c in range(num_cols):
    #         if (r,c) in bombs:
    #             board[r][c] = "."

    # for r in range(num_rows):
    #     for c in range(num_cols):
    #         if board[r][c] == 0:
    #             neighbor_bombs = 0
    #             for i in range(max(0, r-1), min(num_rows, r+2)):
    #                 for j in range(max(0, c-1), min(num_cols, c+2)):
    #                     if board[i][j] == ".":
    #                         neighbor_bombs += 1
    #             board[r][c] = neighbor_bombs

    # return {
    #     "dimensions": (num_rows, num_cols),
    #     "board": board,
    #     "hidden": hidden,
    #     "state": "ongoing",
    # }


def dig_2d(game, row, col):
    """
    Reveal the cell at (row, col), and, in some cases, recursively reveal its
    neighboring squares.

    Update game['hidden'] to reveal (row, col).  Then, if (row, col) has no
    adjacent bombs (including diagonally), then recursively reveal (dig up) its
    eight neighbors.  Return an integer indicating how many new squares were
    revealed in total, including neighbors, and neighbors of neighbors, and so
    on.

    The state of the game should be changed to 'defeat' when at least one bomb
    is revealed on the board after digging (i.e. game['hidden'][bomb_location]
    == False), 'victory' when all safe squares (squares that do not contain a
    bomb) and no bombs are revealed, and 'ongoing' otherwise.

    Parameters:
       game (dict): Game state
       row (int): Where to start digging (row)
       col (int): Where to start digging (col)

    Returns:
       int: the number of new squares revealed

    >>> game = {'dimensions': (2, 4),
    ...         'board': [['.', 3, 1, 0],
    ...                   ['.', '.', 1, 0]],
    ...         'hidden': [[True, False, True, True],
    ...                  [True, True, True, True]],
    ...         'state': 'ongoing'}
    >>> dig_2d(game, 0, 3)
    4
    >>> dump(game)
    board:
        ['.', 3, 1, 0]
        ['.', '.', 1, 0]
    dimensions: (2, 4)
    hidden:
        [True, False, False, False]
        [True, True, False, False]
    state: victory

    >>> game = {'dimensions': [2, 4],
    ...         'board': [['.', 3, 1, 0],
    ...                   ['.', '.', 1, 0]],
    ...         'hidden': [[True, False, True, True],
    ...                  [True, True, True, True]],
    ...         'state': 'ongoing'}
    >>> dig_2d(game, 0, 0)
    1
    >>> dump(game)
    board:
        ['.', 3, 1, 0]
        ['.', '.', 1, 0]
    dimensions: [2, 4]
    hidden:
        [False, False, True, True]
        [True, True, True, True]
    state: defeat
    """

    # if game["state"] != "ongoing":
    #     # game["state"] = game["state"]  # keep the state the same
    #     return 0

    # if game["board"][row][col] == ".":
    #     game["hidden"][row][col] = False
    #     game["state"] = "defeat"
    #     return 1

    # if game["hidden"][row][col] != False:
    #     game["hidden"][row][col] = False
    #     revealed = 1
    # else:
    #     return 0

    # if game["board"][row][col] == 0:
    #     num_rows, num_cols = game["dimensions"]
    #     for i in range(max(0,row-1),min(num_rows, row+2)):
    #         for j in range(max(0,col-1),min(num_cols, col+2)):
    #             if game["board"][i][j] != ".":
    #                     if game["hidden"][i][j] == True:
    #                         revealed += dig_2d(game, i, j)

    # hidden_squares = 0
    # for r in range(game["dimensions"][0]):
    #     for c in range(game["dimensions"][1]):
    #         if not (game["board"][r][c] == "."):
    #             if game["hidden"][r][c] == True:
    #                 hidden_squares += 1
    #                 game["state"] = "ongoing"

    # if hidden_squares > 0:
    #     game["state"] = "ongoing"
    #     # return revealed
    # else:
    #     game["state"] = "victory"
    # return revealed
    coordinates = (row, col)
    return dig_nd(game, coordinates)


def render_2d_locations(game, xray=False):
    """
    Prepare a game for display.

    Returns a two-dimensional array (list of lists) of '_' (hidden squares),
    '.' (bombs), ' ' (empty squares), or '1', '2', etc. (squares neighboring
    bombs).  game['hidden'] indicates which squares should be hidden.  If
    xray is True (the default is False), game['hidden'] is ignored and all
    cells are shown.

    Parameters:
       game (dict): Game state
       xray (bool): Whether to reveal all tiles or just the that are not
                    game['hidden']

    Returns:
       A 2D array (list of lists)

    >>> render_2d_locations({'dimensions': (2, 4),
    ...         'state': 'ongoing',
    ...         'board': [['.', 3, 1, 0],
    ...                   ['.', '.', 1, 0]],
    ...         'hidden':  [[True, False, False, True],
    ...                   [True, True, False, True]]}, False)
    [['_', '3', '1', '_'], ['_', '_', '1', '_']]

    >>> render_2d_locations({'dimensions': (2, 4),
    ...         'state': 'ongoing',
    ...         'board': [['.', 3, 1, 0],
    ...                   ['.', '.', 1, 0]],
    ...         'hidden':  [[True, False, True, False],
    ...                   [True, True, True, False]]}, True)
    [['.', '3', '1', ' '], ['.', '.', '1', ' ']]
    """
    # board_row = [" "] * game["dimensions"][1]
    # board_copy = []
    # for _ in range(game["dimensions"][0]):
    #     board_copy.append(board_row.copy())

    # # for row in game["board"]:
    # #     board_copy.append(row[:])

    # # board_copy = game["board"][:]
    # for row in range(game["dimensions"][0]):
    #     for col in range(game["dimensions"][1]):
    #         if not xray and game["hidden"][row][col]:
    #             board_copy[row][col] = "_"
    #         # if game["board"][row][col] == 0:
    #         #     board_copy[row][col] = ' '
    #         elif game["board"][row][col]:
    #             board_copy[row][col] = str(game["board"][row][col])
    # return board_copy
    return render_nd(game, xray)


def render_2d_board(game, xray=False):
    """
    Render a game as ASCII art.

    Returns a string-based representation of argument 'game'.  Each tile of the
    game board should be rendered as in the function
        render_2d_locations(game)

    Parameters:
       game (dict): Game state
       xray (bool): Whether to reveal all tiles or just the ones allowed by
                    game['hidden']

    Returns:
       A string-based representation of game

    >>> render_2d_board({'dimensions': (2, 4),
    ...                  'state': 'ongoing',
    ...                  'board': [['.', 3, 1, 0],
    ...                            ['.', '.', 1, 0]],
    ...                  'hidden':  [[False, False, False, True],
    ...                            [True, True, False, True]]})
    '.31_\\n__1_'

    >>> render_2d_board({'dimensions': (3, 4),
    ...                  'state': 'ongoing',
    ...                  'board': [['.', 3, 1, 0],
    ...                            ['.', 3, 1, 0],
    ...                            ['.', '.', 1, 0]],
    ...                  'hidden':  [[False, False, False, True],
    ...                            [False, False, False, True],
    ...                            [True, True, False, True]]})
    '.31_\\n.31_\\n__1_'
    """
    # render_nd(game, xray=False)
    locations = render_2d_locations(game, xray)
    # [['.', '3', '1', '_'],['_', '_', '1', '_']]
    result = ""
    for row in locations:
        for element in row:
            result += element
        result += "\n"
    return result[:-1]


# N-D IMPLEMENTATION HELPER


def create_array(dimensions, value):
    """
    A function that, given a list of dimensions and a value,
    creates a new N-d array with those dimensions,
    where each value in the array is the given value.

    >>> create_array((2, 4, 2), 0)
    [[[0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0]]]

    """

    if len(dimensions) == 1:
        return [value] * dimensions[0]
    else:
        result = []
        for _ in range(dimensions[0]):
            new_dimension = create_array(dimensions[1:], value)
            result.append(new_dimension)
        return result


def get_value(nd_array, coordinates):
    """
    A function that, given an N-d array and a tuple/list of coordinates,
    returns the value at those coordinates in the array.

    >>> get_value([1,2,3], (2,))
    3
    >>> get_value([[1,2],[3,4]], (1,1))
    4

    """
    if len(coordinates) == 1:
        return nd_array[coordinates[0]]
    else:
        inner_array = nd_array[coordinates[0]]
        return get_value(inner_array, coordinates[1:])


def replace_value(nd_array, coordinates, value):
    """
    A function that, given an N-d array, a tuple/list of coordinates,
    and a value, replaces the value at those coordinates
    in the array with the given value.

    >>> nd_array = [1,2,3]
    >>> replace_value(nd_array,(1,), 0)
    >>> nd_array
    [1, 0, 3]

    >>> nd_array = [[1,2],[3,4]]
    >>> replace_value(nd_array,(1,0), 0)
    >>> nd_array
    [[1, 2], [0, 4]]

    """

    if len(coordinates) == 1:
        nd_array[coordinates[0]] = value
    else:
        replace_value(nd_array[coordinates[0]], coordinates[1:], value)


operation_vectors = {
    "smaller": -1,
    "no change": 0,
    "bigger": 1,
}

operations = ["smaller", "no change", "bigger"]


def neighbors(coordinates, dimensions):
    """
    A function that returns all the neighbors of
    a given set of coordinates in a given game.

    >>> neighbors([0, 0, 0],[2, 2, 2])
    [(0, 0, 0), (0, 0, 1), (0, 1, 0),
    (0, 1, 1), (1, 0, 0), (1, 0, 1),
    (1, 1, 0), (1, 1, 1)]

    """

    all_neighbors = []
    if len(coordinates) == 0:
        return [()]
    else:
        for operation in operations:
            if 0 <= coordinates[0] + operation_vectors[operation] < dimensions[0]:
                for inner_combo in neighbors(coordinates[1:], dimensions[1:]):
                    all_neighbors.append(
                        (coordinates[0] + operation_vectors[operation],) + inner_combo
                    )
        return all_neighbors


def all_possible_coordinates(dimensions):
    """
    Returns all possible coordinates in a given board.
    >>> all_possible_coordinates([3])
    [(0,), (1,), (2,)]
    >>> all_possible_coordinates([2,3])
    [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)]

    """
    if len(dimensions) == 0:
        return [()]
    else:
        result = []
        for i in all_possible_coordinates(dimensions[1:]):
            for j in range(dimensions[0]):
                result.append((j,) + i)
    return result


# N-D IMPLEMENTATION


def new_game_nd(dimensions, bombs):
    """
    Start a new game.

    Return a game state dictionary, with the 'dimensions', 'state', 'board' and
    'hidden' fields adequately initialized.


    Args:
       dimensions (tuple): Dimensions of the board
       bombs (list): Bomb locations as a list of tuples, each an
                     N-dimensional coordinate

    Returns:
       A game state dictionary

    >>> g = new_game_nd((2, 4, 2), [(0, 0, 1), (1, 0, 0), (1, 1, 1)])
    >>> dump(g)
    board:
        [[3, '.'], [3, 3], [1, 1], [0, 0]]
        [['.', 3], [3, '.'], [1, 1], [0, 0]]
    dimensions: (2, 4, 2)
    hidden:
        [[True, True], [True, True], [True, True], [True, True]]
        [[True, True], [True, True], [True, True], [True, True]]
    state: ongoing
    """
    board = create_array(dimensions, 0)

    hidden = create_array(dimensions, True)

    for coordinate in bombs:
        replace_value(board, coordinate, ".")
        for neighbor in neighbors(coordinate, dimensions):
            value = get_value(board, neighbor)
            if not value == ".":
                replace_value(board, neighbor, value + 1)

    return {
        "dimensions": dimensions,
        "board": board,
        "hidden": hidden,
        "state": "ongoing",
    }


def dig_nd(game, coordinates):
    """
    Recursively dig up square at coords and neighboring squares.

    Update the hidden to reveal square at coords; then recursively reveal its
    neighbors, as long as coords does not contain and is not adjacent to a
    bomb.  Return a number indicating how many squares were revealed.  No
    action should be taken and 0 returned if the incoming state of the game
    is not 'ongoing'.

    The updated state is 'defeat' when at least one bomb is revealed on the
    board after digging, 'victory' when all safe squares (squares that do
    not contain a bomb) and no bombs are revealed, and 'ongoing' otherwise.

    Args:
       coordinates (tuple): Where to start digging

    Returns:
       int: number of squares revealed

    >>> g = {'dimensions': (2, 4, 2),
    ...      'board': [[[3, '.'], [3, 3], [1, 1], [0, 0]],
    ...                [['.', 3], [3, '.'], [1, 1], [0, 0]]],
    ...      'hidden': [[[True, True], [True, False], [True, True],
    ...                [True, True]],
    ...               [[True, True], [True, True], [True, True],
    ...                [True, True]]],
    ...      'state': 'ongoing'}
    >>> dig_nd(g, (0, 3, 0))
    8
    >>> dump(g)
    board:
        [[3, '.'], [3, 3], [1, 1], [0, 0]]
        [['.', 3], [3, '.'], [1, 1], [0, 0]]
    dimensions: (2, 4, 2)
    hidden:
        [[True, True], [True, False], [False, False], [False, False]]
        [[True, True], [True, True], [False, False], [False, False]]
    state: ongoing
    >>> g = {'dimensions': (2, 4, 2),
    ...      'board': [[[3, '.'], [3, 3], [1, 1], [0, 0]],
    ...                [['.', 3], [3, '.'], [1, 1], [0, 0]]],
    ...      'hidden': [[[True, True], [True, False], [True, True],
    ...                [True, True]],
    ...               [[True, True], [True, True], [True, True],
    ...                [True, True]]],
    ...      'state': 'ongoing'}
    >>> dig_nd(g, (0, 0, 1))
    1
    >>> dump(g)
    board:
        [[3, '.'], [3, 3], [1, 1], [0, 0]]
        [['.', 3], [3, '.'], [1, 1], [0, 0]]
    dimensions: (2, 4, 2)
    hidden:
        [[True, False], [True, False], [True, True], [True, True]]
        [[True, True], [True, True], [True, True], [True, True]]
    state: defeat
    """

    if game["state"] != "ongoing" or not get_value(game["hidden"], coordinates):
        return 0
    replace_value(game["hidden"], coordinates, False)
    # bomb
    if get_value(game["board"], coordinates) == ".":
        game["state"] = "defeat"
        return 1
    # 0:
    else:
        revealed = reveal_square(game, coordinates)
        # result=1
        # if get_value(game["board"],coordinates) == 0:
        #     all_neighbors = neighbors(coordinates, game["dimensions"])
        #     for neighbor in all_neighbors:
        #         result += dig_nd(game, neighbor)
        if victory_check(game):
            game["state"] = "victory"
        return revealed


def reveal_square(game, coordinates):
    """
    Return the total number of squares revealed once a square is dug

    >>> g = {'dimensions': (2, 4, 2),
    ...      'board': [[[3, '.'], [3, 3], [1, 1], [0, 0]],
    ...                [['.', 3], [3, '.'], [1, 1], [0, 0]]],
    ...      'hidden': [[[True, True], [True, False], [True, True],
    ...                [True, True]],
    ...               [[True, True], [True, True], [True, True],
    ...                [True, True]]],
    ...      'state': 'ongoing'}
    >>> reveal_square(g,(0,0,0))
    1
    """
    result = 1
    if get_value(game["board"], coordinates) == 0:
        all_neighbors = neighbors(coordinates, game["dimensions"])
        for neighbor in all_neighbors:
            if get_value(game["hidden"], neighbor):
                replace_value(game["hidden"], neighbor, False)
                result += reveal_square(game, neighbor)
    return result


def victory_check(game):
    """
    Retunrs True if the game is in a "victory" state False otherwise

    >>> g = {'dimensions': (2, 4, 2),
    ...      'board': [[[3, '.'], [3, 3], [1, 1], [0, 0]],
    ...                [['.', 3], [3, '.'], [1, 1], [0, 0]]],
    ...      'hidden': [[[True, True], [True, False], [True, True],
    ...                [True, True]],
    ...               [[True, True], [True, True], [True, True],
    ...                [True, True]]],
    ...      'state': 'ongoing'}
    >>> victory_check(g)
    False
    """
    hidden_square = 0
    for coordinate in all_possible_coordinates(game["dimensions"]):
        if (
            get_value(game["hidden"], coordinate)
            and get_value(game["board"], coordinate) != "."
        ):
            hidden_square += 1
    if hidden_square > 0:
        return False
    else:
        return True


def render_nd(game, xray=False):
    """
    Prepare the game for display.

    Returns an N-dimensional array (nested lists) of '_' (hidden squares), '.'
    (bombs), ' ' (empty squares), or '1', '2', etc. (squares neighboring
    bombs).  The game['hidden'] array indicates which squares should be
    hidden.  If xray is True (the default is False), the game['hidden'] array
    is ignored and all cells are shown.

    Args:
       xray (bool): Whether to reveal all tiles or just the ones allowed by
                    game['hidden']

    Returns:
       An n-dimensional array of strings (nested lists)

    >>> g = {'dimensions': (2, 4, 2),
    ...      'board': [[[3, '.'], [3, 3], [1, 1], [0, 0]],
    ...                [['.', 3], [3, '.'], [1, 1], [0, 0]]],
    ...      'hidden': [[[True, True], [True, False], [False, False],
    ...                [False, False]],
    ...               [[True, True], [True, True], [False, False],
    ...                [False, False]]],
    ...      'state': 'ongoing'}
    >>> render_nd(g, False)
    [[['_', '_'], ['_', '3'], ['1', '1'], [' ', ' ']],
    [['_', '_'], ['_', '_'], ['1', '1'], [' ', ' ']]]

    >>> render_nd(g, True)
    [[['3', '.'], ['3', '3'], ['1', '1'], [' ', ' ']],
    [['.', '3'], ['3', '.'], ['1', '1'], [' ', ' ']]]
    """
    board = create_array(game["dimensions"], 0)
    for coordinate in all_possible_coordinates(game["dimensions"]):
        value = get_value(game["board"], coordinate)
        replace_value(board, coordinate, str(value))
        if value == 0:
            replace_value(board, coordinate, " ")
        if not xray:
            if_hidden = get_value(game["hidden"], coordinate)
            if if_hidden:
                replace_value(board, coordinate, "_")
    return board


if __name__ == "__main__":
    # Test with doctests. Helpful to debug individual lab.py functions.
    _doctest_flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    doctest.testmod(optionflags=_doctest_flags)  # runs ALL doctests

    # Alternatively, can run the doctests JUST for specified function/methods,
    # e.g., for render_2d_locations or any other function you might want.  To
    # do so, comment out the above line, and uncomment the below line of code.
    # This may be useful as you write/debug individual doctests or functions.
    # Also, the verbose flag can be set to True to see all test results,
    # including those that pass.
    #
    # doctest.run_docstring_examples(
    #    new_game_nd,
    #    globals(),
    #    optionflags=_doctest_flags,
    #    verbose=False
    # )

    # result = new_game_2d(2, 3, [(0, 0)])
    # print(result)
