# Leia uma string representando um e-mail e determine se ela possui o formato básico de um endereço eletrônico

try:
    email = input('Digite seu email: ')

    if ' ' in email:
        print('Email inserido inválido')

    elif '@' in email and '.' in email and email.split('.')[-1].isalpha():
        print('Email válido')
    else:
        print('Email inválido')

except ValueError:
    print('Email inválido')
    
except Exception:
    print('Email inválido')