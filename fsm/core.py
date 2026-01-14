from typing import Dict, Set, Any

class FiniteStateMachine:
    """
        Generic Finite State Automaton (FSM) implementation.
        FA = (Q, Σ, q0, F, δ)
    """
    def __init__(
        self,
        states: Set[Any],
        alphabet: Set[str],
        initial_state: Any,
        final_states: Set[Any],
        transitions: Dict[Any, Dict[str, Any]],
    ):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions

        self._validate()

    def _validate(self):
        if self.initial_state not in self.states:
            raise ValueError("Initial state must be in states")

        if not self.final_states.issubset(self.states):
            raise ValueError("Final states must be subset of states")

        for state, rules in self.transitions.items():
            if state not in self.states:
                raise ValueError(f"Invalid transition state: {state}")

            for symbol, next_state in rules.items():
                if symbol not in self.alphabet:
                    raise ValueError(f"Invalid symbol: {symbol}")
                if next_state not in self.states:
                    raise ValueError(f"Invalid next state: {next_state}")

    def process(self, input_string: str) -> Any:
        """
        Process input symbols and return final state.
        """
        current_state = self.initial_state

        for symbol in input_string:
            if symbol not in self.alphabet:
                raise ValueError(f"Invalid input symbol: {symbol}")

            current_state = self.transitions[current_state][symbol]

        return current_state