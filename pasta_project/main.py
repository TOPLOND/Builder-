from pasta_factory import PastaFactory


pasta = PastaFactory.create_pasta("Carbonara")
print(f"Тип пасты: {pasta.get_type()}")
print(f"Соус: {pasta.get_sauce()}")
print(f"Начинка: {pasta.get_topping()}")
print(f"Добавки: {pasta.get_additives()}")