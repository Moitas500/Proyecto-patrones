from Command import Command

class Invoker():
    orden: Command
    
    def __init__(self, orden: Command):
        self.orden = orden

    def run(self):
        self.orden.execute()
