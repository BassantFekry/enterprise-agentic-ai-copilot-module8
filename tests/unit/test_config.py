
from app.core.config import Settings


def test_environment_variables_override_defaults(monkeypatch):
    monkeypatch.setenv("APP_NAME", "Test App From Env")
    monkeypatch.setenv("ENVIRONMENT", "testing")
    monkeypatch.setenv("OPENAI_API_KEY", "")

    settings = Settings(_env_file=None)

    assert settings.app_name == "Test App From Env"
    assert settings.environment == "testing"
    assert settings.openai_api_key == ""
