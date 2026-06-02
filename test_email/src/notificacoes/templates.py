def boas_vindas(nome: str) -> dict:
    return {
        "assunto": "Bem-vindo(a)!",
        "corpo": (
            f"Olá, {nome}!\n\n"
            "Seja muito bem-vindo(a) à nossa plataforma."
        )
    }


def recuperacao_senha(nome: str, link: str) -> dict:
    return {
        "assunto": "Recuperação de senha",
        "corpo": (
            f"Olá, {nome}!\n\n"
            f"Para redefinir sua senha, acesse o link:\n{link}"
        )
    }


def confirmacao_pedido(
    nome: str,
    numero_pedido: str,
    valor: float
) -> dict:

    return {
        "assunto": "Confirmação do pedido",
        "corpo": (
            f"Olá, {nome}!\n\n"
            f"Seu pedido número {numero_pedido} foi confirmado.\n"
            f"Valor total: R$ {valor:.2f}"
        )
    }