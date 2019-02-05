import gym
from gym.spaces import *
import sys




def print_spaces(space):
    print(space)
    if isinstance(space, Box):
        print("\n Cola inferior: ", space.low)        
        print("\n Cola superior: ", space.high)
    
if __name__ == "__main__":
    environment = gym.make(sys.argv[1])
    print("Espacio de Observaciones:")
    print_spaces(environment.observation_space)
    print("Espacio de Acciones:")
    print_spaces(environment.action_space)
    try:
        print("Descripcion de las acciones: ", environment.unwrapped.get_action_meanings())
    except AttributeError:
        pass
