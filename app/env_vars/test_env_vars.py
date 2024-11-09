from app.env_vars import EnvVars
import pytest

def test_get_env_variable():
    environment_vars = EnvVars()
    # Retrieve env var
    max = environment_vars.get_environment_variable('HIST_MAX')
    assert max == 5