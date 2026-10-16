# Genera audio/01.mp3, 02.mp3... con una voz neural latinoamericana.
# Requisitos: Python 3 e internet.   Instalar:  pip install edge-tts
# Voces sugeridas: es-CO-SalomeNeural, es-CO-GonzaloNeural, es-MX-DaliaNeural, es-MX-JorgeNeural
import asyncio, os
import edge_tts

VOICE = "es-CO-SalomeNeural"
RATE = "-8%"   # más lento = más pausado; prueba "-12%" o "-4%"

LINES = [
 "A veces sientes que has vivido cosas difíciles. Que hay problemas que no logras resolver y que te superan.",
 "Si alguna vez has sentido eso, te invito a algo sencillo: mira hacia el Sol.",
 "Parece pequeño, pero está a 150 millones de kilómetros. Su luz tarda más de 8 minutos en llegar hasta aquí.",
 "Este es todo el mundo que conoces.",
 "Ahora, siéntate.",
 "¿Ya estás sentado? Por tu seguridad, es muy importante que lo hagas.",
 "Mercurio, el planeta más cercano al Sol.",
 "Mide 4.879 kilómetros, poco más de un tercio de la Tierra.",
 "Marte, un planeta rocoso del Sistema Solar.",
 "Mide 6.779 kilómetros, un poco más de la mitad de la Tierra.",
 "Venus, otro planeta rocoso del Sistema Solar.",
 "Mide 12.104 kilómetros, casi igual que la Tierra.",
 "Esta es la Tierra, nuestro hogar.",
 "Mide 12.756 kilómetros de diámetro.",
 "Neptuno, un gigante de hielo del Sistema Solar.",
 "Mide 49.244 kilómetros, casi cuatro veces la Tierra.",
 "Urano, también un gigante de hielo.",
 "Mide 50.724 kilómetros, unas cuatro veces la Tierra.",
 "Saturno, un gigante gaseoso famoso por sus anillos.",
 "Mide 116.460 kilómetros, más de nueve veces la Tierra.",
 "Júpiter, el planeta más grande del Sistema Solar.",
 "Mide 139.820 kilómetros, unas once veces la Tierra.",
 "Y este es el Sol, la estrella de nuestro sistema.",
 "Es unas 109 veces más ancho que la Tierra. En su interior cabrían más de un millón de Tierras.",
 "Sirio, una estrella de la Vía Láctea, en la constelación del Can Mayor.",
 "Es la más brillante del cielo nocturno. Mide 1,7 radios solares y está a 8,6 años luz.",
 "Arturo, una estrella de la Vía Láctea, en la constelación del Boyero.",
 "Es una gigante naranja de unos 25 radios solares, a 37 años luz.",
 "Betelgeuse, una estrella de la Vía Láctea, en la constelación de Orión.",
 "Es una supergigante roja de entre 640 y 760 radios solares, a una distancia de entre 500 y 650 años luz.",
 "UY Scuti, una estrella de la Vía Láctea, en la constelación del Escudo.",
 "Es una supergigante roja de entre 755 y 1.700 radios solares, según la medición, a entre 5.100 y 9.500 años luz.",
 "VY Canis Majoris, una estrella de la Vía Láctea, en la constelación del Can Mayor.",
 "Es una hipergigante roja de unos 1.420 radios solares, a 3.900 años luz.",
 "Stephenson 2-18, la mayor estrella conocida. Está en la Vía Láctea, en un cúmulo de la constelación del Escudo.",
 "Es una supergigante roja de unos 2.150 radios solares, a unos 19.000 años luz.",
 "Frente a todo esto, tus problemas se ven más pequeños de lo que parecían. Y aun así, en este punto diminuto es donde existe todo lo que te importa.",
 "Cuando quieras, puedes ponerte de pie con calma."
]

async def main():
    os.makedirs("audio", exist_ok=True)
    for i, t in enumerate(LINES, 1):
        await edge_tts.Communicate(t, VOICE, rate=RATE).save(f"audio/{i:02d}.mp3")
        print("listo", i, "de", len(LINES))

asyncio.run(main())
