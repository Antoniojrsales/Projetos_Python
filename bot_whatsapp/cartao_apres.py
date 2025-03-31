import pywhatkit as kit
import time

# Lista de contatos
contatos = ["+5511985505630"]

# Mensagem personalizada
mensagem = """
            Olá! Aqui está meu cartão de apresentação:\n
            ✏️**Antonio Gomes**
            🚀*Automação de Processos & Análise de Dados com Python*
            \n📌 *Serviços:*
            📊 Análise, Visualização e Modelagem de Dados
            ⚙️ Automação de Processos e Tarefas Repetitivas
            🔗 Integração de Dados e Web Scraping
            🌐 Desenvolvimento de Sites e Aplicações Web
            \n📞 *Contato:*            
            WhatsApp: +55 8599200-6309
            E-mail: antoniogomes.junio@gmail.com"
            Portfólio: https://antoniojrsales.github.io/meu_portfolio/
            """

# Enviar mensagem para cada contato
for contato in contatos:
    kit.sendwhatmsg_instantly(contato, mensagem)
    time.sleep(5)  # Evita bloqueios por spam
