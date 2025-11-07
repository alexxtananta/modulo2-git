"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Request.
- Repetir o processo até concluir todas as funções.

Boa sorte e bons commits! 🚀
"""

def criar_mensagem_commit(funcao_nome):
    """
    Recebe o nome de uma função e retorna uma mensagem de commit padronizada.
    Exemplo:
    criar_mensagem_commit("listar_comandos_git_basicos") ->
    "Implementa função listar_comandos_git_basicos"
    """
    
    mensagem_commit = f"Implementa função {funcao_nome}"
    
    return mensagem_commit

mensagem_1 = criar_mensagem_commit("listar_comandos_git_basicos")
print(f'Função "listar_comandos_git_basicos" -> Commit: "{mensagem_1}"')

mensagem_2 = criar_mensagem_commit("mostrar_mensagem_inicial")
print(f'Função "mostrar_mensagem_inicial" -> Commit: "{mensagem_2}"')
