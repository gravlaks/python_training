from FSM import FSM
def main():
    print("Test program")

    periodic_functions = {print_hello_world:{"args": (), "period": 1, "entry_states": ("second state"), "end_state": "second state"}, print_every_five:{"args": (), "period": 5, "entry_states": ("init", "second state"), "end_state": "second state"}, print_anything: {"args": ("hello every 0.5 seconds", ), "period": 0.5, "entry_states": ("init"), "end_state": "init"}}

    one_time_functions = {print_anything:{"args": ("hello only when 10 seconds have gone", ), "execution_time": 10}}
    fsm = FSM(periodic_functions, one_time_functions)

    fsm.run()
    

def print_hello_world():
    print("Hello world every 1 second!")

def print_every_five():
    print("Hello 5th second")

def print_anything(string):
    print(string)


if __name__ == "__main__":
    main()
