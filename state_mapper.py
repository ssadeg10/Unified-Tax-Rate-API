class StateMapper:
    def __init__(self):
        self.state_map = {}
    
    def register_function(self, id, function):
        self.state_map[id] = function
    
    def call(self, id, *args, **kwargs):
        try:
            return self.state_map[id](*args, **kwargs)
        except Exception as e:
            return f"{e}: not found"

state_mapper = StateMapper()

def register(id):
    def decorator(function):
        state_mapper.register_function(id, function)
        return function
    return decorator