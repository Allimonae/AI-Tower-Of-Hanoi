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
            self.num_disks = number_of_disks
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

        # Check length if length of peg2 equals num_disks
        if len(self.peg2) != self.num_disks:
            return False

        # Check if peg2 is arranged in consecutive descending order, any disk should be 1 smaller than the previous
        for i in range(self.num_disks):
            if self.peg2[i] != self.num_disks - i:
                return False
        
        return True

    def reset(self):
        """Resets the Tower of Hanoi to the initial state.
        """       
        # Reset pegs
        self.peg0 = []
        self.peg1 = []
        self.peg2 = []

        # Repopulate peg0
        if self.num_disks:
            self.peg0 = list(range(self.num_disks, 0, -1))
        else:
            print(f"Error: number of disks not yet set")

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
        # initialize peg0, peg1, peg2
        self.peg0 = []
        self.peg1 = []
        self.peg2 = []

        if number_of_disks < 1:
            print(f"Error: number of disks ({number_of_disks}) not allowed")
        else:
            self.num_disks = number_of_disks
            # peg 0 initialized as a list containing specified number of disks, 3 disks of each size
            for i in range(number_of_disks):
                for n in range(3):
                    self.peg0.append(number_of_disks - i)

    def is_goal(self):
        """Checks whether the current state of the puzzle is the goal state.

        Returns:
            boolean: Returns True if disks (numbers) are in descending order on the third peg and False otherwise.
        """
        # Check if peg0 and peg1 are empty
        if self.peg0 or self.peg1:
            return False

        # Check length if length of peg2 equals num_disks * 3
        if len(self.peg2) != self.num_disks * 3:
            return False

        # Check if peg2 is arranged in consecutive descending order, with 3 of each disk size
        for i in range(0, self.num_disks):
            for j in range(3):
                if self.peg2[3 * i + j] != self.num_disks - i:
                    return False
            
        return True

    def reset(self):
        """Resets the Tower of Hanoi to the initial state.
        """
        # Reset pegs
        self.peg0 = []
        self.peg1 = []
        self.peg2 = []

        # Repopulate peg0
        if self.num_disks:
            for i in range(self.num_disks):
                for n in range(3):
                    self.peg0.append(self.num_disks - i)
        else:
            print(f"Error: number of disks not yet set")

class SpecialTowerOfHanoi(TowerOfHanoi):
    """There are three pegs, numbers 1-number of disks are used instead of disks, 
       where a bigger number is a bigger disk.

       In this version of the problem, there are no	triple disks, 
       but there is a special disk that is initially alone on the second peg
       
       Use	 “_” to	 represent the special disk.	 

       Example initial state with 3 disks and k = 2:
       Peg 0: [3, 2, 1]
       Peg 1: ["_"]
       Peg 2: []

       Goal state for example:
       Peg 0: []
       Peg 1: []
       Peg 2: [3, 2, "_", 1]
    """
    def __init__(self, number_of_disks, k = 0):
        """Constructor for TowerOfHanoi

        Args:
            number_of_disks (int, optional): The number of disks for the game. Defaults to 4.
            k (int, optional): The size of the special disk
        """
        self.peg0 = []
        self.peg1 = []
        self.peg2 = []

        if number_of_disks < 1:
            print(f"Error: number of disks ({number_of_disks}) not allowed")
        if k > number_of_disks or k < 0:
            print(f"Error: k ({k}) out of range")
        else:
            self.num_disks = number_of_disks
            self.special = k
            # peg 0 initialized as a list containing specified number of disks, in consecutive descending order
            self.peg0 = list(range(number_of_disks, 0, -1))
            self.peg1.append("_")

    def move(self, source, destination):
        """ Moves the top disk from a source peg to the destiniation peg.
            No bigger disk may be placed on stop of a smaller one. 

            The	special	disk can be	placed on any disk, but	the	only disks that	can	be placed on top of	the	special	disk 
            are	those whose	number are no more than	k, and k ≤ number of disks in the game.

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
        
        source_disk = choose_peg[source][-1]
        dest_disk = choose_peg[destination][-1] if choose_peg[destination] else None
        
        if source_disk == "_":
            choose_peg[destination].append(choose_peg[source].pop())
            return True

        if dest_disk == "_" and source_disk > self.special:
            print(f"Error: source disk size ({source_disk}) is greater than destination special disk size ({self.special})")
            return False
       
        if choose_peg[destination] and source_disk > dest_disk:
            print(f"Error: source disk size ({source_disk}) is greater than destination disk size ({dest_disk})")
            return False
        
        # Pop last element of source and append it to destination
        choose_peg[destination].append(choose_peg[source].pop())
        return True
    
    def is_goal(self):
        """Checks whether the current state of the puzzle is the goal state.

            The	special disk should	be ignored by the function that	checks for the goal	state but should meet	
            all	the	base conditions	for	the	original game once it ignores the special disk.

        Returns:
            boolean: Returns True if disks (numbers) are in descending order on the third peg and False otherwise.
        """ 
        # Check if peg0 and peg1 are empty or contain only "_"
        if (self.peg0 and self.peg0 != ["_"]) or (self.peg1 and self.peg1 != ["_"]):
            return False

        length = self.num_disks + (1 if "_" in self.peg2 else 0)
        if len(self.peg2) != length:
            return False

        # Check if peg2 is arranged in consecutive descending order, ignore position of special
        disks = list(filter(lambda disk: disk != "_", self.peg2))
        for i in range(len(disks)):
            if disks[i] != self.num_disks - i:
                return False
        
        return True

def main():
    tower = SpecialTowerOfHanoi(4)
    TTTowerOfHanoi.print_state(tower)
    tower.print_state()
    print(tower.move(0, 4))
    tower.print_state()
    print(tower.move(0, 0))
    tower.print_state()
    print(tower.move(1, 2))
    tower.print_state()
    print(tower.move(0, 1))
    tower.print_state()
    print(tower.move(2, 0))
    tower.print_state()
    print(tower.move(2, 1))
    tower.print_state()
    print(tower.move(0, 1))
    tower.print_state()
    tower.print_state()
    # print(tower.move(0, 2))
    tower.print_state()
    print(tower.move(1, 2))
    tower.print_state()
    print(tower.move(1, 0))
    tower.print_state()
    print(tower.move(2, 0))
    tower.print_state()
    print(tower.move(1, 2))
    tower.print_state()
    print(tower.move(0, 1))
    tower.print_state()
    print(tower.move(0, 2))
    tower.print_state()
    print(tower.move(1, 2))
    tower.print_state()
    print("goal: ", tower.is_goal())
    # tower.reset()
    tower.print_state()

if __name__ == "__main__":
    main()