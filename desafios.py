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

def gerar_relatorio_final(funcoes_concluidas):
    """
    Recebe uma lista com os nomes das funções implementadas
    e retorna uma mensagem final do desafio.

    Exemplo:
    gerar_relatorio_final(["mostrar_mensagem_inicial", "listar_comandos_git_basicos"])
    ->
    "Desafio concluído! 2 funções implementadas com sucesso."
    """

    quantidade = len(funcoes_concluidas)
    
    mensagem_final = f"Desafio concluído! {quantidade} funções implementadas com sucesso."
    
    return mensagem_final


funcoes_exemplo_1 = ["mostrar_mensagem_inicial", "listar_comandos_git_basicos"]
relatorio_1 = gerar_relatorio_final(funcoes_exemplo_1)
print(f"Relatório 1 (2 funções): {relatorio_1}")


funcoes_exemplo_2 = ["funcao_a", "funcao_b", "funcao_c", "funcao_d"]
relatorio_2 = gerar_relatorio_final(funcoes_exemplo_2)
print(f"Relatório 2 (4 funções): {relatorio_2}")