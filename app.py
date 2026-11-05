
import streamlit as st
import pandas as pd

from datetime import datetime
from pathlib import Path

from temperature import (
    get_temperature_info,
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    get_progress,
    get_extra_advice,
    get_weather_animation,
    calculate_temperature_difference,
    get_temperature_description
)


# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="TEMPERATURE PRO",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# 2. LOAD CSS
# ==========================================

css_path = Path(__file__).parent / "style.css"

if css_path.exists():
    css = css_path.read_text(encoding="utf-8")
    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )


# ==========================================
# 3. SESSION STATE
# ==========================================

if "history" not in st.session_state:
    st.session_state.history = []

if "last_result" not in st.session_state:
    st.session_state.last_result = None

if "checks" not in st.session_state:
    st.session_state.checks = 0


# ==========================================
# 4. SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("# 🌡️ TEMP PRO")
    st.caption("ULTIMATE WEATHER EXPERIENCE")

    st.divider()

    st.markdown("### ⚙️ Настройки")

    theme = st.selectbox(
        "Цветова тема",
        ["Dark Neon", "Ocean Blue", "Purple Dream"]
    )

    show_animation = st.toggle(
        "Активирай анимациите",
        value=True
    )

    sound_enabled = st.toggle(
        "Звукови ефекти",
        value=False
    )

    st.divider()

    st.markdown("### 📍 Информация")

    st.write("Версия: 2.0")
    st.write("Разработено със Streamlit")
    st.write("Автор: Temperature PRO")

    st.divider()

    st.markdown("### 📊 Статистика")

    st.metric(
        "Направени проверки",
        st.session_state.checks
    )

    st.metric(
        "Записани измервания",
        len(st.session_state.history)
    )


# ==========================================
# 5. HEADER
# ==========================================

