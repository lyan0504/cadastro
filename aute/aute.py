usuarios = {
    'admin': {'senha': 'admin123', 'permissoes': ['admin']},
    'user1': {'senha': 'user123', 'permissoes': ['user']},
    'user2': {'senha': 'user456', 'permissoes': ['user']}
}

def autenticar(usuario, senha):
    if usuario in usuarios and usuarios[usuario]['senha'] == senha:
        return True
    else:
        return False

def verificar_permissao(usuario, permissao_requerida):
    if permissao_requerida in usuarios[usuario]['permissoes']:
        return True
    else:
        return False

def main():
    print("Bem-vindo ao sistema de autenticação e autorização!")

    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if autenticar(usuario, senha):
        print("Autenticação bem-sucedida!")

        permissao_requerida = input("Digite a permissão que deseja verificar (ex: 'admin' ou 'user'): ")

        if verificar_permissao(usuario, permissao_requerida):
            print("Autorizado! Você tem acesso ao recurso.")
        else:
            print("Não autorizado! Você não tem acesso ao recurso.")
    else:
        print("Autenticação falhou! Usuário ou senha incorretos.")

if __name__ == "__main__":
    main()
    