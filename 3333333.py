favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# for name, language in favorite_languages.items():
#    print(f"{name.title()}'s favorite language is {language.title()}")
opros = ['jen', 'qqq', 'www', 'eee', 'edward', 'fff', 'sarah']
for name in opros:
    if name not in favorite_languages:
        print(f"{name.title()}, proidi please opros!")
    else:
        print(f"{name.title()}, thx, no you yge proshel opros")
