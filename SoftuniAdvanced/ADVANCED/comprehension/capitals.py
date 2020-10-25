countries = [x for x in input().split(', ')]
capitals = [x for x in input().split(', ')]
result = list(zip(countries, capitals))
[print(f'{x[0]} -> {x[1]}') for x in result]