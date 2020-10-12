#6.5
rivers = {
    'nile': 'egypt',
    'volga': 'russia',
    'dnepr': 'ukraine',
    'amazon': 'brazil',
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())
#6.6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
#for name, language in favorite_languages.items():
#    print(f"{name.title()}'s favorite language is {language.title()}")
opros = ['jen', 'qqq', 'www', 'eee', 'edward', 'fff', 'sarah']
for name in opros:
    if name not in favorite_languages:
        print(f"{name.title()}, proidi please opros!")
    else:
        print(f"{name.title()}, thx, but you yge proshel opros")
