# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta o abrimos el folder desde visual Studio Code 

# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Opcional: Activaremos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu ordenador.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu ordenador.
# OJO: Debes antes tener instalado Streamlit en tu ordenador, 
## también debes antes definir la ruta de tus archivos y 
## tener un script de Python (nombre_de_tu_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC3.py
# python -m streamlit run nombre_de_tu_script.py

# Librería principal para desarrollar aplicaciones web con Streamlit.
import streamlit as st
# Herramienta para crear menús de navegación personalizados en Streamlit.
from streamlit_option_menu import option_menu
# Este módulo permite incrustar componentes personalizados escritos en HTML, CSS y JavaScript dentro de una aplicación.
# components.html() permite mostrar código HTML interactivo directamente en la interfaz.
import streamlit.components.v1 as components
import base64
#Imagen pa
pip install pandas openpyxl
# Menú vertical en una barra lateral
# Crea una barra lateral (sidebar) en la aplicación.
with st.sidebar:
    opciones = option_menu("Selecciona una sección: ",['Inicio', 'Experiencia', 'Gráficos', 'Que tanto sabes de los chinos?'] , 
        icons=['0-circle','1-circle', '2-circle','3-circle'], menu_icon="filetype-py", default_index=0)
    # Crea un menú de opciones dentro de la barra lateral -> option_menu(...)
    # Título que se mostrará encima del menú -> "Selecciona una sección: "
    # Lista de opciones disponibles para navegar -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['0-circle','1-circle', '2-circle']
    # Icono principal que aparece junto al título del menú -> menu_icon="filetype-py"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0

