from Timer import Timer
class FSM:

    def __init__(self,tasks, init_state="init"):
        self.tasks = tasks
        self.current_state = init_state


        for task_key, parameters in self.tasks.items():
            fnc = parameters["fnc"]
            periodic = parameters["periodic"]

            if periodic:
                period = parameters["period"] 
                self.tasks[task_key]["timer"] = Timer(period)

            if not periodic:
                execution_time = parameters["execution_time"]
                self.tasks[task_key]["timer"] = Timer(execution_time)
                self.tasks[task_key]["done"] = False


        

    def run(self):

        while True:

            for task, parameters in self.tasks.items():
                fnc = parameters["fnc"]
                
                args = parameters["args"]
                timer = parameters["timer"]
                entry_states = parameters["entry_states"] 
                end_state = parameters["end_state"]

                periodic = parameters["periodic"]

                if self.current_state in entry_states:
                    if periodic:
                        if timer.timeout():
                            if end_state =="return_value":
                                self.current_state = fnc(*args)
                            else:
                                fnc(*args)
                                self.current_state = end_state
                            timer.reset()
                    else:
                        done = parameters["done"]
                        if timer.timeout() and not done:
                            parameters["done"] = True
                            if end_state =="return_value":
                                self.current_state = fnc(*args)
                            else:
                                fnc(*args)
                                self.current_state = end_state
                

