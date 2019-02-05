
import gym
import sys

def run_gym_environment(argv):
    ## el primer parametro de argv es el nombre del entorno a ejecutar
    environment = gym.make(argv[1])
    environment.reset()
    for _ in range(int(argv[2])):
        environment.render()
        environment.step(environment.action_space.sample())
    environment.close()

if __name__ == "__main__":
    run_gym_environment(sys.argv)