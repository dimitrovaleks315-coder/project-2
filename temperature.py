
def get_temperature_info(temp):
    if temp < 0:
        return {
            "category": "Екстремен студ",
            "emoji": "🥶",
            "message": "Температурата е под нулата!",
            "advice": "Облечи дебело зимно яке, шапка и ръкавици.",
            "color": "#60a5fa",
            "status": "Много студено"
        }

    elif temp < 10:
        return {
            "category": "Студено време",
            "emoji": "❄️",
            "message": "Навън е доста студено!",
            "advice": "Препоръчваме топло яке и затворени обувки.",
            "color": "#38bdf8",
            "status": "Студено"
        }

    elif temp < 20:
        return {
            "category": "Прохладно време",
            "emoji": "🌥️",
            "message": "Температурата е прохладна.",
            "advice": "Леко яке или суичър ще бъдат подходящи.",
            "color": "#a78bfa",
            "status": "Прохладно"
        }

    elif temp < 30:
        return {
            "category": "Приятно време",
            "emoji": "☀️",
            "message": "Чудесно време за разходка!",
            "advice": "Избери леки и удобни дрехи.",
            "color": "#34d399",
            "status": "Приятно"
        }

    elif temp < 40:
        return {
            "category": "Горещо време",
            "emoji": "🔥",
            "message": "Навън е доста горещо!",
            "advice": "Пий вода и стой на сянка.",
            "color": "#fb923c",
            "status": "Горещо"
        }

    else:
        return {
            "category": "Екстремна жега",
            "emoji": "🌋",
            "message": "Изключително висока температура!",
            "advice": "Избягвай продължителния престой навън.",
            "color": "#ef4444",
            "status": "Екстремна жега"
        }


def celsius_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


def celsius_to_kelvin(temp):
    return temp + 273.15


def get_progress(temp):
    return max(0.0, min(1.0, (temp + 50) / 110))


def get_extra_advice(temp):
    if temp < 0:
        return [
            "Пази се от заледени повърхности.",
            "Носи топли обувки.",
            "Ограничи продължителния престой навън."
        ]

    elif temp < 10:
        return [
            "Избери топли дрехи.",
            "Носи подходящи обувки.",
            "Вземи си шал."
        ]

    elif temp < 20:
        return [
            "Вземи леко яке.",
            "Подходящо време за разходка.",
            "Провери прогнозата преди излизане."
        ]

    elif temp < 30:
        return [
            "Подходящо време за активности навън.",
            "Носи слънчеви очила при силно слънце.",
            "Пий достатъчно вода."
        ]

    else:
        return [
            "Пий редовно вода.",
            "Стой на сянка.",
            "Избягвай физически натоварвания в най-горещите часове."
        ]


def get_weather_animation(temp):
    if temp < 10:
        return "snow"

    elif temp < 20:
        return "cloud"

    elif temp < 30:
        return "sun"

    else:
        return "fire"


def calculate_temperature_difference(temp1, temp2):
    return abs(temp1 - temp2)


def get_temperature_description(temp):
    if temp < 0:
        return "Температура под нулата."

    elif temp < 10:
        return "Ниска температура."

    elif temp < 20:
        return "Умерено прохладна температура."

    elif temp < 30:
        return "Комфортна температура."

    elif temp < 40:
        return "Висока температура."

    else:
        return "Изключително висока температура."
