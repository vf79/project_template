def test_create_app(client):
    assert client.app.version == "0.1.0"


def test_config(settings):
    settings.setenv("production")
    assert settings.ambiente == "producao"
    settings.setenv("development")
    assert settings.ambiente == "desenvolvimento"
    settings.setenv("testing")
    assert settings.ambiente == "testes"
