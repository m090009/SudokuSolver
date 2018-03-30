
from utils import *
from collections import defaultdict

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
diagonal_grid = True

# TODO: Update the unit list to add the new diagonal units
if diagonal_grid:
    diagonal_units = [[rows[i] + cols[i] for i in range(len(rows))]] + [[rows[i] + cols[::-1][i] for i in range (len(rows))]]
    unitlist = unitlist + diagonal_units


# Must be called after all units (including diagonals) are added to the unitlist
units = extract_units(unitlist, boxes)
peers = extract_peers(units, boxes)


def naked_twins(values):
    """Eliminate values using the naked twins strategy.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the naked twins eliminated from peers

    Notes
    -----
    Your solution can either process all pairs of naked twins from the input once,
    or it can continue processing pairs of naked twins until there are no such
    pairs remaining -- the project assistant test suite will accept either
    convention. However, it will not accept code that does not process all pairs
    of naked twins from the original input. (For example, if you start processing
    pairs of twins and eliminate another pair of twins before the second pair
    is processed then your code will fail the PA test suite.)

    The first convention is preferred for consistency with the other strategies,
    and because it is simpler (since the reduce_puzzle function already calls this
    strategy repeatedly).
    """
    # TODO: Implement this function!
    # case one: the naked twins are in the col peers
    # case two: the naked twins are in the row extract_peers
    # case three: the naked twins are in the box peers
    # for each box in values (grid)
    naked_twins = []
    print("method called")
    for box in values.keys():
        if len(values[box]) == 2: #Choose boxes that only have 2 digits
            # All box twin peers
            all_twin_peers = [peer for peer in peers[box] if values[box] == values[peer]]
            # This step is important for dynamicity
            naked_twin = [[twin, box] for twin in all_twin_peers]
            if naked_twin:
                naked_twins.extend(naked_twin)
            #   sort each of the twins to eliminate duplicates afterwards
            for twins in naked_twins:
                twins.sort()
    # eliminate duplicate twin combos
    naked_twins_sorted = set([tuple(x) for x in naked_twins])
    naked_twins = [list(x) for x in list(naked_twins_sorted)]
    print(naked_twins)
    if naked_twins:
        for twins in naked_twins:
                # Get twins' peers, the intersection btween the twins' peers 13 peers
                twin_peers = get_twins_common_peers(twins[0], twins[1])
                for peer in twin_peers:
                    # If the peer have more than one digit (not solved)
                    if len(values[peer]) > 1:
                        # Get the matches btween twin and the peer chars
                        # matches = [char for char in values[twins[0]] if char in values[peer]]
                        # if matches:
                        # Remove the matches from the peer
                        for digit in values[twins[0]]:
                            values[peer] = values[peer].replace(digit, '')
    # print()
    # print('=======================Sol========================')
    # print()
    # display(values)
    return values

def get_twins_common_peers(box, possible_twin):
    # Get the common peers btween the twins
    common_peers = list(set(peers[box]) & set(peers[possible_twin]))
    return common_peers

def eliminate(values):
    """Apply the eliminate strategy to a Sudoku puzzle

    The eliminate strategy says that if a box has a value assigned, then none
    of the peers of that box can have the same value.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the assigned values eliminated from peers
    """
    # TODO: Copy your code from the classroom to complete this function
    for box in values.keys():
         if len(values[box]) == 1:
             for peer in peers[box]:
                 values[peer] = values[peer].replace(values[box], '')
    return values


def only_choice(values):
    """Apply the only choice strategy to a Sudoku puzzle

    The only choice strategy says that if only one box in a unit allows a certain
    digit, then that box must be assigned that digit.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with all single-valued boxes assigned

    Notes
    -----
    You should be able to complete this function by copying your code from the classroom
    """
    # TODO: Copy your code from the classroom to complete this function
    for unit in unitlist:
        for digit in cols:
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values


def reduce_puzzle(values):
    """Reduce a Sudoku puzzle by repeatedly applying all constraint strategies

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict or False
        The values dictionary after continued application of the constraint strategies
        no longer produces any changes, or False if the puzzle is unsolvable
    """
    # TODO: Copy your code from the classroom and modify it to complete this function
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Add eliminate strategy
        eliminate(values)
        # Add only choice strategy
        only_choice(values)
        # Add Naked Twins strategy
        naked_twins(values)
        # Check how may boxes were solved
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    """Apply depth first search to solve Sudoku puzzles in order to solve puzzles
    that cannot be solved by repeated reduction alone.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict or False
        The values dictionary with all boxes assigned or False

    Notes
    -----
    You should be able to complete this function by copying your code from the classroom
    and extending it to call the naked twins strategy.
    """
    # TODO: Copy your code from the classroom to complete this function
    # Depth first search
    values = reduce_puzzle(values) # Run the strategies until it stops
    if values is False: # Wrong values or error somewhere whoops!
        return False
    if all(len(values[s]) == 1 for s in boxes): # Its solved hooraay
        return values
    # Choose one of the unsolved boxes with the least amount of digits(2)
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Recursively search for the solution and return it
    for digit in values[s]:
        # Tree for each digit of the min chosen box
        new_sudoku = values.copy()
        new_sudoku[s] = digit
        # Recursive step and the branch
        attempt = search(new_sudoku)
        if attempt:
            return attempt


def solve(grid):
    """Find the solution to a Sudoku puzzle using search and constraint propagation

    Parameters
    ----------
    grid(string)
        a string representing a sudoku grid.

        Ex. '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    Returns
    -------
    dict or False
        The dictionary representation of the final sudoku grid or False if no solution exists.
    """
    values = grid2values(grid)
    values = search(values)
    return values


if __name__ == "__main__":
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(grid2values(diag_sudoku_grid))
    result = solve(diag_sudoku_grid)
    display(result)

    try:
        import PySudoku
        PySudoku.play(grid2values(diag_sudoku_grid), result, history)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
