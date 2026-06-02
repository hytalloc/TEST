from  src.notificacoes.service import enviar_boas_vindas


def test_enviar_boas_vindas():
    resultado = enviar_boas_vindas(
        "teste@email.com",
        "João"
    )

    assert resultado is True