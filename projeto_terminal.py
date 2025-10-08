usuarios_autorizados = [
    {"login": "admin", "senha": "123"},
]


def fazer_login():
    # Controla o acesso ao sistema. Pede um login e senha e verifica

    print("\n--- Acesso ao Sistema ---")
    while True:
        login = input("Login: ").strip()
        senha = input("Senha: ").strip()

        # Verifica se a combinação de login e senha existe na lista
        for usuario in usuarios_autorizados:
            if usuario["login"] == login and usuario["senha"] == senha:
                print(f"\n Login bem-sucedido! Bem-vindo(a), {login}.")
                return True  # Retorna True para indicar sucesso

     
        print(" Login ou senha incorretos. Tente novamente.")


def exibir_menu():
    print("\nAnálise Clínica:")
    print("1. Listar Pacientes")
    print("2. Gerenciar Estudo Clínico (Testes)")
    print("3. Gerenciar Produção Farmacêutica")
    print("4. Analisar Dados Clínicos (Concluídos)")
    print("5. Testes Concluídos")
    print("6. Incluir Ficha de Atendimento (Cadastrar Paciente)")
    print("7. Sair")


# LISTA PRINCIPAL
pacientes = []


# Função para adicionar pacientes
def adicionar_pacientes():
    nome = input("Nome do paciente: ").strip()
    nascimento = input("Data de nascimento (AAAA-MM-DD): ").strip()
    procedimento = input("Procedimento clínico: ").strip()

    novo_paciente = {
        "nome": nome,
        "nascimento": nascimento,
        "procedimento": procedimento,
        "testes": [],  # lista de testes vinculados
        "status": "pendente"
    }

    pacientes.append(novo_paciente)
    print(f"✅ Paciente '{nome}' adicionado com sucesso com status 'pendente'.")


# Função para listar pacientes
def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    print("\nPacientes cadastrados:")
    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. {p['nome']} - {p['procedimento']} - Status: {p['status']}")


