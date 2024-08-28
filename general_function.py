import random


def get_info():
    images_headers = [
        "1_header.jpg",
        "2_header.jpg",
        "3_header.jpg",
        "4_header.jpg",
        "5_header.jpg",
        "6_header.jpg",
    ]
    images_ears = [
        "1_ears.jpg",
        "2_ears.jpg",
        "3_ears.jpg",
        "4_ears.jpg",
        "5_ears.jpg",
        "6_ears.jpg",
    ]
    images_eyes = [
        "1_eyes.jpg",
        "2_eyes.jpg",
        "3_eyes.jpg",
        "4_eyes.jpg",
        "5_eyes.jpg",
        "6_eyes.jpg",
    ]
    images_nose = [
        "1_nose.jpg",
        "2_nose.jpg",
        "3_nose.jpg",
    ]
    images_mouse = [
        "1_mouse.jpg",
        "2_mouse.jpg",
        "3_mouse.jpg",
        "4_mouse.jpg",
        "5_mouse.jpg",
    ]
    images_hairstyle = [
        "1_hairstyle.jpg",
        "2_hairstyle.jpg",
        "3_hairstyle.jpg",
        "4_hairstyle.jpg",
        "5_hairstyle.jpg",
        "6_hairstyle.jpg",
    ]
    images_body = [
        "1_body.jpg",
        "2_body.jpg",
        "3_body.jpg",
        "4_body.jpg",
        "5_body.jpg",
        "6_body.jpg",
    ]
    styles = [
        "Счастливая, спокойная, милая.",
        "Злая, дерзкая.",
        "Спокойная, милосердная",
        "Мятный кексик",
        "Готический стиль",
        "Деловой стиль",
        "Гоблин кор",
        "Фарфоровая девочка",
        "Спортивная",
        "Школьная",
        "Тёплая одежда",
        "Оверсайз",
        "Смолсайз",
        "Кингуруми",
        "Платье на бал",
        "Платье",
        "Меховая одежда",
        "Пляжный костюм",
        "Купальник",
        "Спокойный",
        "Лолита",
    ]
    images_color_scheme = [
        "1_color_scheme.jpg",
        "2_color_scheme.jpg",
        "3_color_scheme.jpg",
        "4_color_scheme.jpg",
        "5_color_scheme.jpg",
        "6_color_scheme.jpg",
        "7_color_scheme.jpg",
        "8_color_scheme.jpg",
        "9_color_scheme.jpg",
        "10_color_scheme.jpg",
    ]
    material = [
        "Карандаши",
        "Ручки",
        "Акварель",
        "Гуашь",
        "Пастель",
        "Акварельные карандаши",
        "Свой матерьял",
        "Скетчмаркеры",
        "Любой мательял",
    ]

    variables = {
        "Голова": images_headers,
        "Уши": images_ears,
        "Глаза": images_eyes,
        "Нос": images_nose,
        "Рот": images_mouse,
        "Причёска": images_hairstyle,
        "Тело": images_body,
        "Style": styles,
        "Цветовая гамма": images_color_scheme,
        "Матерьял": material,
    }

    return variables


def fetch_cards():
    cards = []
    variables = get_info()

    for variable in variables:
        random_variable = random.choice(variables[variable])

        one_cards = {
            "type": variable,
            "info": random_variable,
        }

        cards.append(one_cards)

    return cards
