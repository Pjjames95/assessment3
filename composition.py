#two classes, Engine and Car. The Car class should have an attribute engine that is an instance of the Engine class.
# Write methods for Engine (e.g., start() and stop()) and
# show how the Car class can use these methods to control the engine
class Engine:
    def __init__(self):
        pass
    def start(self):
        print("Our engine is on")

    def stop(self):
        print("Our engine is off")


class Cars:
    #the car inherits the methods from the engine class and its output
    def __init__(self, engine):
        self.engine = engine

    def start_from_engine(self):
        self.engine.start()

    def stop_from_engine(self):
        self.engine.stop()

engine = Engine()
car = Cars(engine)

car.start_from_engine()
car.stop_from_engine()