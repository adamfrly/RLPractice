import gym
from stable_baselines3 import A2C, PPO

env = gym.make("CartPole-v1")
env.reset()

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=25000)

episodes = 10

for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, reward, done, info = env.step(action)
        env.render()
        # print(reward)

env.close()

