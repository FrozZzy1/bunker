from environs import Env

env = Env()
env.read_env()

DATABASE_URL = env.str('DATABASE_URL')
