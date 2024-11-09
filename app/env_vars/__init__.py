from dotenv import load_dotenv
import os

class EnvVars:
    def __init__(self):
        load_dotenv()
        self.vars = self.load_environment_variables()
    
    def load_environment_variables(self):
        vars = {key: value for key, value in os.environ.items()}
        return vars

    def get_environment_variable(self, env_var: str):
        return self.vars.get(env_var, None)