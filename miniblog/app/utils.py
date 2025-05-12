from functools import wraps
from flask import session, redirect, url_for
from langchain_openai import OpenAIEmbeddings, ChatOpenAI, OpenAI
import logging
from langchain_openai import ChatOpenAI

def autenticar_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper

def openai_request(contexto: list[str] = [""], historico: list[dict] = [], ids: list[str] = [""], metadatas: list[list[dict]] = []) -> dict:
    """
    Faz uma única requisição ao modelo GPT para responder a perguntas relacionadas à pedagogia de robótica.

    Args:
        contexto : Lista de contextos.
        historico : Histórico de mensagens.
        ids : Lista de IDs dos documentos.
        metadatas : Lista de metadados.

    Returns:
        Resposta gerada pelo modelo GPT em relação à pergunta, contendo o conteúdo e metadados da resposta.
    """
    try:
        logging.info("Iniciando interação com o modelo GPT.")
        
        # Configuração do modelo
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.2,
            max_tokens=None,
            timeout=None,
            max_retries=3,
            frequency_penalty=0.2
        )

        # Preparação das mensagens
        messages = prepare_messages(contexto=contexto, 
                                    historico=historico, 
                                    ids=ids, 
                                    metadatas=metadatas)

        # Chamada ao modelo
        ai_msg = llm.invoke(messages)
        if not ai_msg or not ai_msg.content:
            raise ValueError("Resposta do modelo está vazia ou inválida.")

        response_dict = {
            "content": ai_msg.content,
            "response_metadata": ai_msg.response_metadata,
        }
        
        logging.info("Interação com o modelo concluída com sucesso.")
        
        return response_dict
    except Exception as e:
        logging.error(f"Erro durante interação com o modelo GPT: {e}")
        return {"error": f"Ocorreu um erro inesperado: {str(e)}"}
    
def prepare_messages(contexto: list[str], metadatas: list[dict], ids: list[str], historico: list[dict]) -> list[tuple[str, str]]:
    """
    Prepara mensagens para o modelo sem usar funções externas.

    Args:
        contexto : Lista de contextos.
        ids : Lista de IDs dos documentos.
        historico : Histórico de mensagens.
        metadatas : Lista de metadados.

    Returns:
        Lista de mensagens formatadas.
    """
    try:
        # Combina os contextos em uma única string
        prompt_contexto = "\n".join(contexto)

        # Formata os IDs em uma string
        ids_formatados = ", ".join(ids)

        # Formata os metadados em uma string
        metadados_formatados = "\n".join(
            [f"reference: {meta.get('reference', 'N/A')}" for meta in metadatas]
        )

        # Agrupa as informações em um formato de texto
        info = (
            f"Contextos:\n{prompt_contexto}\n\n"
            f"IDs:\n{ids_formatados}\n\n"
            f"Metadados:\n{metadados_formatados}\n"
        )

        logging.info(f'INFORMAÇÃO: {info}\n')
        logging.info("Formatando mensagens para o modelo...")

        system_prompt = (
            "Você é um assistente especializado em pedagogia para robótica, projetado exclusivamente para ajudar pedagogos com dúvidas "
            "e questões relacionadas ao ensino e à prática de robótica para crianças e adolescentes. Sua função é fornecer informações "
            "precisas, esclarecer conceitos, sugerir atividades pedagógicas e oferecer suporte técnico dentro deste contexto. Não use "
            "caracteres especiais, como * ou _ na resposta, apenas use o texto puro.\n\n"
            "### CONTEXTO FORNECIDO ###\n"
            f"{info}\n"
        )

        messages = [("system", system_prompt)]

        for msg in historico[:-1]:
            messages.append((msg['role'], msg['content']))

        if historico:
            messages.append((historico[-1]['role'], historico[-1]['content']))

        logging.info("Mensagens preparadas com sucesso.")
        return messages

    except Exception as e:
        logging.error(f"Erro ao preparar mensagens: {e}")
        return []