def gerenciar_producao_farmaceutica():
    if not pacientes:
        print("Nenhum paciente cadastrado para associar a uma produção.")
        return

    listar_pacientes()
    try:
        escolha = int(input("\nEscolha o número do paciente para gerenciar a produção: ")) - 1
        if escolha < 0 or escolha >= len(pacientes):
            print("Opção inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    paciente = pacientes[escolha]
    print(f"\nGerenciando Produção Farmacêutica para {paciente['nome']}")

    if "medicamentos" not in paciente:
        paciente["medicamentos"] = []

    while True:
        print("\n1. Solicitar Novo Medicamento")
        print("2. Atualizar Status de Produção")
        print("3. Ver Medicamentos do Paciente")
        print("4. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome_medicamento = input("Nome do medicamento: ").strip()
            lote = input("Lote de produção: ").strip()
            novo_medicamento = {
                "nome": nome_medicamento,
                "lote": lote,
                "status": "Solicitado" 
            }
            paciente["medicamentos"].append(novo_medicamento)
            print(f"✅ Medicamento '{nome_medicamento}' (Lote: {lote}) solicitado com sucesso.")

        elif opcao == "2":
            if not paciente["medicamentos"]:
                print("Nenhum medicamento solicitado para este paciente.")
                continue

            print("\nSelecione o medicamento para atualizar o status:")
            for i, med in enumerate(paciente["medicamentos"], start=1):
                print(f"{i}. {med['nome']} (Lote: {med['lote']}) - Status atual: {med['status']}")

            try:
                m_index = int(input("Escolha o número do medicamento: ")) - 1
                if not (0 <= m_index < len(paciente["medicamentos"])):
                    print("Opção inválida.")
                    continue

                print("\nSelecione o novo status:")
                status_disponiveis = ["Em produção", "Controle de Qualidade", "Disponível", "Administrado"]
                for i, status in enumerate(status_disponiveis, start=1):
                    print(f"{i}. {status}")

                s_index = int(input("Escolha o número do novo status: ")) - 1
                if 0 <= s_index < len(status_disponiveis):
                    paciente["medicamentos"][m_index]["status"] = status_disponiveis[s_index]
                    print("✅ Status atualizado com sucesso!")
                else:
                    print("Opção de status inválida.")

            except ValueError:
                print("Entrada inválida.")

        elif opcao == "3":
            if not paciente["medicamentos"]:
                print("\nNenhum medicamento associado a este paciente.")
            else:
                print(f"\n--- Medicamentos de {paciente['nome']} ---")
                for med in paciente["medicamentos"]:
                    print(f"- Nome: {med['nome']} | Lote: {med['lote']} | Status: {med['status']}")

        elif opcao == "4":
            break
        else:
            print("Opção inválida.")
    
        


# Gerenciar estudo clínico (adicionar testes e concluir)
def gerenciar_estudo():
    if not pacientes:
        print("Nenhum paciente cadastrado ainda.")
        return

    listar_pacientes()
    try:
        escolha = int(input("\nEscolha o número do paciente para gerenciar: ")) - 1
        if escolha < 0 or escolha >= len(pacientes):
            print("Opção inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    paciente = pacientes[escolha]
    print(f"\nGerenciando testes de {paciente['nome']}")

    while True:
        print("\n1. Adicionar teste")
        print("2. Marcar teste como concluído")
        print("3. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome_teste = input("Nome do teste: ").strip()
            observacao = input("Observação: ").strip()
            paciente["testes"].append({"nome": nome_teste, "observacao": observacao, "concluido": False})
            print(f"Teste '{nome_teste}' adicionado com sucesso.")

        elif opcao == "2":
            if not paciente["testes"]:
                print("Nenhum teste cadastrado ainda.")
                continue

            for i, t in enumerate(paciente["testes"], start=1):
                status = "✅" if t["concluido"] else "⏳"
                print(f"{i}. {t['nome']} - {status}")

            try:
                t_index = int(input("Escolha o número do teste para marcar como concluído: ")) - 1
                if 0 <= t_index < len(paciente["testes"]):
                    paciente["testes"][t_index]["concluido"] = True
                    paciente["status"] = "concluído"
                    print(f"Teste '{paciente['testes'][t_index]['nome']}' concluído com sucesso!")
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Entrada inválida.")

        elif opcao == "3":
            break
        else:
            print("Opção inválida.")


# Analisar dados clínicos — apenas os concluídos
def analisar_dados_clinicos():
    concluidos = [p for p in pacientes if p["status"] == "concluído"]
    if not concluidos:
        print("Nenhum paciente com dados clínicos concluídos.")
        return

    print("\n=== Pacientes com dados concluídos ===")
    for p in concluidos:
        print(f"- {p['nome']} | Procedimento: {p['procedimento']}")


# Testes concluídos
def testes():
    pacientes_concluidos = [
        p for p in pacientes if any(t.get('concluido') for t in p.get('testes', []))
    ]

    if not pacientes_concluidos:
        print("Nenhum paciente possui testes concluídos ainda.")
        return

    print("\n=== Pacientes com Testes Concluídos ===")
    for i, p in enumerate(pacientes_concluidos, start=1):
        print(f"{i}. {p['nome']} — Status: {p['status']} — Procedimento: {p['procedimento']}")

    try:
        escolha = int(input("\nDigite o número do paciente para ver os testes: ")) - 1
        if escolha < 0 or escolha >= len(pacientes_concluidos):
            print("Opção inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    paciente = pacientes_concluidos[escolha]
    print(f"\n=== Testes do paciente {paciente['nome']} ===")

    for t in paciente.get('testes', []):
        status = "✅ Concluído" if t.get('concluido') else "⏳ Pendente"
        print(f"- {t.get('nome')}: {status}")
        if t.get('observacao'):
            print(f"  Observação: {t['observacao']}")



fazer_login()
# Programa principal
while True:
    exibir_menu()
    try:
        opcao = int(input("\nSelecione uma opção: "))

        if opcao == 1:
            listar_pacientes()
        elif opcao == 2:
            gerenciar_estudo()
        elif opcao == 3:  
           gerenciar_producao_farmaceutica()
        elif opcao == 4:
            analisar_dados_clinicos()
        elif opcao == 5:
            testes()
        elif opcao == 6:
            adicionar_pacientes()
        elif opcao == 7:
            print("Encerrando o programa. Excelente dia!")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite o número da opção.")
