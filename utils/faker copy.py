from faker import Faker


fake = Faker()

def get_login_faker(num_casos=5):

    lista = [] 

    for _ in range(num_casos):
        username = fake.user_name()
        password = fake.password(length=12)
        login_booleano = fake.boolean(chance_of_getting_true=70)

        lista.append((username, password, login_booleano))

    return lista


