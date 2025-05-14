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

# Test amb múltiples paràmetres
@pytest.mark.parametrize(
    "input1, input2, resultat_esperat",  # Noms dels paràmetres
    [
        (biblioteca, "novel·la", ['El Quixot', 'Crim i Càstig']), # Hauria de passar
        (biblioteca, "ciència-ficció", ['1984']), # Hauria de passar
        (biblioteca, "novel·la", ['1984', 'El Quixot']) # NO hauria de passar
    ]
)

# Funció per fer la prova
def test_llibres_iguals(input1, input2, resultat_esperat):
    '''
    Comprova si la funció 'llibres_per_categoria' retorna els llibres correctes per a una categoria donada.
    
    :param input1: Llista de llibres en una biblioteca
    :param input2: Categoria que vols buscar
    :param resultat_esperat: Llista de títols esperats
    
    "assert": Comprova si el resultat retornat per 'llibres_per_categoria' coincideix amb el resultat esperat.
    
    '''
    assert llibres_per_categoria(input1, input2) == resultat_esperat # Comprovem si el resultat es el mateix

#___________________________________________

# Test amb múltiples paràmetres
@pytest.mark.parametrize(
    "primer, segon, resultat", # Noms dels paràmetres
    [
        (biblioteca, "El Senyor dels Anells", False), # Hauria de passar
        (biblioteca, "El Quixot", False), # Hauria de passar
        (biblioteca, "El Quixot", True) # NO hauria de passar
        
    ]
)

# Funció per fer la prova
def test_esta_disponible(primer, segon, resultat):
    '''
    Comprova si la funció 'esta_disponible' determina correctament la disponibilitat d'un llibre.
    
    :param primer: Llista de llibres en una biblioteca
    :param segon: Títol del llibre que es vol comprovar.
    :param resultat: Estat que esperem de la disponibilitat del llibre (True = disponible, False = no). 
    
    "assert": Comprova si el resultat retornat per 'esta_disponible' coincideix amb el resultat esperat.
    
    '''
    assert esta_disponible(primer, segon) == resultat # Comprovem si el resultat es el mateix
    
#___________________________________________

# Test amb múltiples paràmetres
@pytest.mark.parametrize(
    "a, b, resultat", # Noms dels paràmetres
    [
        (biblioteca, "Pere", True), # Hauria de passar
        (biblioteca, "Joan", False), # Hauria de passar
        (biblioteca, "Pere", False) # Hauria de fallar
    ]
)

# Funció per fer la prova
def test_usuari_te_prestecs(a, b, resultat):
    '''
    Comprova si la funció 'usuari_te_prestecs' detecta correctament si un usuari té préstecs actius.
    
    :param a: Llista de llibres en una biblioteca
    :param b: Nom de l'usuari que es vol comprovar
    :param resultat: Estat esperat (True = té préstecs actius, False = no).
    
    "assert": Comprova si el resultat retornat per 'usuari_te_prestecs' coincideix amb el resultat esperat.
    '''
    assert usuari_te_prestecs(a, b) == resultat # Comprovem si el resultat es el mateix
    
#___________________________________________

# Test amb múltiples paràmetres
@pytest.mark.parametrize(
    "input1, input2, resultat", # Noms dels paràmetres
    [
        (biblioteca, "El Senyor dels Anells", 67), # Hauria de passar
        (biblioteca, "Crim i Càstig", 63), # Hauria de passar
        (biblioteca, "El Quixot", 1000) # Hauria de fallar
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