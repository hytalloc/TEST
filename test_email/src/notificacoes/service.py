import logging
import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logger = logging.getLogger(__name__)


def enviar_email(destinatario: str, assunto: str, corpo: str) -> bool:
    host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    porta = int(os.getenv("SMTP_PORT", "587"))

    usuario = os.getenv("SMTP_USER")
    senha = os.getenv("SMTP_PASS")

    if not usuario or not senha:
        raise EnvironmentError(
            "SMTP_USER e SMTP_PASS sao obrigatorios"
        )

    msg = MIMEMultipart()
    msg["Subject"] = assunto
    msg["From"] = usuario
    msg["To"] = destinatario

    msg.attach(MIMEText(corpo, "plain"))

    with smtplib.SMTP(host, porta) as server:
        server.starttls()
        server.login(usuario, senha)
        server.send_message(msg)

    logger.info(f"E-mail enviado para {destinatario}")
    return True


def enviar_boas_vindas(email: str, nome: str) -> bool:
    return enviar_email(
        destinatario=email,
        assunto="Boas-vindas",
        corpo=f"Olá {nome}, seja bem-vindo!"
    )