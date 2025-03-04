# 8-5 Cities
def describe_city(name, country='japan'):
    """Describes in which country the city is located."""
    print(f"\n{name.title()} is in {country.title()}.")


describe_city('osaka')
describe_city('tokyo')
describe_city('busan', 'korea')
