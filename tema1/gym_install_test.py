# Visual studio Code

import gym

environment = gym.make("BipedalWalker-v2") #lanzamos una instancia del videojuego
environment.reset() #limpiamos y preparamos el entorno

for _ in range(20000): #durante 2000 veces
    environment.render() #pintamos en pantalla la accion
    environment.step(environment.action_space.sample()) #tomamos una decision aleatorea

environment.close()  #se cierra la sesion de Open AI Gym
