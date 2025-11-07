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

import re

def verificar_tag_valida(tag):
    """
    Verifica se uma tag está no formato 'vX.Y' (ex: v1.0, v2.1).
    Retorna True se o formato for válido, caso contrário False.
    """
    padrao = r'^v\d+\.\d+$'
    
    return re.match(padrao, tag) is not None

print("Verificação de Tags Válidas:")
print(f"Tag 'v1.0': {verificar_tag_valida('v1.0')}")       # Esperado: True
print(f"Tag 'v2.15': {verificar_tag_valida('v2.15')}")     # Esperado: True
print(f"Tag 'v0.5': {verificar_tag_valida('v0.5')}")       # Esperado: True

print("\nVerificação de Tags Inválidas:")
print(f"Tag '1.0': {verificar_tag_valida('1.0')}")         # Esperado: False (falta o 'v')
print(f"Tag 'v1': {verificar_tag_valida('v1')}")           # Esperado: False (falta o '.Y')
print(f"Tag 'v1.0.1': {verificar_tag_valida('v1.0.1')}")   # Esperado: False (formato extra)
print(f"Tag 'V1.0': {verificar_tag_valida('V1.0')}")       # Esperado: False (letra maiúscula)