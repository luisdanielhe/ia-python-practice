# Visual studio Code

import gym

environment = gym.make("MountainCar-v0") #lanzamos una instancia del videojuego
environment.reset() #limpiamos y preparamos el entorno

for _ in range(2000): #durante 2000 veces
    environment.render() #pintamos en pantalla la accion
    environment.step(environment.action_space.sample()) #tomamos una decision aleatorea
