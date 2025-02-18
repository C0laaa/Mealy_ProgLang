def mealy_machine():
    transitions = {}  # Dictionary to store transitions
    current_state = input("Enter the starting state: ")
    states = [current_state]  # List to keep track of states

    while True:
        from_state = input("Enter 'first state (or 'done'): ")
        if from_state.lower() == 'done':
            break

        if from_state not in states:
            states.append(from_state)

        input_symbol = input(f"Enter input symbol for state {from_state}: ")
        next_state = input(f"Enter 'to' state for ({from_state}, {input_symbol}): ")

        if next_state not in states:
            states.append(next_state)

        output_symbol = input(f"Enter output symbol for ({from_state}, {input_symbol}): ")
        transitions[(from_state, input_symbol)] = (next_state, output_symbol)

    while True:
        input_seq = input("Enter input sequence (or 'exit'): ")
        if input_seq.lower() == 'exit':
            break

        output_seq = ""
        current_state_run = current_state  # Reset to starting state for each run

        for input_sym in input_seq:
            if (current_state_run, input_sym) in transitions:
                next_state, output = transitions[(current_state_run, input_sym)]
                current_state_run = next_state
                output_seq += output
            else:
                output_seq = "Invalid Input"  # Or handle as you prefer
                break  # Stop processing on invalid input

        print("Output:", output_seq)

mealy_machine()