from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class ResponseObserver(Observer):
    def update(self, message: str):
        print(f"Atualização: {message}")

class Subject(ABC):
    def __init__(self):
        self.observers = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, message: str):
        for observer in self.observers:
            observer.update(message)

class ResponseNotifier(Subject):
    def change_response(self, response: str):
        self.notify(response)
