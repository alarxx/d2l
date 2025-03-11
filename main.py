import module
from module import greet
# import packet.module
import packet.module as pm

if __name__ == "__main__":
    print("Hello, World!")

    module.greet()
    greet()

    # packet.module.greet()
    pm.greet()
