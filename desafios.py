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

def mostrar_mensagem_inicial():
    """
    Exibe uma mensagem de boas-vindas ao desafio.
    Retorno esperado: string com a mensagem "Bem-vindo ao Desafio de Git!"
    """
    print("\n")
    print("1º DESAFIO CONCLUÍDO")
    print("\n")
    
    mensagem = "Bem-vindo ao Desafio de Git!"
    print(mensagem) 
    return mensagem

mensagem_de_retorno = mostrar_mensagem_inicial()

print(f"\nO valor retornado é: {mensagem_de_retorno}\n") 

print("=================================================================================================")
print("\n")

print("2º DESAFIO CONCLUÍDO")
print("\n")

def listar_comandos_git_basicos():
    """
    Retorna uma lista com os principais comandos básicos do Git.
    Exemplo de saída:
    ["git init", "git add", "git commit", "git status", "git push"]
    """
    
    comandos_basicos = [
        "git init --> inicia o git",    
        "git add ---> prepara o arquivo para fazer o commiit (stage area)",   
        "git commit -> faz o commit", 
        "git status -> lista o status se tem algum arquivo para adicionar ou fazer commit",  
        "git push ---> envia o repositório para o git hub",    
        "git pull ---> puxa o diretório",    
    ]
    
    return comandos_basicos

# Exemplo de uso da função:
lista_de_comandos = listar_comandos_git_basicos()
print("Comandos Básicos do Git:")
for comando in lista_de_comandos:
    print(f"- {comando}\n")

print("=================================================================================================")
print("\n")

print("3º DESAFIO CONCLUÍDO")
print("\n")

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
print(f'Função "listar_comandos_git_basicos" -> Commit: "{mensagem_1}\n"')

mensagem_2 = criar_mensagem_commit("mostrar_mensagem_inicial")
print(f'Função "mostrar_mensagem_inicial" -> Commit: "{mensagem_2}\n"')

print("===================================================================================================")
print("\n")

print("4º DESAFIO CONCLUÍDO")
print("\n")

import re

def verificar_tag_valida(tag):
    """
    Verifica se uma tag está no formato 'vX.Y' (ex: v1.0, v2.1).
    Retorna True se o formato for válido, caso contrário False.
    """
    padrao = r'^v\d+\.\d+$'
    
    return re.match(padrao, tag) is not None

print("Verificação de Tags Válidas:\n")
print(f"Tag 'v1.0': {verificar_tag_valida('v1.0')}")       # Esperado: True
print(f"Tag 'v2.15': {verificar_tag_valida('v2.15')}")     # Esperado: True
print(f"Tag 'v0.5': {verificar_tag_valida('v0.5')}")       # Esperado: True

print("\nVerificação de Tags Inválidas:\n")
print(f"Tag '1.0': {verificar_tag_valida('1.0')}")         # Esperado: False (falta o 'v')
print(f"Tag 'v1': {verificar_tag_valida('v1')}")           # Esperado: False (falta o '.Y')
print(f"Tag 'v1.0.1': {verificar_tag_valida('v1.0.1')}")   # Esperado: False (formato extra)
print(f"Tag 'V1.0': {verificar_tag_valida('V1.0')}\n")       # Esperado: False (letra maiúscula)

print("===================================================================================================")
print("\n")

print("5º DESAFIO CONCLUÍDO")
print("\n")

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
print(f"Relatório 1 (2 funções): {relatorio_1}\n")


funcoes_exemplo_2 = ["funcao_a", "funcao_b", "funcao_c", "funcao_d"]
relatorio_2 = gerar_relatorio_final(funcoes_exemplo_2)
print(f"Relatório 2 (4 funções): {relatorio_2}\n")

print("===================================================================================================")
print("\n")