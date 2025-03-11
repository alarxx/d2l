import sys

current_module = sys.modules[__name__]

def _protected():
    print("Module's private function")

def greet():
    print("Hello, Module!:", __name__, current_module)

    current_module._protected()
