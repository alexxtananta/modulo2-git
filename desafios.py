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

print("==================================================================================")
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

print("==================================================================================")
print("\n")



