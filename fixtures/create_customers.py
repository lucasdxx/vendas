import random
import names
from vendas.core.models import Customer
from fixtures.gen_random_values import *
from fixtures.gen_names import *

customer_list = []

REPEAT = 40

for i in range(REPEAT):
    g = random.choice(['M', 'F'])
    if g == 'M':
        firstname = gen_male_first_name()['first_name']
    else:
        firstname = gen_female_first_name()['first_name']
    lastname = names.get_last_name()
    gender = g
    cpf = gen_doc()
    email = firstname[0].lower() + \
        '.' + lastname.lower() + '@example.com'
    phone = gen_phone()
    birthday = gen_timestamp() + '+00'
    Customer.objects.create(
        gender=g,
        cpf=cpf,
        firstname=firstname,
        lastname=lastname,
        email=email,
        phone=phone,
        birthday=birthday,
    )

print('%d Customers salvo com sucesso.' % REPEAT)
