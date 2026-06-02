import os


def enviar_sms(destinatario: str, mensagem: str) -> bool:

    remetente = os.getenv("SMS_REMETENTE")

    if not remetente:
        raise EnvironmentError(
            "A variável SMS_REMETENTE não foi definida."
        )

    print(
        f"[SMS] De: {remetente} | "
        f"Para: {destinatario} | "
        f"Mensagem: {mensagem}"
    )

    return True


def enviar_codigo_verificacao(
    telefone: str,
    codigo: str
) -> bool:

    mensagem = (
        f"Seu código de verificação é: {codigo}"
    )

    return enviar_sms(
        telefone,
        mensagem
    )