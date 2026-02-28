import  logging

logging.basicConfig(
    filename="diagnostico.log",
    level=logging.INFO,
    format= "%(asctime)s - %(message)s"
)


def salvar_log(mensagem):
    logging.info(mensagem)

