import pytest

from src.notificacoes.sms import (
    enviar_sms,
    enviar_codigo_verificacao
)


def test_enviar_sms_sucesso(monkeypatch):

    monkeypatch.setenv(
        "SMS_REMETENTE",
        "+551199999999"
    )

    resultado = enviar_sms(
        "+558899999999",
        "Teste SMS"
    )

    assert resultado is True


def test_sem_remetente_levanta_erro(
    monkeypatch
):

    monkeypatch.delenv(
        "SMS_REMETENTE",
        raising=False
    )

    with pytest.raises(EnvironmentError):

        enviar_sms(
            "+558899999999",
            "Teste"
        )


def test_enviar_codigo_verificacao(
    mocker
):

    mock_sms = mocker.patch(
        "src.notificacoes.sms.enviar_sms",
        return_value=True
    )

    enviar_codigo_verificacao(
        "+558899999999",
        "123456"
    )

    mock_sms.assert_called_once_with(
        "+558899999999",
        "Seu código de verificação é: 123456"
    )