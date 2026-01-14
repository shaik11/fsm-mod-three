from fsm.core import FiniteStateMachine

class ModThreeFSM:
    """
        FSM implementation to compute binary % 3
    """
    STATE_OUTPUT = {
        "S0": 0,
        "S1": 1,
        "S2": 2,
    }

    def __init__(self):
        states = {"S0", "S1", "S2"}
        alphabet = {"0", "1"}
        initial_state = "S0"
        final_states = {"S0", "S1", "S2"}

        transitions = {
            "S0": {"0": "S0", "1": "S1"},
            "S1": {"0": "S2", "1": "S0"},
            "S2": {"0": "S1", "1": "S2"},
        }

        self.fsm = FiniteStateMachine(
            states=states,
            alphabet=alphabet,
            initial_state=initial_state,
            final_states=final_states,
            transitions=transitions,
        )

    def mod_three(self, binary_string: str) -> int:
        final_state = self.fsm.process(binary_string)
        return self.STATE_OUTPUT[final_state]