st.markdown(
    '<div class="hero-title">'
    '🌡️ TEMPERATURE PRO'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'YOUR PERSONAL TEMPERATURE EXPERIENCE'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# ==========================================
# 6. NAVIGATION
# ==========================================

tab_home, tab_stats, tab_converter, tab_history, tab_about = st.tabs([
    "🏠 Начало",
    "📊 Статистика",
    "🔄 Конвертор",
    "📜 История",
    "ℹ️ За нас"
])


# ==========================================
# 7. HOME PAGE
# ==========================================

with tab_home:

    st.markdown("## 🌤️ Добре дошъл!")

    st.write(
        "Въведи температурата и получи "
        "персонализирана препоръка."
    )

    col1, col2 = st.columns([2, 1])

    with col1:

        temperature = st.number_input(
            "🌡️ Температура в градуси Celsius",
            min_value=-50.0,
            max_value=60.0,
            value=20.0,
            step=0.5
        )

        humidity = st.slider(
            "💧 Влажност (%)",
            min_value=0,
            max_value=100,
            value=50
        )

        wind = st.slider(
            "💨 Скорост на вятъра (km/h)",
            min_value=0,
            max_value=150,
            value=10
        )

    with col2:

        st.markdown("### 📍 Твоите показатели")

        st.metric(
            "Температура",
            f"{temperature:.1f} °C"
        )

        st.metric(
            "Влажност",
            f"{humidity}%"
        )

        st.metric(
            "Вятър",
            f"{wind} km/h"
        )

    st.markdown("")

    check = st.button(
        "🚀 АНАЛИЗИРАЙ ТЕМПЕРАТУРАТА",
        use_container_width=True
    )

    if check:

        info = get_temperature_info(temperature)

        record = {
            "Дата": datetime.now().strftime(
                "%d.%m.%Y %H:%M:%S"
            ),
            "Температура": temperature,
            "Влажност": humidity,
            "Вятър": wind,
            "Категория": info["category"]
        }

        st.session_state.history.append(record)

        st.session_state.last_result = {
            **record,
            **info
        }

        st.session_state.checks += 1

        if show_animation:

            if temperature < 10:
                st.snow()

            elif temperature < 20:
                st.toast("🌥️ Прохладно време!")

            elif temperature < 30:
                st.balloons()

            else:
                st.toast("🔥 Внимавай с жегата!")

    # DISPLAY RESULT

    result = st.session_state.last_result

    if result:

        st.markdown("---")

        st.markdown("## ✨ Резултат от анализа")

        icon = result["emoji"]

        animation_class = get_weather_animation(
            result["Температура"]
        )

        if show_animation:

            st.markdown(
                f'<div class="weather-icon {animation_class}-icon">'
                f'{icon}'
                f'</div>',
                unsafe_allow_html=True
            )

        st.markdown(
            f'<div class="glass-card">'
            f'<h2 style="text-align:center;">'
            f'{result["category"]}'
            f'</h2>'
            f'<h3 style="text-align:center;">'
            f'{result["message"]}'
            f'</h3>'
            f'<p style="text-align:center;">'
            f'{result["advice"]}'
            f'</p>'
            f'</div>',
            unsafe_allow_html=True
        )

        st.write("")

        a, b, c = st.columns(3)

        a.metric(
            "🌡️ Celsius",
            f'{result["Температура"]:.1f} °C'
        )

        b.metric(
            "🔥 Fahrenheit",
            f'{celsius_to_fahrenheit(result["Температура"]):.1f} °F'
        )

        c.metric(
            "🧪 Kelvin",
            f'{celsius_to_kelvin(result["Температура"]):.2f} K'
        )

        st.markdown("### 📈 Температурна скала")

        st.progress(
            get_progress(result["Температура"])
        )

        st.caption(
            "Диапазон на скалата: от -50°C до 60°C."
        )

        st.markdown("### 💡 Персонални препоръки")

        for advice in get_extra_advice(
            result["Температура"]
        ):
            st.write(f"✅ {advice}")

        st.markdown("### 📋 Допълнителна информация")

        st.write(
            get_temperature_description(
                result["Температура"]
            )
        )

        st.write(
            f'💧 Влажност: {result["Влажност"]}%'
        )

        st.write(
            f'💨 Вятър: {result["Вятър"]} km/h'
        )

        st.caption(
            "Забележка: това е препоръка по въведените "
            "стойности, а не реална метеорологична прогноза."
        )

    else:

        st.info(
            "👆 Въведи температура и натисни бутона "
            "за първия си анализ!"
        )


# ==========================================
# 8. STATISTICS PAGE
# ==========================================

with tab_stats:

    st.markdown("## 📊 Температурна статистика")

    if st.session_state.history:

        df = pd.DataFrame(
            st.session_state.history
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Средна температура",
            f'{df["Температура"].mean():.1f} °C'
        )

        col2.metric(
            "Най-висока",
            f'{df["Температура"].max():.1f} °C'
        )

        col3.metric(
            "Най-ниска",
            f'{df["Температура"].min():.1f} °C'
        )

        st.markdown("### 📈 Графика на измерванията")

        fig = px.line(
            df,
            x=df.index,
            y="Температура",
            markers=True,
            title="История на температурите",
            template="plotly_dark"
        )

        fig.update_traces(
            line=dict(
                color="#8b5cf6",
                width=4
            ),
            marker=dict(size=10)
        )

        fig.update_layout(
            xaxis_title="Номер на измерване",
            yaxis_title="Температура (°C)",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("### 📊 Разпределение")

        category_counts = df["Категория"].value_counts()

        fig2 = px.pie(
            names=category_counts.index,
            values=category_counts.values,
            hole=0.5,
            title="Категории температури",
            template="plotly_dark"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    else:

        st.info(
            "Все още няма данни. Направи няколко "
            "измервания в началната страница."
        )


# ==========================================
# 9. CONVERTER PAGE
# ==========================================

with tab_converter:

    st.markdown("## 🔄 Температурен конвертор")

    st.write(
        "Преобразувай температурата между "
        "Celsius, Fahrenheit и Kelvin."
    )

    converter_temp = st.number_input(
        "Въведи стойност в Celsius:",
        min_value=-273.15,
        max_value=100000.0,
        value=25.0,
        step=1.0,
        key="converter_input"
    )

    if converter_temp < -273.15:
        st.error(
            "Температурата не може да бъде под абсолютната нула."
        )
    else:

        x, y, z = st.columns(3)

        x.metric(
            "Celsius",
            f"{converter_temp:.2f} °C"
        )

        y.metric(
            "Fahrenheit",
            f"{celsius_to_fahrenheit(converter_temp):.2f} °F"
        )

        z.metric(
            "Kelvin",
            f"{celsius_to_kelvin(converter_temp):.2f} K"
        )

        st.success(
            "✅ Преобразуването е успешно!"
        )


# ==========================================
# 10. HISTORY PAGE
# ==========================================

with tab_history:

    st.markdown("## 📜 История на измерванията")

    if st.session_state.history:

        history_df = pd.DataFrame(
            st.session_state.history
        )

        st.dataframe(
            history_df,
            use_container_width=True,
            hide_index=True
        )

        csv = history_df.to_csv(
            index=False
        ).encode("utf-8-sig")

        st.download_button(
            "⬇️ Изтегли историята като CSV",
            data=csv,
            file_name="temperature_history.csv",
            mime="text/csv",
            use_container_width=True
        )

        if st.button(
            "🗑️ Изчисти историята",
            use_container_width=True
        ):

            st.session_state.history = []
            st.session_state.last_result = None

            st.rerun()

    else:

        st.info(
            "Няма записани измервания."
        )


# ==========================================
# 11. ABOUT PAGE
# ==========================================

with tab_about:

    st.markdown("## ℹ️ За Temperature PRO")

    st.markdown(
        """
        <div class="glass-card">
            <h2>🌡️ TEMPERATURE PRO</h2>
            <p>
                Интерактивен температурен помощник,
                създаден с Python и Streamlit.
            </p>
            <p>
                Приложението анализира въведени температури,
                показва препоръки и визуализира статистика.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🚀 Използвани технологии")

    st.write("🐍 Python")
    st.write("🎨 CSS")
    st.write("📊 Plotly")
    st.write("⚡ Streamlit")
    st.write("🐼 Pandas")

    st.markdown("### ⭐ Основни функции")

    features = [
        "Температурен анализ",
        "Анимиран интерфейс",
        "Статистически графики",
        "Конвертиране на температури",
        "История на измерванията",
        "Експорт на данни",
        "Персонални препоръки"
    ]

    for feature in features:
        st.write(f"✅ {feature}")


# ==========================================
# 12. FOOTER
# ==========================================

st.markdown("---")

st.markdown(
    """
    <div class="custom-footer">
        <h3 class="footer-glow">
            🌡️ TEMPERATURE PRO
        </h3>
        <p>
            Ultimate Temperature Experience
        </p>
        <p>
            Made with ❤️ using Python & Streamlit
        </p>
        <p>
            © 2026 Temperature PRO
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

