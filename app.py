import streamlit as st

# Настройки на страницата
st.set_page_config(
    page_title="Температурен помощник",
    page_icon="🌡️",
    layout="centered"
)

# CSS анимации
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #101c3a, #243b65, #345b82);
    color: white;
}

h1, h2, h3, p, label {
    color: white !important;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    animation: fadeIn 2s ease-in-out;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    animation: fadeIn 3s ease-in-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.sun {
    font-size: 100px;
    text-align: center;
    animation: rotateSun 8s linear infinite,
               pulse 2s ease-in-out infinite;
}

@keyframes rotateSun {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

@keyframes pulse {
    0%, 100% { scale: 1; }
    50% { scale: 1.15; }
}

.snow {
    font-size: 70px;
    text-align: center;
    animation: snowfall 3s ease-in-out infinite;
}

@keyframes snowfall {
    0% {
        transform: translateY(-20px);
        opacity: 0;
    }
    50% {
        opacity: 1;
    }
    100% {
        transform: translateY(30px);
        opacity: 0;
    }
}

.fire {
    font-size: 90px;
    text-align: center;
    animation: fireAnimation 0.8s ease-in-out infinite alternate;
}

@keyframes fireAnimation {
    from {
        transform: scale(1) rotate(-5deg);
    }
    to {
        transform: scale(1.2) rotate(5deg);
    }
}

.result {
    text-align: center;
    padding: 20px;
    border-radius: 20px;
    background: rgba(255,255,255,0.12);
    animation: fadeIn 1.5s ease-in-out;
}

</style>
""", unsafe_allow_html=True)


# Заглавие
st.markdown(
    '<div class="main-title">🌡️ Температурен помощник</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Провери времето и получи съвет как да се облечеш!</div>',
    unsafe_allow_html=True
)

st.write("")

# Въвеждане на температура
st.markdown("### 🌡️ Въведи температура")

temperature = st.number_input(
    "Температура в °C:",
    min_value=-50,
    max_value=60,
    value=20,
    step=1
)

# Бутон
if st.button("🔍 Провери температурата", use_container_width=True):

    st.markdown("---")

    st.markdown(
        '<div class="result"><h2>🌤️ Резултат от проверката</h2></div>',
        unsafe_allow_html=True
    )

    # Проверка на температурата

    if temperature < 0:

        st.markdown(
            '<div class="snow">❄️ ❄️ ❄️</div>',
            unsafe_allow_html=True
        )

        st.error("🥶 Изключително студено е!")
        st.write("Температурата е под нулата.")
        st.write("🧥 Облечи дебело зимно яке.")
        st.write("🧣 Не забравяй шапка, шал и ръкавици!")

        st.snow()

    elif temperature < 10:

        st.markdown(
            '<div class="snow">🌨️</div>',
            unsafe_allow_html=True
        )

        st.info("❄️ Студено е!")
        st.write("Навън е доста хладно.")
        st.write("🧥 Облечи топло яке и затворени обувки.")

    elif temperature < 20:

        st.markdown(
            '<div class="sun">🌤️</div>',
            unsafe_allow_html=True
        )

        st.warning("🌥️ Прохладно е.")
        st.write("Времето е сравнително приятно.")
        st.write("🧥 Подходящо е леко яке или суичър.")

    elif temperature < 30:

        st.markdown(
            '<div class="sun">☀️</div>',
            unsafe_allow_html=True
        )

        st.success("☀️ Приятно топло е!")
        st.write("Температурата е подходяща за разходка.")
        st.write("👕 Облечи леки и удобни дрехи.")

        st.balloons()

    else:

        st.markdown(
            '<div class="fire">🔥</div>',
            unsafe_allow_html=True
        )

        st.error("🔥 Много е горещо!")
        st.write("Навън температурите са високи.")
        st.write("🕶️ Носи леки дрехи.")
        st.write("💧 Пий повече вода.")
        st.write("🌳 Стой на сянка и избягвай силното слънце.")

    # Допълнителна информация
    st.markdown("---")

    st.markdown("### 📊 Допълнителна информация")

    st.metric(
        label="Измерена температура",
        value=f"{temperature} °C"
    )

    # Прогрес лента
    progress = (temperature + 50) / 110

    st.write("Температурна скала:")
    st.progress(progress)

    st.caption("Скалата показва температурата спрямо диапазона от -50°C до 60°C.")

    st.markdown("---")

    st.success("✅ Проверката приключи успешно!")

# Долен текст
st.markdown("---")

st.markdown(
    '<div style="text-align:center;">'
    '🌡️ Температурен помощник | Създаден със Streamlit'
    '</div>',
    unsafe_allow_html=True
)

