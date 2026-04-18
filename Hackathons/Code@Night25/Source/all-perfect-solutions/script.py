import subprocess
import glob
import os

'''
Esse script executa um arquivo Python com entradas de teste e compara a saída com os resultados esperados.
O script deve ser chamado com o nome da letra do arquivo Python que deseja testar.
O arquivo Python deve estar no mesmo diretório que este script e deve ter o nome da letra em maiúsculo (ex: A.py).
Os arquivos de entrada devem estar na pasta "input" e seguir o padrão "letra_numero" (ex: A_1).
Os arquivos de saída esperados devem estar na pasta "output" e seguir o mesmo padrão (ex: A_1).
'''

# Caminho absoluto da pasta onde está o script
base_dir = os.path.dirname(os.path.abspath(__file__))

letra = input("Digite uma letra: ").strip().upper()
py_file = os.path.join(base_dir, f"codes/{letra}.py")
input_files = sorted(glob.glob(os.path.join(base_dir, f"input/{letra}/{letra}_*")))

all_passed = True

for in_file in input_files:
    # Gera o nome do arquivo de output correspondente
    out_file = in_file.replace(os.path.join("input"), os.path.join("output"))

    # Lê o input do arquivo txt
    with open(in_file, "r") as f:
        input_data = f.read()

    # Executa o script Python com o input do arquivo
    result = subprocess.run(
        ["python3", py_file],
        input=input_data,
        text=True,
        capture_output=True
    )

    # Lê o output esperado
    with open(out_file, "r") as f:
        expected_output = f.read()

    if result.stdout.strip() != expected_output.strip():
        print(f"falhou: {in_file}")
        all_passed = False

if all_passed:
    print("\nTodos os casos passaram! 🎉")
else:
    print("\nAlguns casos falharam. ❌")