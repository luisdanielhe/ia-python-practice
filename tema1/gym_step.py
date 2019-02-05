import gym

environment = gym.make("Qbert-v0")
MAX_NUM_EPISODES = 10
MAX_STEPS_PER_EPISODE = 500

for episode in range(MAX_NUM_EPISODES):
    obs=environment.reset()
    for step in range(MAX_STEPS_PER_EPISODE):
        environment.render()
        action = environment.action_space.sample()
        next_state, reward, done, info = environment.step(action)
        obs = next_state

        if done is True:
            print("\n Episode #{} terminando  en {} steps.".format(episode, step+1))
            break

environment.close()