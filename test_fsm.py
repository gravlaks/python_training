from FSM import FSM

def foo(string_to_print):
    print(string_to_print)

def griffin_on():
    print("turning on griffin")

def read_uart():
    print("reading uart")

def change_state():
    print("ten seconds, moving to third state")
    return "third_state"

i = 0
def check_for_starting():
    global i
    i += 1
    print("Check for starting")
    if i == 10:
        print("Turned on")
        return "griffin_started"
        
    else:
        return "griffin_turning_on"

def main():
    print("Test program")
    

    task_1_config = {"fnc": read_uart, "args": (), "periodic": True, "period": 0.1,  "entry_states": ("init", "griffin_turning_on", "griffin_started"), "end_state": "no_change"}
    task_2_config = {"fnc": griffin_on, "args": (), "periodic": False, "execution_time":2, "entry_states": ("init"), "end_state": "griffin_turning_on"}
    task_3_config = {"fnc": check_for_starting, "args": (), "periodic": True, "period": 0.5, "entry_states": ("griffin_turning_on"), "end_state": "return_value"}
    task_4_config = {"fnc": change_state, "args": (), "periodic": False, "execution_time": 10, "entry_states":("init", "second_state"), "end_state": "return_value"}
    task_when_second_state_config = {"fnc": foo, "args": ("Now in second_state", ), "periodic": False, "execution_time": 0, "entry_states":("second_state"), "end_state": "second_state"}
    tasks = {"task_1":task_1_config, "task_2": task_2_config, "task_3": task_3_config}

    trace = ""
    fsm = FSM(tasks, trace)

    while True:
        fsm.run()
    


if __name__ == "__main__":
    main()
