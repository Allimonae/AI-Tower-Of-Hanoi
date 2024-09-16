import time

class TowerOfHanoi:
    """Representation of the Tower of Hanoi Puzzle
       Link: https://en.wikipedia.org/wiki/Tower_of_Hanoi

       There are three pegs, numbers 1-number of disks are used instead of disks, 
       where a bigger number is a bigger disk.

       Example initial state with 3 disks:
       Peg 0: [3, 2, 1]
       Peg 1: []
       Peg 2: []

       Goal state for example:
       Peg 0: []
       Peg 1: []
       Peg 2: [3, 2, 1]
    """

    def __init__(self, number_of_disks = 4):
        """Constructor for TowerOfHanoi

        Args:
            number_of_disks (int, optional): The number of disks for the game. Defaults to 4.
        """
        # initialize peg0, peg1, peg2
        self.peg0 = []
        self.peg1 = []
        self.peg2 = []

        if number_of_disks < 1:
            print(f"Error: number of disks ({number_of_disks}) not allowed")
        else:
            # peg 0 initialized as a list containing specified number of disks, in consecutive descending order
            self.peg0 = list(range(number_of_disks, 0, -1))
    
    def move(self, source, destination):
        """ Moves the top disk from a source peg to the destiniation peg.
            No bigger disk may be placed on stop of a smaller one. 

        Args:
            source (int): The number of the peg to move a disk from. Possible values are 0, 1, or 2.
            destination (int): The number of the peg to move a disk to. Possible values are 0, 1, or 2.

        Returns:
            boolean: Returns True if the move was made and False otherwise.
        """
        # A list with indices 0, 1, 2 corresponding with peg0, peg1, peg2
        choose_peg = [self.peg0, self.peg1, self.peg2]

        if source not in [0, 1, 2] or destination not in [0, 1, 2]:
            print(f"Error: source peg ({source}) or destination peg ({destination}) out of range")
            return False

        if source == destination:
            print(f"Error: source peg ({source}) == destination peg ({destination})")
            return False
        
        if not choose_peg[source]:
            print(f"Error: source peg ({source}) is empty")
            return False

        if choose_peg[destination] and choose_peg[source][-1] > choose_peg[destination][-1]:
            print(f"Error: source disk size ({choose_peg[source][-1]}) is greater than destination disk size ({choose_peg[destination][-1]})")
            return False
        
        # Pop last element of source and append it to destination
        choose_peg[destination].append(choose_peg[source].pop())
        return True

    def print_state(self):
        """Prints the state of each peg on one line each.
        """
        print("Peg 0:" , self.peg0)
        print("Peg 1:" , self.peg1)
        print("Peg 2:" , self.peg2)

    def is_goal(self):
        """Checks whether the current state of the puzzle is the goal state.

        Returns:
            boolean: Returns True if disks (numbers) are in descending order on the third peg and False otherwise.
        """ 
        # Check if peg0 and peg1 are empty
        if self.peg0 or self.peg1:
            return False

        # Check if first disk is equal to total number of disks
        if self.peg2[0] != len(self.peg2):
            return False

        # Check if peg2 is arranged in consecutive descending order, any disk should be 1 smaller than the previous
        for i in range(1, len(self.peg2)):
            if self.peg2[i] != self.peg2[i - 1] - 1:
                return False
        
        return True

    def reset(self):
        """Resets the Tower of Hanoi to the initial state.
        """
        # Calculate total number of disks
        num = len(self.peg0) + len(self.peg1) + len(self.peg2)
        
        # Reset pegs
        self.peg0 = []
        self.peg1 = []
        self.peg2 = []

        # Repopulate peg0
        self.peg0 = list(range(num, 0, -1))

    def get_state(self):
        """Returns the current state of the Tower.

        Returns:
            list: List containing three lists representing each peg in ascending order of peg number.
        """
        return [self.peg0, self.peg1, self.peg2]

def main():
    tower = TowerOfHanoi(4)
    TowerOfHanoi.print_state(tower)
    print(TowerOfHanoi.move(tower, 0, 4))
    print(TowerOfHanoi.move(tower, 0, 0))
    print(TowerOfHanoi.move(tower, 1, 2))
    print(TowerOfHanoi.move(tower, 0, 1))
    print(TowerOfHanoi.move(tower, 2, 0))
    print(TowerOfHanoi.move(tower, 2, 1))
    print(TowerOfHanoi.move(tower, 0, 1))
    TowerOfHanoi.print_state(tower)
    # print(TowerOfHanoi.move(tower, 0, 2))
    print(TowerOfHanoi.move(tower, 1, 2))
    print(TowerOfHanoi.move(tower, 1, 0))
    print(TowerOfHanoi.move(tower, 2, 0))
    print(TowerOfHanoi.move(tower, 1, 2))
    print(TowerOfHanoi.move(tower, 0, 1))
    print(TowerOfHanoi.move(tower, 0, 2))
    print(TowerOfHanoi.move(tower, 1, 2))

    # TowerOfHanoi.reset(tower)
    # print("reset:", TowerOfHanoi.is_goal(tower))
    # print(TowerOfHanoi.get_state(tower))
    print("goal: ", TowerOfHanoi.is_goal(tower))

if __name__ == "__main__":
    main()