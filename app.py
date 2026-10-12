import streamlit as st
import streamlit as st

# Тёмная тема через CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1e1e1e;  /* тёмно-серый фон */
        color: #ffffff;             /* белый текст по умолчанию */
    }
    /* Подправим цвета для заголовков и подзаголовков, чтобы читались */
    h1, h2, h3, .stText, .stMarkdown p {
        color: #f0f0f0;
    }
    /* Тёмный фон для карточек-контейнеров, если они есть */
    .stContainer {
        background-color: #2b2b2b;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="Literary Places of Russia", page_icon="📖")

# English-only data: names, descriptions, images, coordinates
places_data = {
    "Bryansk Oblast": [
        {
            "name": "Fyodor Tyutchev Estate Museum (Ovstug)",
            "desc": (
                "Ovstug is where Tyutchev’s special vision of nature and poetry took shape. "
                "Here, among the Bryansk fields and quiet alleys, he first felt how silence could sound like verse. "
                "The estate remembers both the poet’s childhood and his mature visits when, already a famous diplomat and thinker, "
                "he briefly returned to these walls to hear again that special, almost musical whisper of the leaves."
            ),
            "lat": 53.3797,
            "lon": 33.8778,
            "img": ["h/li.jpg", "h/kh.webp"]
        },
        {
            "name": "Aleksey Tolstoy House Museum (Krasny Rog)",
            "desc": (
                "Krasny Rog was not a showy residence for Aleksey Konstantinovich Tolstoy, but a real home where he could be himself. "
                "He rested here from the bustle of the capital, wrote a lot, and held quiet family evenings. "
                "The estate is closely tied to his dramas and lyrics: in these rooms, images were born that combined personal tone "
                "with a deep interest in Russian history. The house preserves authentic details of everyday life that help you feel the atmosphere of the era."
            ),
            "lat": 52.9231,
            "lon": 33.4717,
            "img": ["h/was.jpg", "h/i (28).webp"]
        }
    ],
    "Saint Petersburg": [
        {
            "name": "Alexander Pushkin Memorial Apartment (Moika, 12)",
            "desc": (
                "This apartment marks the end of Pushkin’s earthly biography and the beginning of his immortality: "
                "his final months were spent here, filled with intense work and anxious premonitions. "
                "The rooms carefully preserve the original furnishings, helping you see Pushkin not as a bronze monument, "
                "but as a living person. His study with the working desk, bookshelves with favorite books, and personal items "
                "show how the poet lived and what he thought about. The exhibition’s strength lies in its details."
            ),
            "lat": 59.9417,
            "lon": 30.3083,
            "img": ["h/i.webp", "h/l.jpg"]
        },
        {
            "name": "Fyodor Dostoevsky Literary and Memorial Museum",
            "desc": (
                "In this apartment, Dostoevsky didn’t just live — he created his world. Ideas were born here, complex psychological lines were built, "
                "and everyday life became material for great novels. The exhibition conveys not only the writer’s быт (everyday life), "
                "but also the atmosphere of intense labor: the working desk with manuscripts, books, and objects he used. "
                "Every detail reveals Dostoevsky’s character: asceticism sits side by side with deep concentration, "
                "and the modesty of the surroundings only emphasizes the scale of his thought."
            ),
            "lat": 59.9343,
            "lon": 30.3351,
            "img": ["h/i (27).webp", "h/fap.jpg"]
        }
    ],
    "Tylskya Oblast and Moscow": [
        {
            "name": "Leo Tolstoy Estate Museum 'Yasnaya Polyana'",
            "desc": (
                "Yasnaya Polyana is not just an estate — it’s an entire world where Tolstoy lived most of his life and which became the source of his main themes. "
                "The writer’s house holds authentic items that show how his strict yet warm everyday life was arranged: the study with a simple desk, "
                "the library filled with books he constantly consulted, and the rooms where his large family lived. "
                "The park and alleys were not only places for walks, but spaces for reflection: here he pondered the fates of the heroes of 'War and Peace' and 'Anna Karenina', "
                "and nature became his interlocutor and teacher."
            ),
            "lat": 54.0758,
            "lon": 37.5266,
            "img": ["h/ioh.jpg", "h/palen.jpg"]
        },
        {
            "name": "Mikhail Bulgakov House Museum ('The Naughty Apartment')",
            "desc": (
                "'The Naughty Apartment' is a place where reality and fiction wove so tightly in Bulgakov’s mind that it’s impossible to separate them now. "
                "This communal apartment on Bolshaya Sadovaya became the prototype of the famous apartment from 'The Master and Margarita'. "
                "The museum conveys not only the everyday life of the 1920s–1930s, but also the special atmosphere where Bulgakov’s style was born: "
                "mystique sits next to irony, and an ordinary household detail becomes a key to big meanings. "
                "You can feel how the writer saw the extraordinary in the ordinary — and how magic grew from daily hustle."
            ),
            "lat": 55.7663,
            "lon": 37.6000,
            "img": ["h/pop.jpg", "h/lodka.jpg"]
        }
    ]
}

st.sidebar.title("Select a Region")
region = st.sidebar.radio("Region", list(places_data.keys()))

st.title(f"📖 Literary Places: {region}")

selected_places = places_data[region]


st.subheader("📍 Map of Literary Sites")

map_data = []
for p in selected_places:
    map_data.append({
        "latitude": p["lat"],
        "longitude": p["lon"],
        "name": p["name"]
    })

st.map(map_data, zoom=7)


st.subheader("📚 Places and Descriptions")

for place in selected_places:
    st.subheader(place["name"])
    
    for img_path in place["img"]:
        try:
            st.image(img_path, width="stretch")
        except Exception:
            pass

    st.write(place["desc"])

    map_url = f"https://www.google.com/maps?q={place['lat']},{place['lon']}"
    st.link_button("🗺 Show on Google Maps", map_url)
    st.divider()

