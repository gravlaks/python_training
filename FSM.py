from Timer import Timer
class FSM:

    def __init__(self,tasks, trace, init_state="init"):
        self.tasks = tasks
        self.trace = trace
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
                self.tasks[task_key]["is_done"] = False


        

    def run(self):

# Iterate all tasks and find out which ones should be run
        for task, parameters in self.tasks.items():

            fnc = parameters["fnc"]
            args = parameters["args"]
            timer = parameters["timer"]
            entry_states = parameters["entry_states"] 
            end_state = parameters["end_state"]
            periodic = parameters["periodic"]
            trace_dependent = parameters["trace_dependent"]

            if self.current_state in entry_states:
                
                if trace_dependent:
                    args = (*args, self.trace)

                if periodic:
                    if timer.timeout():
                        timer.reset()
                        if end_state =="return_value":
                            self.current_state = fnc(*args)
                        elif end_state == "no_change":
                            fnc(*args)
                            pass
                        else:

                            fnc(*args)
                            self.current_state = end_state

                else: #task should only be done once

                    is_done = parameters["is_done"]
                    if timer.timeout() and not is_done:
                        parameters["is_done"] = True
                        if end_state =="return_value":
                            self.current_state = fnc(*args)
                        elif end_state == "no_change":
                            fnc(*args)
                            pass
                        else:
                            fnc(*args)
                            self.current_state = end_state
            

