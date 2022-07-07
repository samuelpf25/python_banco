from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []

def main() -> None:
    menu()

def menu() -> None:
    print('======================================')
    print('================ ATM =================')
    print('============= Geek Bank ==============')

    print('Selecione uma opção no menu:')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('Informe os dados do cliente: ')

    nome: str = str(input('Nome:'))
    email: str = str(input('E-mail:'))
    cpf: str = str(input('cpf:'))
    data_nascimento: str = str(input('Data de Nascimento (d/m/y):'))

    cliente: Cliente = Cliente(nome,email,cpf,data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com suceso')
    print('Dados da conta:')
    print('---------')
    print(conta)
    sleep(2)
    menu()

def registra_busca(texto) -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta:'))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input(f'Informe o valor do {texto}:'))
            if texto=='saque':
                conta.sacar(valor)
            elif texto=='depósito':
                conta.depositar(valor)
        else:
            print(f'Não foi encontrada conta com o número {numero}')
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()

def efetuar_saque() -> None:
    registra_busca('saque')


def efetuar_deposito() -> None:
    registra_busca('depósito')

def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da sua conta'))
        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('Informe o número da conta de destino'))
            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da transferência:'))
                conta_o.transferir(conta_d, valor)
            else:
                print(f'A conta de destino com número{numero_d} não foi encontrada')
        else:
            print(f'A sua conta com número {numero_o} não foi encontrada.')

    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()

def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')
        for conta in contas:
            print(conta)
            print('--------------------')
            sleep(1)
    else:
        print('Não existem contas cadastradas')
    sleep(2)
    menu()

def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c= conta
    return c

if __name__ == '__main__':
    main()