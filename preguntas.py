"""Módulo para almacenar las preguntas del cuestionario."""

# Lista pública donde se almacenarán las preguntas.
# Cada elemento podrá ser un dict con keys como 'pregunta', 'opciones', 'respuesta'
PREGUNTAS = [
    {
        'pregunta': '¿Cuántas esferas del dragón existen?',
        'opciones': {
            'A': '7',
            'B': '8',
            'C': '4',
            'D': '9'
        },
        # respuesta correcta (opcional)
        'correcta': 'A'
    }
    ,
    {
        'pregunta': '¿De qué raza pertenece Goku?',
        'opciones': {
            'A': 'Saiyajin',
            'B': 'Namekiano',
            'C': 'Terrícola',
            'D': 'Mexicano'
        },
        'correcta': 'A'
    }
    ,
    {
        'pregunta': '¿Por qué Goku consiguió el Super Saiyajin?',
        'opciones': {
            'A': 'Mataron a Krillin',
            'B': 'Porque hirieron a Piccolo',
            'C': 'Porque ya no hay juegos buenos en la Play Store',
            'D': 'Por todos los namekianos muertos'
        },
        'correcta': 'A'
    }
]

def agregar(pregunta):
    """Agrega una pregunta (útil helper). Espera un dict o string."""
    PREGUNTAS.append(pregunta)

def listar():
    """Devuelve la lista de preguntas."""
    return PREGUNTAS
