import random

from src.notificacoes import templates
from src.notificacoes.service import enviar_email
from src.notificacoes.sms import enviar_codigo_verificacao


class GerenciadorDeNotificacoes:

    def __init__(self):
        self.historico = []

    def notificar_usuario(
        self,
        nome: str,
        email: str,
        telefone: str
    ) -> dict:

        template = templates.boas_vindas(nome)

        email_enviado = enviar_email(
            email,
            template["assunto"],
            template["corpo"]
        )

        codigo = str(
            random.randint(100000, 999999)
        )

        sms_enviado = enviar_codigo_verificacao(
            telefone,
            codigo
        )

        resultado = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "email_enviado": email_enviado,
            "sms_enviado": sms_enviado
        }

        self.historico.append(resultado)

        return resultado

    def reenviar_falhas(self) -> int:

        reenvios = 0

        for item in self.historico:

            if item["email_enviado"] is False:
                item["email_enviado"] = True
                reenvios += 1

            if item["sms_enviado"] is False:
                item["sms_enviado"] = True
                reenvios += 1

        return reenvios

    def resumo(self) -> dict:

        total = len(self.historico)

        emails_enviados = sum(
            1 for item in self.historico
            if item["email_enviado"]
        )

        sms_enviados = sum(
            1 for item in self.historico
            if item["sms_enviado"]
        )

        return {
            "total": total,
            "emails_enviados": emails_enviados,
            "sms_enviados": sms_enviados,
            "falhas_email": total - emails_enviados,
            "falhas_sms": total - sms_enviados
        }