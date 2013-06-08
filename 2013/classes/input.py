import sfml as sf

class Input():
    pressed = []
    hold = []
    released = []
    axes = dict()
    
    @staticmethod
    def process_event(event):
        if(event.pressed and not Input.get_key(event.code)):
            Input.pressed.append(event.code)
        elif(event.released):
            try: Input.hold.remove(event.code)
            except: pass
            Input.released.append(event.code)
            
    @staticmethod
    def update():
        for key in Input.pressed:
            Input.hold.append(key)
            Input.pressed.remove(key)
        Input.released = []
        
    @staticmethod
    def reset():
        pressed = []
        hold = []
        
    @staticmethod
    def get_key(code):
        return code in Input.hold or code in Input.pressed
        
    @staticmethod
    def get_key_down(code):
        return code in Input.pressed
        
    @staticmethod
    def get_key_up(code):
        return code in Input.released
        
    @staticmethod
    def define_axis(name, positive, negative):
        Input.axes[name] = InputAxis(positive, negative)
        
    @staticmethod
    def get_axis(name):
        try:
            return Input.axes[name].get_value()
        except KeyError:
            print("Input axis %s not defined" % name)
            return 0.0
        

class InputAxis():
    def __init__(self, positive, negative):
        self.positive = positive
        self.negative = negative
        
    def get_value(self):
        result = 1.0 if Input.get_key(self.positive) else 0.0
        if(Input.get_key(self.negative)):
            result -= 1.0
        return result