# Menú horizontal en una barra horizontal
# OJO: Se puede eliminar el título del menú con None
# Crea un menú de navegación horizontal y guarda la opción seleccionada por el usuario en la variable 'selected'
selected = option_menu(
    menu_title="Selecciona una sección: ", 
    options=['Inicio', 'Experiencia', 'Gráficos'], 
    icons=['person-heart', 'globe-americas', 'pencil-square'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
    # Título que aparece antes de las opciones del menú -> menu_title="Selecciona una sección: "
    # Lista de opciones que estarán disponibles en el menú -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['person-heart', 'globe-americas', 'pencil-square']
    # Icono principal que aparece junto al título del menú -> menu_icon="cast"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0
    # Hace que el menú se muestre horizontalmente en lugar de verticalmente -> orientation="horizontal"

# Verifica si el usuario ha seleccionado la opción "Inicio" en el menú de navegación horizontal.
# OJO: En caso que elijas el menú de la barra lateral (sidebar) debes cambiar "selected" por "opciones"
if opciones == 'Inicio':
    st.markdown("<h1 style='text-align: center;'>Nombre del blog</h1>", unsafe_allow_html=True)
    # Muestra un título principal utilizando HTML -> st.markdown("...", unsafe_allow_html=True)
    # La etiqueta <h1> define un encabezado de nivel 1 -> "<h1 ...>...</h1>"
    # El estilo CSS 'text-align: center' centra el texto -> style='text-align: center;'
    # unsafe_allow_html=True permite que Streamlit interprete y renderice el código HTML incluido en la cadena

    # Crea dos columnas de igual tamaño para organizar el contenido de forma horizontal en la aplicación.
    col1, col2 = st.columns(2)

    # Muestra una imagen en la primera columna
    col1.image("ellie.png", caption='Ellie', width=300)
    # "ellie.png" es el archivo de imagen que se visualizará -> Aquí debes reemplazar por tu foto de perfil
    # El texto "Ellie" aparecerá como descripción de la imagen
    # width=300 establece el ancho de la imagen en 300 píxeles

    # Define una cadena de texto multilínea que contiene una guía para redactar una presentación personal.
    texto = """
    Aquí escribe una presentación creativa sobre ti.
    ¿Quién eres?, 
    ¿De dónde eres?, 
    ¿Qué estudias?, 
    ¿Qué te gusta de tu carrera?, 
    ¿Qué te gustaría hacer en el futuro?, 
    ¿Qué te gusta hacer en tu tiempo libre?
    """

    # Muestra el texto en la segunda columna utilizando HTML
    col2.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto}</div>", unsafe_allow_html=True)
    # El estilo CSS justifica el texto y establece un tamaño de fuente de 18 píxeles
    # f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>"
    # unsafe_allow_html=True permite que Streamlit interprete las etiquetas HTML incluidas en la cadena

elif opciones == 'Experiencia':
    st.markdown("<h1 style='text-align: center;'>Nombre a la sección de experiencia 💻</h1>", unsafe_allow_html=True)

    # Agregar un  texto para la respuesta
    texto_2 = """
    Aquí escribe tu experiencia aprendiendo a programar. 
    ¿Cómo te sentiste al principio?, 
    ¿Qué te ha enseñado la programación?, 
    ¿Qué te gusta de programar?, 
    ¿Qué te gustaría hacer con la programación en el futuro?
    ¿Cómo se relaciona lo que haz aprendido con tu carrera?
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    # Formato A
    # Agregamos todo los videos realizados en las prácticas anteriores
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Video 1 - YouTube")
    # Inserta un video de YouTube directamente en la aplicación.
    # El usuario puede reproducirlo sin salir de Streamlit.
    st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se presenta ...., "
    )

    # Formato B
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Video 1 - Google Drive")
    # Crea un botón que redirige al usuario a un video alojado en Google Drive. 
    # Al hacer clic, el video se abrirá en una nueva pestaña del navegador.
    st.link_button(
            "Ver video",
            "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link"
        )
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se presenta ...., "
    )

elif opciones == 'Gráficos':
    st.markdown("<h2 style='text-align: center;'>Nombre a la sección 'Gráficos'</h2>", unsafe_allow_html=True)

    graficos = ['Gráfico_1', 'Gráfico_2', 'Mapa_1']

    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Gráfico_1':
        # Título de la sección
        st.subheader("📊 Gráfico 1: Lenguas aisladas")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
            Aquí debe ir una breve interpretación de tu gráfico.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen utilizando tres columnas
        col3, col4, col5 = st.columns([1, 5, 1])

        with col4:
            st.image(
                "aisladas_base_datos.png",
                width=800
            )

    elif grafico_seleccionado == 'Gráfico_2':
        # Título de la sección
        st.subheader("📊 Gráfico 2: Familias lingüísticas")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Aquí debe ir una breve interpretación del gráfico.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "lengua_familia_GB.png",
                width=800
            )
    elif grafico_seleccionado == 'Mapa_1':
        # Título de la sección
        st.subheader("🗺️ Mapa 1: Distribución geográfica")

        # Interpretación del mapa
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Aquí debe ir una breve interpretación del mapa.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Cargar el mapa HTML generado previamente
        with open("mapa.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        # Mostrar el mapa interactivo
        components.html(
            html_content,
            height=600
        )
elif opciones == 'Que tanto sabes de los chinos?':
    st.markdown("<h1 style='text-align: center;'>Que tanto sabes de los chinos? 💻</h1>",unsafe_allow_html=True)    
    # Agregar un  texto para la respuesta
    texto_4 = """
    Hola preciosa calabazita de algodon, en este quiz se te hara una prueba psicometrica 
    para saber que tan fan eres de los hermosos chicos ojos razgados que cantan como los mismos angeles
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_4}</div>", unsafe_allow_html=True)
        # --- SELECCIONAR DIFICULTAD ---
    dificultad = st.radio(
        "Selecciona el nivel de dificultad:",
        options=["Fácil", "Normal", "Difícil"],
        index=0,  # Por defecto "Fácil"
        horizontal=True
    )
    st.divider()  # Línea separadora

    # --- BANCO DE PREGUNTAS ---
    preguntas_facil = [
        {
            "pregunta": "¿De qué país proviene el K-pop?",
            "opciones": ["Japón", "Corea del Sur", "China", "Tailandia"],
            "respuesta": "Corea del Sur"
        },
        {
            "pregunta": "¿Qué significa K-pop?",
            "opciones": ["Korean Pop", "King Pop", "Kawaii Pop", "K-Music"],
            "respuesta": "Korean Pop"
        },
        {
            "pregunta": "¿Cuál de estos es un grupo de K-pop?",
            "opciones": ["BTS", "One Direction", "Maroon 5", "Coldplay"],
            "respuesta": "BTS"
        },
        {
            "pregunta": "¿Cuál de estas palabras se usa mucho en K-pop para referirse a los fans?",
            "opciones": ["Fandom", "Clan", "Equipo", "Banda"],
            "respuesta": "Fandom"
        },
        {
            "pregunta": "¿Qué significa 'maknae'?",
            "opciones": ["Líder", "Integrante más joven", "Rapero principal", "Coreógrafo"],
            "respuesta": "Integrante más joven"
        }
    ]

    preguntas_normal = [
        {
            "pregunta": "¿Cuál es la compañía detrás del grupo BTS?",
            "opciones": ["SM Entertainment", "YG Entertainment", "HYBE (antes Big Hit)", "JYP Entertainment"],
            "respuesta": "HYBE (antes Big Hit)"
        },
        {
            "pregunta": "En el K-pop, ¿qué es un 'comeback'?",
            "opciones": ["Un concierto especial", "El lanzamiento de nuevo material musical", "Un baile característico", "El saludo del grupo"],
            "respuesta": "El lanzamiento de nuevo material musical"
        },
        {
            "pregunta": "¿Qué significa 'bias' en el fandom del K-pop?",
            "opciones": ["El miembro favorito de cada persona", "El líder del grupo", "El baile principal", "El primer álbum"],
            "respuesta": "El miembro favorito de cada persona"
        },
        {
            "pregunta": "¿Qué artista popularizó el K-pop a nivel mundial con 'Gangnam Style'?",
            "opciones": ["BTS", "PSY", "BLACKPINK", "EXO"],
            "respuesta": "PSY"
        },
        {
            "pregunta": "¿Cómo se llama el sistema de baile sincronizado en grupo que caracteriza al K-pop?",
            "opciones": ["Freestyle", "Coreografía en espejo", "Dance battle", "Performance grupal"],
            "respuesta": "Coreografía en espejo"  # Aunque es un término común, lo dejo así para la prueba
        }
    ]

    preguntas_dificil = [
        {
            "pregunta": "¿Quién es el líder del grupo BTS (Bangtan Sonyeondan)?",
            "opciones": ["Jin", "Suga", "RM", "J-Hope"],
            "respuesta": "RM"
        },
        {
            "pregunta": "¿Qué significa la palabra 'Sasaeng' dentro de la cultura del K-pop?",
            "opciones": ["Un fan que sigue obsesivamente a los ídolos", "Un baile moderno", "Un tipo de saludo", "Una canción de amor"],
            "respuesta": "Un fan que sigue obsesivamente a los ídolos"
        },
        {
            "pregunta": "¿Cuál es el nombre del fundador de HYBE Corporation?",
            "opciones": ["Lee Soo-man", "Yang Hyun-suk", "Park Jin-young", "Bang Si-hyuk"],
            "respuesta": "Bang Si-hyuk"
        },
        {
            "pregunta": "En la industria del K-pop, ¿qué es un 'lightstick'?",
            "opciones": ["Un bastón de luz oficial del grupo", "Un micrófono especial", "Un accesorio de baile", "Un tipo de coreografía"],
            "respuesta": "Un bastón de luz oficial del grupo"
        },
        {
            "pregunta": "¿Qué grupo de K-pop es conocido por tener una integrante llamada 'Lisa'?",
            "opciones": ["TWICE", "RED VELVET", "BLACKPINK", "ITZY"],
            "respuesta": "BLACKPINK"
        }
    ]

    # --- SELECCIONAR EL BANCO SEGÚN DIFICULTAD ---
    if dificultad == "Fácil":
        preguntas = preguntas_facil
    elif dificultad == "Normal":
        preguntas = preguntas_normal
    else:
        preguntas = preguntas_dificil

    # --- MOSTRAR PREGUNTAS Y GUARDAR RESPUESTAS ---
    respuestas_usuario = {}
    for i, p in enumerate(preguntas):
        respuestas_usuario[i] = st.radio(
            f"**{i+1}. {p['pregunta']}**",
            p["opciones"],
            key=f"pregunta_{i}"  # Clave única para cada radio
        )

    # --- BOTÓN PARA CALIFICAR ---
    if st.button("📊 Ver mi puntuación", use_container_width=True):
        correctas = 0
        for i, p in enumerate(preguntas):
            if respuestas_usuario[i] == p["respuesta"]:
                correctas += 1
        
        total = len(preguntas)
        porcentaje = (correctas / total) * 100
        
        # Mostrar resultado con emojis según rendimiento
        if porcentaje == 100:
            mensaje = "🌟 ¡Perfecto! Eres un auténtico experto en K-pop."
        elif porcentaje >= 60:
            mensaje = "🎉 ¡Bien! Tienes buen conocimiento, pero puedes mejorar."
        else:
            mensaje = "📖 ¡Sigue practicando! El K-pop tiene mucho más que ofrecer."
        
        st.success(f"**{correctas}** de **{total}** respuestas correctas ({porcentaje:.0f}%)")
        st.info(mensaje)
        
        # Opcional: mostrar cuáles fallaste (si quieres, descomenta esto)
        # with st.expander("Ver respuestas correctas"):
        #     for i, p in enumerate(preguntas):
        #         if respuestas_usuario[i] != p["respuesta"]:
        #             st.write(f"❌ {p['pregunta']} → Respuesta correcta: **{p['respuesta']}**")

