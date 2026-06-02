from src.notificacoes.service import enviar_email


def test_enviar_email_retorna_true():
    
    resultado = enviar_email(
        "teste@email.com",
        "Teste",
        "Mensagem teste"
    )

    assert resultado is True