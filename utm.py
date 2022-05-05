blank = "_"
tm = "010001001000100110101000100010011001000100000000000000010001001100101000100010011000100010000100010011000101000101001100001000100000000000000001000101100001010000010001001100000100010000001000100110000010100000101001100000010001000000010101100000010100000010100110000000100010000000010001011000000010100000001010110000000010001000000000010101100000000101000000000101011000000000100010000101001100000000010100000000010101100000000001000100000000000100010110000000000101000000000010101100000000000100010000000000000100010011000000000001010000000000001010110000000000001000101000100110000000000001010000000000001010110000000000000100010000000000000100010011000000000000010100000000000000100010011000000000000001010000000000000010001001100000000000000010100000000000000010001001100000000000000001000100000000000000000100010110000000000000000101000000000000000010001011000000000000000001010000000000000000010001011100_000"
code = ""
separator = '1'
delta_separator = '11'
input_separator = '111'
TAPE_LEFT_RIGHT_SPACE = 15
PRINT_LEFT_RIGHT_SPACE = 62
calculations_counter = 0
delta_dictionaries = []
tape_border_up = ""
tape_border_down = ""
tape = []
head = 0
print_head = 0
current_state = "q1"
calculation_finished = False


def generate_tape_border(temp_tape, head_char):
    tape_border = ""
    i = 0
    while i < len(temp_tape):
        tape_border = tape_border + "─"
        i += 1
    tape_border = tape_border[:print_head] + head_char + tape_border[print_head:]
    return tape_border


def find_and_remove_code():
    global code, tm
    code = tm.partition(input_separator)[2]
    tm = tm.partition(input_separator)[0]


def add_blanks():
    i = 0
    while i < TAPE_LEFT_RIGHT_SPACE:
        tape.append("_")
        i += 1


def initialize_tape():
    global tape
    global head
    global print_head
    add_blanks()
    for element in code:
        tape.append(element)
    add_blanks()
    head = TAPE_LEFT_RIGHT_SPACE
    print_head = 4 * TAPE_LEFT_RIGHT_SPACE + 2


def initialize_delta_tuples():
    coded_tuples = tm.split(delta_separator)
    delta_tuples = []
    for coded_tuple in coded_tuples:
        split_tuple = tuple(filter(None, coded_tuple.split(separator)))
        delta_tuples.append(split_tuple)
    return delta_tuples


def unary_to_state(unary):
    return "q" + str(len(unary))


def unary_to_tape_symbol(unary):
    if unary == '0':
        return '0'
    elif unary == '00':
        return '1'
    elif unary == '000':
        return blank


def unary_to_direction(unary):
    if unary == '0':
        return 'L'
    elif unary == '00':
        return 'R'


def convert_delta_tuples_to_dictionaries():
    for delta_tuple in initialize_delta_tuples():
        global delta_dictionaries
        delta_dictionary = {
            "state": unary_to_state(delta_tuple[0]),
            "tape_symbol_read": unary_to_tape_symbol(delta_tuple[1]),
            "state_change": unary_to_state(delta_tuple[2]),
            "tape_symbol_write": unary_to_tape_symbol(delta_tuple[3]),
            "direction": unary_to_direction(delta_tuple[4])
        }
        delta_dictionaries.append(delta_dictionary)


def print_tape():
    global tape_border_up
    global tape_border_down
    print("Tape:")
    temp_tape = "│ "
    for tape_element in tape:
        temp_tape = temp_tape + tape_element + " │ "
    temp_tape = temp_tape[print_head - PRINT_LEFT_RIGHT_SPACE:print_head + PRINT_LEFT_RIGHT_SPACE]
    if tape_border_up == "" and tape_border_down == "":
        tape_border_up = generate_tape_border(temp_tape, "┬")
        tape_border_down = generate_tape_border(temp_tape, "┴")
    print(tape_border_up)
    print(temp_tape)
    print(tape_border_down)
    print("\n")


def print_state(transition):
    print(
        "(" + transition.get('state') + ',' + transition.get('tape_symbol_read') + ') -> (' + transition.get(
            'state_change') + ',' + transition.get('tape_symbol_write') + ',' + transition.get('direction') + ')')
    print("Current state: " + transition.get('state'))
    print("Calculations: " + str(calculations_counter))
    print_tape()


def execute_transition():
    global head
    global print_head
    global current_state
    global calculations_counter
    transition_list = list(
        filter(lambda delta: delta['state'] == current_state and delta['tape_symbol_read'] == tape[head],
               delta_dictionaries))
    if len(transition_list) != 0:
        transition = transition_list[0]
        # write symbol on tape
        tape[head] = transition.get('tape_symbol_write')
        # change current state
        current_state = transition.get('state_change')
        # increment calculations counter
        calculations_counter += 1
        # print tape
        print_state(transition)
        # change direction (head index)
        if transition.get('direction') == 'R':
            head = head + 1
            print_head = print_head + 4
            if head + TAPE_LEFT_RIGHT_SPACE >= len(tape):
                add_blanks()
        elif transition.get('direction') == 'L':
            head = head - 1
            print_head = print_head - 4
    else:
        global calculation_finished
        calculation_finished = True


def calculate_result():
    print("Result: " + str(tape.count('0')))


def main():
    find_and_remove_code()
    initialize_tape()
    convert_delta_tuples_to_dictionaries()
    print_tape()

    while calculation_finished is False:
        execute_transition()
    calculate_result()


if __name__ == "__main__":
    main()
