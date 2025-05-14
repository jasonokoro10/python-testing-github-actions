from Prova_escrita_05 import *
import pytest

# Copiem la "base de dades" de la biblioteca, ja que no es detecta la variable, si no la definim en aquest arxiu
biblioteca = [
    {
        "llibre": "El Quixot",
        "autor": "Cervantes",
        "categoria": "novel·la",
        "prestecs": [
            {"usuari": "Joan", "dies": 15, "retornat": True},
            {"usuari": "Maria", "dies": 20, "retornat": False},
            {"usuari": "Pere", "dies": 12, "retornat": True}
        ]
    },
    {
        "llibre": "1984",
        "autor": "Orwell",
        "categoria": "ciència-ficció",
        "prestecs": [
            {"usuari": "Pere", "dies": 10, "retornat": True},
            {"usuari": "Anna", "dies": 25, "retornat": True},
            {"usuari": "Marta", "dies": 18, "retornat": False}
        ]
    },
    {
        "llibre": "El Senyor dels Anells",
        "autor": "Tolkien",
        "categoria": "fantasia",
        "prestecs": [
            {"usuari": "Maria", "dies": 30, "retornat": True},
            {"usuari": "Joan", "dies": 22, "retornat": True},
            {"usuari": "Pere", "dies": 15, "retornat": False}
        ]
    },
    {
        "llibre": "Crim i Càstig",
        "autor": "Dostoievski",
        "categoria": "novel·la",
        "prestecs": [
            {"usuari": "Anna", "dies": 28, "retornat": True},
            {"usuari": "Marta", "dies": 14, "retornat": True},
            {"usuari": "Joan", "dies": 21, "retornat": True}
        ]
    }
    ]

@pytest.mark.parametrize(
    "input1, input2, resultat_esperat",
    [
        (biblioteca, "novel·la", ['El Quixot', 'Crim i Càstig']),
        (biblioteca, "ciència-ficció", ['1984']),
        (biblioteca, "fantasia", ['El Senyor dels Anells'])  # Corregido
    ]
)
def test_llibres_iguals(input1, input2, resultat_esperat):
    assert llibres_per_categoria(input1, input2) == resultat_esperat

#___________________________________________

@pytest.mark.parametrize(
    "primer, segon, resultat",
    [
        (biblioteca, "El Senyor dels Anells", False),
        (biblioteca, "Crim i Càstig", True),  # Corregido
        (biblioteca, "El Quixot", False)
    ]
)

def test_esta_disponible(primer, segon, resultat):
    assert esta_disponible(primer, segon) == resultat
    
#___________________________________________

@pytest.mark.parametrize(
    "a, b, resultat",
    [
        (biblioteca, "Pere", True),
        (biblioteca, "Joan", False),
        (biblioteca, "Anna", False)  # Corregido
    ]
)

def test_usuari_te_prestecs(a, b, resultat):
    assert usuari_te_prestecs(a, b) == resultat
    
#___________________________________________

# Test amb múltiples paràmetres
@pytest.mark.parametrize(
    "input1, input2, resultat",
    [
        (biblioteca, "El Senyor dels Anells", 67),
        (biblioteca, "Crim i Càstig", 63),
        (biblioteca, "El Quixot", 47)  # Corregido
    ]
)

# Funció per fer la prova
def test_dies_prestec_total(input1, input2, resultat):
    '''
    Comprova si la funció 'dies_prestec_total' retorna correctament la suma total de dies
    que els llibres d'un títol específic han estat en préstec.
    
    :param input1: Llista de llibres en una biblioteca
    :param input2: Títol del llibre per al qual es vol calcular la suma total de dies.
    :param resultat: Suma total esperada de dies de préstec per al llibre.
    
    "assert": Comprova si el resultat retornat per 'dies_prestec_total' coincideix amb el resultat esperat.
    '''
    assert dies_prestec_total(input1, input2) == resultat # Comprovem si el resultat es el mateix