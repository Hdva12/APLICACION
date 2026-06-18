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
    ,
    {
        'pregunta': '¿Cuál es el hijo de Vegeta?',
        'opciones': {
            'A': 'Trunks',
            'B': 'Gohan',
            'C': 'Kyabe',
            'D': 'El Ciber'
        },
        'correcta': 'A'
    }
    ,
    {
        'pregunta': '¿Cuál fue el primer villano de Dragon Ball Z?',
        'opciones': {
            'A': 'Raditz',
            'B': 'Piccolo',
            'C': 'Vegeta y Nappa',
            'D': 'Anubis un poderoso enemigo'
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


def get_vf_questions():
    """Devuelve una lista de 5 preguntas de Verdadero/Falso.

    Cada pregunta es un dict con 'pregunta', 'opciones' (A=Verdadero, B=Falso),
    'correcta' ('A' o 'B') y opcionalmente 'explicacion'.
    """
    return [
        {
            'pregunta': 'Gohan alcanza el estado Super Saiyajin 2 durante la saga de Cell.',
            'opciones': {'A': 'Verdadero', 'B': 'Falso'},
            'correcta': 'A',
            'explicacion': 'Gohan alcanza Super Saiyajin 2 durante la pelea contra Cell.'
        },
        {
            'pregunta': 'Bills (Beerus) es el Dios de la Destrucción del Universo 6.',
            'opciones': {'A': 'Verdadero', 'B': 'Falso'},
            'correcta': 'B',
            'explicacion': 'Beerus es el Dios de la Destrucción del Universo 7, no del 6.'
        },
        {
            'pregunta': 'Trunks del futuro utiliza una espada en su primera aparición.',
            'opciones': {'A': 'Verdadero', 'B': 'Falso'},
            'correcta': 'A',
            'explicacion': 'Trunks aparece por primera vez empuñando una espada.'
        },
        {
            'pregunta': 'Cell alcanza su forma perfecta absorbiendo a otros androides.',
            'opciones': {'A': 'Verdadero', 'B': 'Falso'},
            'correcta': 'A',
            'explicacion': 'Cell absorbe a los androides 17 y 18 para alcanzar su forma perfecta.'
        },
        {
            'pregunta': 'Vegeta es originario del planeta Namek.',
            'opciones': {'A': 'Verdadero', 'B': 'Falso'},
            'correcta': 'B',
            'explicacion': 'Vegeta es un Saiyajin originario del Planeta Vegeta, no de Namek.'
        },
        {
            'pregunta': 'Goku aprendió a volar por medio del entrenamiento con el Maestro Roshi.',
            'opciones': {'A': 'Verdadero', 'B': 'Falso'},
            'correcta': 'B',
            'explicacion': 'Goku aprende a volar de forma natural más tarde; el Maestro Roshi no es quien le enseña a volar.'
        },
        {
            'pregunta': 'El Kaioken es una técnica enseñada por Whis.',
            'opciones': {'A': 'Verdadero', 'B': 'Falso'},
            'correcta': 'B',
            'explicacion': 'El Kaioken fue enseñado por el Kaio (King Kai), no por Whis.'
        },
        {
            'pregunta': 'El Super Saiyajin original apareció cuando Goku peleó con Freezer.',
            'opciones': {'A': 'Verdadero', 'B': 'Falso'},
            'correcta': 'A',
            'explicacion': 'Goku se transforma en Super Saiyajin por primera vez durante la batalla contra Freezer.'
        },
        {
            'pregunta': 'El Dragón Shenlong puede conceder cualquier deseo sin limitaciones.',
            'opciones': {'A': 'Verdadero', 'B': 'Falso'},
            'correcta': 'B',
            'explicacion': 'Shenlong tiene limitaciones: no puede crear vida si no está dentro de su poder, entre otras restricciones.'
        },
        {
            'pregunta': 'Los Saiyajins aumentan su poder tras recuperarse de heridas graves.',
            'opciones': {'A': 'Verdadero', 'B': 'Falso'},
            'correcta': 'A',
            'explicacion': 'Los Saiyajins poseen la habilidad de volverse más fuertes tras recuperarse de heridas severas (Zenkai).' 
        }
    ]


# Añadir 10 preguntas más al cuestionario normal (no V/F)
PREGUNTAS.extend([
    {
        'pregunta': '¿Qué invento utiliza Bulma para localizar las Esferas del Dragón?',
        'opciones': {'A': 'Radar del dragón', 'B': 'Espada de energía', 'C': 'Capsula Hoi-Poi', 'D': 'Scouter'},
        'correcta': 'A',
        'explicacion': 'Bulma creó y usa el Radar del Dragón para encontrar las Esferas.'
    },
    {
        'pregunta': '¿Cómo se llama el hermano mayor de Goku que aparece al inicio de DBZ?',
        'opciones': {'A': 'Raditz', 'B': 'Gohan', 'C': 'Turles', 'D': 'Nappa'},
        'correcta': 'A',
        'explicacion': 'Raditz es el hermano mayor de Goku que aparece al comienzo de Dragon Ball Z.'
    },
    {
        'pregunta': '¿Quién enseña a Goku la técnica Kaioken?',
        'opciones': {'A': 'Kaio del Norte (King Kai)', 'B': 'Maestro Roshi', 'C': 'Piccolo', 'D': 'Whis'},
        'correcta': 'A',
        'explicacion': 'King Kai (Kaio) enseña a Goku el Kaioken durante su entrenamiento.'
    },
    {
        'pregunta': '¿De qué raza es Piccolo?',
        'opciones': {'A': 'Namekiano', 'B': 'Saiyajin', 'C': 'Terrícola', 'D': 'Androide'},
        'correcta': 'A',
        'explicacion': 'Piccolo pertenece a la raza Namekiana.'
    },
    {
        'pregunta': '¿Cuál es la técnica característica de Vegeta?',
        'opciones': {'A': 'Galick Gun', 'B': 'Kamehameha', 'C': 'Masenko', 'D': 'Final Shine'},
        'correcta': 'A',
        'explicacion': 'El Galick Gun es una de las técnicas icónicas de Vegeta.'
    },
    {
        'pregunta': '¿Quién creó a los androides 17 y 18?',
        'opciones': {'A': 'Dr. Gero', 'B': 'Bulma', 'C': 'Dr. Brief', 'D': 'Dr. Wheelo'},
        'correcta': 'A',
        'explicacion': 'Dr. Gero, del Equipo Red Ribbon, es el creador de los androides 17 y 18.'
    },
    {
        'pregunta': '¿Cómo se llama la fusión que se realiza mediante la Danza de la Fusión?',
        'opciones': {'A': 'Vegito', 'B': 'Gogeta', 'C': 'Vegetto', 'D': 'Goketa'},
        'correcta': 'B',
        'explicacion': 'Gogeta es el resultado de la Danza de la Fusión entre Goku y Vegeta.'
    },
    {
        'pregunta': '¿Trunks proviene de un futuro donde los androides han destruido gran parte de la Tierra?',
        'opciones': {'A': 'Sí', 'B': 'No', 'C': 'Solo en parte', 'D': 'No se sabe'},
        'correcta': 'A',
        'explicacion': 'Trunks viene de un futuro alterno arrasado por los androides.'
    },
    {
        'pregunta': '¿Qué técnica es el ataque característico del Maestro Roshi?',
        'opciones': {'A': 'Kamehameha', 'B': 'Final Flash', 'C': 'Destructo Disk', 'D': 'Masenko'},
        'correcta': 'A',
        'explicacion': 'El Kamehameha es la técnica característica del Maestro Roshi.'
    },
    {
        'pregunta': '¿Cuál es el objetivo del Torneo de la Fuerza en Dragon Ball Super?',
        'opciones': {'A': 'Determinar qué universos sobreviven', 'B': 'Repartir las Esferas del Dragón', 'C': 'Elegir al mejor luchador de la Tierra', 'D': 'Encontrar a los Kaioshin'},
        'correcta': 'A',
        'explicacion': 'El Torneo de la Fuerza enfrenta universos para decidir su supervivencia.'
    }
])
