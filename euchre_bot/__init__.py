from gym.envs.registration import register

register(
    id='euchrebot-v0',
    entry_point='euchre_bot.envs:EuchreEnv',
)