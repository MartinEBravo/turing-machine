class Tape:
    """Tape class for representing the tape of the Turing machine."""
    def __init__(self, string, B):
        self.tape = list(string)
        self.head = 0
        self.B = B

    def read(self):
        if 0 <= self.head < len(self.tape):
            return self.tape[self.head]
        else:
            return self.B

    def write(self, symbol):
        if 0 <= self.head < len(self.tape):
            self.tape[self.head] = symbol
        elif self.head == len(self.tape):
            self.tape.append(symbol)
        else:
            while self.head < 0:
                self.tape.insert(0, self.B)
                self.head += 1
            while self.head >= len(self.tape):
                self.tape.append(self.B)

    def moveLeft(self):
        self.head -= 1

    def moveRight(self):
        self.head += 1

def TuringMachine(Q = [], Sigma = [], Gamma = [], Delta = [], q0 = '', B = '', F = []):
    """TuringMachine(Q, Sigma, Gamma, Delta, q0, B, F) -> TuringMachine

    Creates a Turing machine with the specified parameters.  The
    parameters are as follows:

    Q: A list of states in the machine.  Each state is a string.

    Sigma: A list of input symbols.  Each symbol is a string.

    Gamma: A list of tape symbols.  Each symbol is a string.

    Delta: A list of transitions.  Each transition is a tuple of the
    form (q, s, g, q', s', d), where q and q' are states, s and s' are
    input symbols, g and d are tape symbols, and d is either 'L' or
    'R'.

    q0: The initial state.  This is a string.

    B: The blank symbol.  This is a string.

    F: The list of final states.  Each state is a string.

    """
    return TuringMachineClass(Q, Sigma, Gamma, Delta, q0, B, F)

class TuringMachineClass:
    """A Turing machine.

    This class represents a Turing machine.  The machine is created
    using the TuringMachine function.

    """
    def __init__(self, Q, Sigma, Gamma, Delta, q0, B, F):
        """TuringMachineClass(Q, Sigma, Gamma, Delta, q0, B, F) -> TuringMachine

        Creates a Turing machine with the specified parameters.  The
        parameters are as follows:

        Q: A list of states in the machine.  Each state is a string.

        Sigma: A list of input symbols.  Each symbol is a string.

        Gamma: A list of tape symbols.  Each symbol is a string.

        Delta: A list of transitions.  Each transition is a tuple of the
        form (q, s, g, q', s', d), where q and q' are states, s and s' are
        input symbols, g and d are tape symbols, and d is either 'L' or
        'R'.

        q0: The initial state.  This is a string.

        B: The blank symbol.  This is a string.

        F: The list of final states.  Each state is a string.

        """
        self.Q = Q
        self.Sigma = Sigma
        self.Gamma = Gamma
        self.Delta = Delta
        self.q0 = q0
        self.B = B
        self.F = F

    def __str__(self):
        """str(self) -> str

        Returns a string representation of the Turing machine.
            
            """
        return 'TuringMachine(' + str(self.Q) + ', ' + str(self.Sigma) + ', ' + str(self.Gamma) + ', ' + str(self.Delta) + ', ' + str(self.q0) + ', ' + str(self.B) + ', ' + str(self.F) + ')'


    def simulate(self, string):
        """simulate(self, string) -> bool

        Simulates the Turing machine on the given string.  Returns True
        if the machine accepts the string, and False otherwise.

        """
        # Create the tape.
        tape = Tape(string, self.B)

        # Initialize the machine.
        q = self.q0

        # Run the machine.
        while True:
            # Find the transition for the current state and tape symbol.
            transition = None
            for t in self.Delta:
                if t[0] == q and t[1] == tape.read():
                    transition = t
                    break

            # If there is no transition, then halt.
            if transition == None:
                break

            # Write the new symbol.
            tape.write(transition[2])

            # Move the tape head.
            if transition[5] == 'L':
                tape.moveLeft()
            elif transition[5] == 'R':
                tape.moveRight()

            # Change the state.
            q = transition[3]

        # Return whether the final state is accepting.
        return q in self.F
    

# machine that accepts the language 0^n1^n
Q = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5']
Sigma = ['0', '1']
Gamma = ['0', '1', 'B']
Delta = [('q0', '0', '0', 'q0', '0', 'R'),
         ('q0', '1', '1', 'q1', '1', 'R'),
         ('q0', 'B', 'B', 'q5', 'B', 'R'),
         ('q1', '0', '0', 'q1', '0', 'R'),
         ('q1', '1', '1', 'q1', '1', 'R'),
         ('q1', 'B', 'B', 'q2', 'B', 'L'),
         ('q2', '0', '0', 'q2', 'B', 'L'),
         ('q2', '1', '1', 'q3', 'B', 'L'),
         ('q2', 'B', 'B', 'q5', 'B', 'R'),
         ('q3', '0', '0', 'q3', '0', 'L'),
         ('q3', '1', '1', 'q3', '1', 'L'),
            ('q3', 'B', 'B', 'q4', 'B', 'R'),
            ('q4', '0', '0', 'q4', 'B', 'R'),
            ('q4', '1', '1', 'q4', 'B', 'R'),
            ('q4', 'B', 'B', 'q5', 'B', 'R')]
q0 = 'q0'
B = 'B'
F = ['q5']
tm = TuringMachine(Q, Sigma, Gamma, Delta, q0, B, F)
# test maquina
test1 = '000111'
test2 = '00001111'
test3 = '010101010'
L = [test1, test2,test3]

for i in L:
    print(i, tm.simulate(i))