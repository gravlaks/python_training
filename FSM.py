from Timer import Timer
class FSM:

    def __init__(self, periodic_functions, one_time_functions, init_state="init"):
        self.periodic_functions = {}
        self.one_time_functions = {}
        self.current_state = init_state


         

        for fnc, parameters in periodic_functions.items():
            period = parameters["period"] 
            args = parameters["args"]
            entry_states = parameters["entry_states"]
            end_state = parameters["end_state"]

            self.periodic_functions[fnc] = {}


            self.periodic_functions[fnc]["timer"] = Timer(period)
            self.periodic_functions[fnc]["args"] = args
            self.periodic_functions[fnc]["entry_states"] = entry_states
            self.periodic_functions[fnc]["end_state"] = end_state

        for fnc, parameters in one_time_functions.items():
            execution_time = parameters["execution_time"]
            args = parameters["args"]

            self.one_time_functions[fnc] = {}
            self.one_time_functions[fnc]["timer"] = Timer(execution_time)
            self.one_time_functions[fnc]["args"] = args
            self.one_time_functions[fnc]["done"] = False
        

    def run(self):

        while True:

            for fnc, parameters in self.periodic_functions.items():
                
                args = parameters["args"]
                timer = parameters["timer"]
                entry_states = parameters["entry_states"] 
                end_state = parameters["end_state"]

                if self.current_state in entry_states:
                    if timer.timeout():
                        print("Current state", self.current_state)
                        fnc(*args)
                        timer.reset()
                        self.current_state = end_state

            for fnc, parameters in self.one_time_functions.items():
                args = parameters["args"]
                timer = parameters["timer"]
                done = parameters["done"]
                
                if timer.timeout() and not done:
                    parameters["done"] = True
                    fnc(*args)
                
