from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse, HttpResponse

def home(request, ):
    
    return HttpResponse('<h1>Bienvenido a  my Pokémon app, escriba /types para ver los tipos de pokemon </h1>' )


def get_pokemon_types(request):
    response = requests.get('https://pokeapi.co/api/v2/type')
    data = response.json()
    types = []
    for result in data['results']:
        type = {'name': result['name'], 'url': result['url']}
        response = requests.get(type['url'])
        data = response.json()
        if data['pokemon']:
            pokemon_url = data['pokemon'][0]['pokemon']['url']
            response = requests.get(pokemon_url)
            data = response.json()
            type['image_url'] = data['sprites']['front_default']
        types.append(type)
    return render(request, 'pokemon_types.html', {'types': types})



def get_pokemon_by_type(request, type_name):
    response = requests.get(f'https://pokeapi.co/api/v2/type/{type_name}')
    data = response.json()
    pokemon = [{'name': result['pokemon']['name'], 'url': result['pokemon']['url']} for result in data['pokemon']]
    html = '<ul>'
    for p in pokemon:
        response = requests.get(p['url'])
        data = response.json()
        image_url = data['sprites']['front_default']
        html += f'<li><a href="/pokemon/details/{p["name"]}"><img src="{image_url}" alt="{p["name"]}" width="50" height="50">{p["name"]}</a></li>'
    html += '</ul>'
    return HttpResponse(html)

def get_pokemon_details(request, pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    data = response.json()
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    types = [type['type']['name'] for type in data['types']]
    image_url = data['sprites']['front_default']
    html = f'<h1>{pokemon_name}</h1>'
    html += f'<img src="{image_url}" alt="{pokemon_name}" width="200" height="200">'
    html += '<h2>Abilities</h2><ul>'
    for ability in abilities:
        html += f'<li>{ability}</li>'
    html += '</ul>'
    html += '<h2>Types</h2><ul>'
    for type in types:
        html += f'<li>{type}</li>'
    html += '</ul>'
    return HttpResponse(html)