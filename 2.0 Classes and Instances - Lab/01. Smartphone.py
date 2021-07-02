class Smartphone:
    apps = []
    is_on = False

    def __init__(self, memory):
        self.memory = memory
      
    def power(self):
        if not self.is_on:
            self.is_on = True
        else:
            self.is_on = False

    def install(self, app, app_memory):
        if self.is_on and self.memory >= app_memory:
            self.apps.append(app)
            self.memory -= app_memory
            return f'Installing {app}'
        if not self.is_on and self.memory >= app_memory:
            return f'Turn on your phone to install {app}'
        
        return f'Not enough memory to install {app}'


    def status(self):
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'     

