from FSM import FSM

def foo(string_to_print):
    print(string_to_print)

def print_hello_world():
    print("Hello world every 1 second!")

def print_every_five():
    print("Hello 5th second")

def change_state():
    print("ten seconds, moving to third state")
    return "third_state"
def main():
    print("Test program")
    

    task_1_config = {"fnc": print_hello_world, "args": (), "periodic": True, "period": 1,  "entry_states": ("second state"), "end_state": "second state"}
    task_2_config = {"fnc": print_every_five, "args": (), "periodic": True, "period": 5, "entry_states": ("init", "second state"), "end_state": "second state"}
    task_3_config = {"fnc": foo, "args": ("hello every 0.5 seconds", ), "periodic": True, "period": 0.5, "entry_states": ("init"), "end_state": "init"}
    task_4_config = {"fnc": change_state, "args": (), "periodic": False, "execution_time": 10, "entry_states":("init", "second state"), "end_state": "return_value"}
    task_when_second_state_config = {"fnc": foo, "args": ("Now in second state", ), "periodic": False, "execution_time": 0, "entry_states":("second state"), "end_state": "second state"}
    tasks = {"task_1":task_1_config, "task_2": task_2_config, "task_3": task_3_config, "task_4": task_4_config, "task_when_second_state": task_when_second_state_config}

    fsm = FSM(tasks)

    fsm.run()
    


if __name__ == "__main__":
    main()
