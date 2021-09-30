import requests

# Verificar versión
def verificar_version():
    url_last_readme = 'https://github.com/JonaRanto/AutoUpdateTestApp/raw/main/README.md'
    page = requests.get(url_last_readme)
    last_version = page.text.split('\n')[1].split('=')[1]
    my_readme = open('README.md', 'r')
    my_version = my_readme.read().split('\n')[1].split('=')[1]
    resp = False
    if my_version == last_version: resp = True
    return resp
if not verificar_version():
    print('La aplicación está desactualziada :C')
else:
    print('La aplicación está actualziada ^^')