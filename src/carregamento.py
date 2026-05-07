import time
import random
from tqdm import tqdm
from colorama import Fore, Style

mensagens = [
    "Conectando ao banco de dados...",
    "Carregando módulos...",
    "Validando credenciais...",
    "Inicializando cache...",
    "Sincronizando dados...",
    "Executando rotina de verificação...",
    "Inicializando serviços principais...",
    "Carregando módulos de configuração...",
    "Validando credenciais de acesso...",
    "Conectando ao banco de dados...",
    "Estabelecendo conexão com servidor remoto...",
    "Verificando dependências do sistema...",
    "Cache atualizado com sucesso.",
    "Mensagem enviada para a fila de eventos.",
    "Resposta recebida da API de pagamentos.",
    "Executando rotina de verificação de integridade...",
    "Consulta ao banco concluída em 0.23s.",
    "Sincronizando dados com servidor central...",
    "Ajustando parâmetros internos...",
    "Preparando café para os servidores...",
    "Etapa 3/5 concluída.",
    "Rotina encerrada sem erros.",
    "Aviso: tempo de resposta acima do esperado.",
    "Erro crítico detectado no módulo de autenticação.",
    "Sessão do usuário validada.",
    
]

barra_cores = random.choice([
    # 'red',
    'yellow',
    'green',
    'cyan',
    'blue',
    'magenta',
    'white',
])

def tela_de_carregamento1(barraCor):
    total = 50
    for i in tqdm(range(total), ncols=80, colour=barraCor):
        time.sleep(0.3)
        msg = random.choice(mensagens)

        # Escolhe cor conforme o progresso
        if i < total * 0.3:
            cor = Fore.YELLOW   # início: atenção
        elif i < total * 0.7:
            cor = Fore.CYAN     # meio: neutro/tecnológico
        else:
            cor = Fore.GREEN    # final: sucesso

        tqdm.write(cor + f"[process] {msg}" + Style.RESET_ALL)
        
def tela_de_carregamento2(barraCor):
    for i in tqdm(range(45), desc="Carregando", ncols=80, colour=barraCor):
        time.sleep(0.3)
        msg = random.choice(mensagens)
        # Usa tqdm.write para não quebrar a barra
        tqdm.write(Fore.CYAN + f"[executando] {msg}")

if __name__ == "__main__":
    for i in range(100):
        tela_de_carregamento1(barra_cores)
        tela_de_carregamento2(barra_cores)
        print(Fore.GREEN + "Processo concluído!" + Style.RESET_ALL)
