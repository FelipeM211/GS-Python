import json
import sys

def carregar_dados(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        dados = json.load(file)
        if "Candidatos" in dados:
            return dados["Candidatos"]
        elif "Empresas" in dados:
            return dados["Empresas"]
        else:
            return []

def salvar_dados(arquivo, dados):
    if 'candidatos' in arquivo.lower():
        estrutura = {"Candidatos": dados}
    else:
        estrutura = {"Empresas": dados}
    with open(arquivo, 'w', encoding='utf-8') as file:
        json.dump(estrutura, file, indent=4, ensure_ascii=False)

def verificar_login(tipo_usuario, email, senha):
    arquivo = 'candidatos.json' if tipo_usuario == 'candidato' else 'empresas.json'
    dados = carregar_dados(arquivo)
    for registro in dados:
        if registro.get('email') == email and registro.get('senha') == senha:
            return True
    return False

def email_existe(arquivo, email):
    dados = carregar_dados(arquivo)
    return any(registro.get('email') == email for registro in dados)

def cadastrar_candidato():
    print("\n--- Cadastro de Candidato ---")
    while True:
        nome = input("Nome completo: ").strip()
        idade = input("Idade: ").strip()
        profissao = input("Profissão: ").strip()
        email = input("E-mail: ").strip()
        senha = input("Senha (mínimo 4 caracteres): ").strip()

        if not nome or not idade or not profissao or not email or not senha:
            print("Nenhum campo pode estar vazio.")
            continue
        if not idade.isdigit():
            print("A idade deve ser um número inteiro.")
            continue
        if len(senha) < 4:
            print("A senha deve ter pelo menos 4 caracteres.")
            continue
        if email_existe('candidatos.json', email):
            print("E-mail já cadastrado.")
            continue

        candidatos = carregar_dados('candidatos.json')
        novo = {
            "nome": nome,
            "idade": int(idade),
            "profissao": profissao,
            "email": email,
            "senha": senha
        }
        candidatos.append(novo)
        salvar_dados('candidatos.json', candidatos)
        print("Cadastro concluído com sucesso!")
        return 'candidato'

def cadastrar_empresa():
    print("\n--- Cadastro de Empresa ---")
    while True:
        nome = input("Nome da empresa: ").strip()
        area = input("Área de atuação: ").strip()
        local = input("Localização: ").strip()
        email = input("E-mail: ").strip()
        senha = input("Senha (mínimo 4 caracteres): ").strip()

        if not nome or not area or not local or not email or not senha:
            print("Nenhum campo pode estar vazio.")
            continue
        if len(senha) < 4:
            print("A senha deve ter pelo menos 4 caracteres.")
            continue
        if email_existe('empresas.json', email):
            print("E-mail já cadastrado.")
            continue

        empresas = carregar_dados('empresas.json')
        nova = {
            "nome": nome,
            "area": area,
            "local": local,
            "email": email,
            "senha": senha
        }
        empresas.append(nova)
        salvar_dados('empresas.json', empresas)
        print("Empresa cadastrada com sucesso!")
        return 'empresa'

def fluxo_candidato():
    empresas = carregar_dados('empresas.json')
    if not empresas:
        print("Nenhuma empresa cadastrada.")
        return

    while True:
        print("\nEmpresas disponíveis:")
        for i, e in enumerate(empresas, start=1):
            print(f"{i}. {e['nome']} ({e['area']} - {e['local']})")

        try:
            escolha = int(input("Escolha o número da empresa para se candidatar: "))
            if 1 <= escolha <= len(empresas):
                empresa_escolhida = empresas[escolha - 1]
                print(f"\nVocê se candidatou à empresa {empresa_escolhida['nome']} com sucesso!")
            else:
                print("Escolha inválida.")
                continue
        except ValueError:
            print("Digite um número válido.")
            continue

        continuar = input("Deseja se candidatar a mais uma empresa? (s/n): ").strip().lower()
        if continuar != 's':
            print("Obrigado por usar o Provenn!")
            sys.exit()


def fluxo_empresa():
    while True:
        candidatos = carregar_dados('candidatos.json')
        if not candidatos:
            print("Nenhum candidato cadastrado.")
            return

        print("\nCandidatos disponíveis:")
        for i, c in enumerate(candidatos, start=1):
            print(f"{i}. {c['nome']}, {c['profissao']} ({c['idade']} anos)")

        escolha = input("\nEscolha o número do candidato para ver mais informações sobre (ou '0' para voltar): ").strip()
        if escolha == '0':
            return
        if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(candidatos):
            print("Escolha inválida.")
            continue

        candidato = candidatos[int(escolha) - 1]
        print("\n--- Detalhes do Candidato ---")
        print(f"Nome: {candidato['nome']}")
        print(f"Idade: {candidato['idade']}")
        print(f"Profissão: {candidato['profissao']}")
        print(f"E-mail: {candidato['email']}")

        confirmacao = input("\nDeseja enviar proposta para este candidato? (s/n): ").strip().lower()
        if confirmacao == 's':
            print(f"Proposta enviada para {candidato['nome']} com sucesso!")

        continuar = input("\nDeseja visualizar mais algum candidato? (s/n): ").strip().lower()
        if continuar != 's':
            print("Obrigado por usar o Provenn.")
            sys.exit()



def tela_login():
    print("\n=== Bem-vindo ao Provenn ===")
    while True:
        print("\n1. Fazer login\n2. Criar nova conta\n3. Sair")
        escolha = input("Escolha: ").strip()

        if escolha == '1':
            tipo = input("Login como candidato ou empresa? (c/e): ").strip().lower()
            if tipo not in ['c', 'e']:
                print("Escolha inválida.")
                continue
            tipo_usuario = 'candidato' if tipo == 'c' else 'empresa'
            email = input("E-mail: ").strip()
            senha = input("Senha: ").strip()
            if verificar_login(tipo_usuario, email, senha):
                print("Login realizado com sucesso!")
                return tipo_usuario
            else:
                print("Login incorreto, tente novamente.")

        elif escolha == '2':
            tipo = input("Deseja criar conta como candidato ou empresa? (c/e): ").strip().lower()
            if tipo == 'c':
                return cadastrar_candidato()
            elif tipo == 'e':
                return cadastrar_empresa()
            else:
                print("Escolha inválida.")

        elif escolha == '3':
            print("Encerrando o sistema Provenn.")
            sys.exit()

        else:
            print("Opção inválida.")

def menu_principal(tipo_usuario):
    print("\n--- SISTEMA DE CONTRATAÇÃO PROVENN ---")
    while True:
        if tipo_usuario == 'candidato':
            print("\n1. Quero ser contratado\n2. Sair")
            opcao = input("Escolha: ").strip()
            if opcao == '1':
                fluxo_candidato()
            elif opcao == '2':
                print("Obrigado por usar o Provenn.")
                sys.exit()
            else:
                print("Opção não disponível para este tipo de usuário.")
        elif tipo_usuario == 'empresa':
            print("\n1. Quero contratar\n2. Sair")
            opcao = input("Escolha: ").strip()
            if opcao == '1':
                fluxo_empresa()
            elif opcao == '2':
                print("Obrigado por usar o Provenn.")
                sys.exit()
            else:
                print("Opção não disponível para este tipo de usuário.")

if __name__ == "__main__":
    tipo_usuario = tela_login()
    if not tipo_usuario:
        sys.exit()
    menu_principal(tipo_usuario)
