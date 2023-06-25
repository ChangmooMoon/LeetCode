from threading import *

class Foo:
    def __init__(self):
        self.lock = [Lock(), Lock()]
        for _ in self.lock:
            _.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.lock[0].release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.lock[0]:
            printSecond()
            self.lock[1].release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.lock[1]:
            printThird()