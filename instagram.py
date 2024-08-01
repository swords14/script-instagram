import instaloader

# Crie uma instância do Instaloader
L = instaloader.Instaloader()

# Insira suas credenciais diretamente no script
username = "seu_usuario"  # Substitua pelo seu nome de usuário
password = "sua_senha"    # Substitua pela sua senha

try:
    # Tente fazer login
    L.login(username, password)
except instaloader.exceptions.TwoFactorAuthRequiredException:
    # Se a autenticação de dois fatores for necessária
    two_factor_code = input("Digite o código de autenticação de dois fatores: ")
    L.two_factor_login(two_factor_code)

# Obtenha o perfil do usuário
profile = instaloader.Profile.from_username(L.context, username)

# Obtenha a lista de contas que você está seguindo
followees = [followee for followee in profile.get_followees()]

# Remova as contas que você está seguindo
for followee in followees:
    print(f"Deixando de seguir: {followee.username}")
    L.context.log("Deixando de seguir: " + followee.username)  # Log para depuração
    L.context.do_unfollow(followee)  # Método correto para deixar de seguir

print("Deixar de seguir contas concluído!")