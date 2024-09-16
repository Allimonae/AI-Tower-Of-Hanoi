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
    peg0 = []
    peg1 = []
    peg2 = []

    def __init__(self, number_of_disks = 4):
        """Constructor for TowerOfHanoi

        Args:
            number_of_disks (int, optional): The number of disks for the game. Defaults to 4.
        """
        for i in range(number_of_disks):
            self.peg0.append(number_of_disks - i)
    
    def move(self, source, destination):
        """ Moves the top disk from a source peg to the destiniation peg.
            No bigger disk may be placed on stop of a smaller one. 

        Args:
            source (int): The number of the peg to move a disk from. Possible values are 0, 1, or 2.
            destination (int): The number of the peg to move a disk to. Possible values are 0, 1, or 2.

        Returns:
            boolean: Returns True if the move was made and False otherwise.
        """

        def choose(num):
            """ Chooses peg based on num parameter. 

            Arg:
                num (int): An integer that may corresponds with a peg. Possible values are 0, 1, or 2.

            Returns:
                list: Returns peg0, peg1, or peg2
            """
            if num == 0:
                return self.peg0
            elif num == 1:
                return self.peg1
            elif num == 2:
                return self.peg2

        if (source not in [0, 1, 2]) or (destination not in [0, 1, 2]):
            return False

        if (source == destination) or (not bool(choose(source))):
            return False

        if bool(choose(destination)) and (choose(source)[-1] > choose(destination)[-1]):
            return False
        
        choose(destination).append(choose(source)[-1])
        choose(source).pop()
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
        if bool(self.peg0) or bool(self.peg1):
            return False

        if not self.peg2:
            return True

        if self.peg2[0] != len(self.peg2):
            return False

        for i in range(1, len(self.peg2)):
            # print(self.peg2[i], self.peg2[i - 1] - 1)
            if self.peg2[i] != self.peg2[i - 1] - 1:
                return False
        
        return True

    def reset(self):
        """Resets the Tower of Hanoi to the initial state.
        """
        num = len(self.peg0) + len(self.peg1) + len(self.peg2)
        
        self.peg0 = []
        self.peg1 = []
        self.peg2 = []

        for i in range(num):
            self.peg0.append(num - i)

    def get_state(self):
        """Returns the current state of the Tower.

        Returns:
            list: List containing three lists representing each peg in ascending order of peg number.
        """
        return [self.peg0, self.peg1, self.peg2]

class TTTowerOfHanoi(TowerOfHanoi):
    """There are three pegs, numbers 1-number of disks are used instead of disks, 
       where a bigger number is a bigger disk.

       TTTowerOfHanoi is the same as the original problem, except there are 3 disks of each size,
       and a disk may be placed on one of the same size or a larger one

       Example initial state with 3 sizes of disks:
       Peg 0: [3, 3, 3, 2, 2, 2, 1, 1, 1]
       Peg 1: []
       Peg 2: []

       Goal state for example:
       Peg 0: []
       Peg 1: []
       Peg 2: [3, 3, 3, 2, 2, 2, 1, 1, 1]
    """

    def __init__(self, number_of_disks = 4):
        """Constructor for TTTowerOfHanoi

        Args:
            number_of_disks (int, optional): The number of disk sizes for the game. Defaults to 4.
        """
        for i in range(number_of_disks):
            for n in range(3):
                self.peg0.append(number_of_disks - i)

    def is_goal(self):
        """Checks whether the current state of the puzzle is the goal state.

        Returns:
            boolean: Returns True if disks (numbers) are in descending order on the third peg and False otherwise.
        """ 
        self.peg0 = []
        self.peg1 = []
        self.peg2 = [3, 3, 3, 2, 2, 2, 1, 1, 1]

        self.print_state()

        if bool(self.peg0) or bool(self.peg1):
            print("hi")
            return False

        if not bool(self.peg2):
            return True

        num_of_sizes = len(self.peg2) / 3

        if self.peg2[0] != num_of_sizes:
            print("hi1")
            return False

        for i in range(num_of_sizes):
            for j in range(3):
                print(i, j, peg2[3 * i + j], self.peg2[i - 1] - 1)
                if self.peg2[3 * i + j] != self.peg2[i - 1] - 1:
                    return False
        
        return True

    def reset(self):
        """Resets the Tower of Hanoi to the initial state.
        """
        num = int((len(self.peg0) + len(self.peg1) + len(self.peg2)) / 3)
        
        self.peg0 = []
        self.peg1 = []
        self.peg2 = []

        for i in range(num):
            for n in range(3):
                self.peg0.append(num - i)

def main():
    tower = TTTowerOfHanoi(3)
    # print("peg0 elements:", TowerOfHanoi.peg0)
    # print(TTTowerOfHanoi.move(tower, 0, 1))
    # print(TTTowerOfHanoi.move(tower, 0, 2))
    # print(TTTowerOfHanoi.move(tower, 1, 2))
    # print(TTTowerOfHanoi.move(tower, 0, 1))
    # print(TTTowerOfHanoi.move(tower, 2, 0))
    # print(TTTowerOfHanoi.move(tower, 2, 1))
    # print(TTTowerOfHanoi.move(tower, 0, 1))
    # print(TTTowerOfHanoi.move(tower, 0, 2))
    # print(TTTowerOfHanoi.move(tower, 1, 2))
    # print(TTTowerOfHanoi.move(tower, 1, 0))
    # print(TTTowerOfHanoi.move(tower, 2, 0))
    # print(TTTowerOfHanoi.move(tower, 1, 2))
    # print(TTTowerOfHanoi.move(tower, 0, 1))
    # print(TTTowerOfHanoi.move(tower, 0, 2))
    # print(TTTowerOfHanoi.move(tower, 1, 2))

    # TTTowerOfHanoi.reset(tower)
    # print("reset:", TTTowerOfHanoi.is_goal(tower))
    # print(TTTowerOfHanoi.get_state(tower))
    print("goal: ", TTTowerOfHanoi.is_goal(tower))

if __name__ == "__main__":
    main()