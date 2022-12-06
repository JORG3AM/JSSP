domains = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3]
}
constraints = {
    ('A', 'B'): lambda a, b: a > b,
    ('B', 'A'): lambda b, a: b < a,
    ('B', 'C'): lambda b, c: b == c,
    ('C', 'B'): lambda c, b: c == b,
}

def revise(x, y):
    """
    Make variable `x` arc consistent with variable `y`.
    To do so, remove values from `domains[x]` for which there is no
    possible corresponding value for `y` in `domains[y]`.
    Return True if a revision was made to the domain of `x`; return
    False if no revision was made.
    """
    revised = False

    # Get x and y domains
    x_domain = domains[x]
    y_domain = domains[y]

    # Get all arc (x, y) constraints
    all_constraints = [
        constraint for constraint in constraints if constraint[0] == x and constraint[1] == y]

    for x_value in x_domain:
        satisfies = False
        for y_value in y_domain:
            for constraint in all_constraints:
                constraint_func = constraints[constraint]
                if constraint_func(x_value, y_value):
                    satisfies = True
        if not satisfies:
            x_domain.remove(x_value)
            revised = True

    return revised


def ac3(arcs):
    """
    Update `domains` such that each variable is arc consistent.
    """
    # Add all the arcs to a queue.
    queue = arcs[:]

    # Repeat until the queue is empty
    while queue:
        # Take the first arc off the queue (dequeue)
        (x, y) = queue.pop(0)

        # Make x arc consistent with y
        revised = revise(x, y)

        # If the x domain has changed
        if revised:
            # Add all arcs of the form (k, x) to the queue (enqueue)
            neighbors = [neighbor for neighbor in arcs if neighbor[1] == x]
            queue = queue + neighbors


arcs = [('A', 'B'), ('B', 'A'), ('B', 'C'), ('C', 'B')]

ac3(arcs)

print(domains) # {'A': [2, 3], 'C': [1, 2], 'B': [1, 2]}