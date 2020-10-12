# 8.3 - 8.4
def make_shirt(size='L', text='I love Python'):
    print(f"\nPrint one shirt with text - {text}. Size is {size.upper()}.")
make_shirt('XL', 'LOL')
make_shirt()

# 8.5
def describe_city(city, country = 'USA'):
    print(f'\n{city.title()} is in {country.title()}.')
describe_city('dallas')
describe_city('moscow', 'russia')

