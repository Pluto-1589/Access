def req_steps(num_disks):
    #  The player can only move one disk at a time.
    # Only the top disk of one tower can be moved.
    # Larger disks cannot be placed on top of a smaller disk.

    # calculates the number of steps that are required to move a stack of n disks from one tower to another in an optimal game of Towers of Hanoi.

    if num_disks == 1:
        return 1
    else:
        return 2 * req_steps(num_disks - 1) + 1


print("For moving {} disks, {} steps are required.".format(3, req_steps(3)))
