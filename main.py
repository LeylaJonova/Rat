from kivy.app import App  # App запускає застосунок і надає доступ до нього з екранів.
from kivy.uix.screenmanager import Screen, ScreenManager  # Screen є базою для екрана; ScreenManager перемикає екрани.
from kivy.core.window import Window  # Window дає змогу налаштувати розмір вікна програми.
from kivy.lang import Builder  # Builder завантажує розмітку інтерфейсу мовою KV.
from kivy.animation import Animation  # Animation плавно змінює властивості віджетів у часі.
from kivy.metrics import dp  # dp задає розміри з урахуванням щільності екрана.
from kivy.uix.image import Image  # Image відображає файл зображення.
from kivy.uix.boxlayout import BoxLayout  # BoxLayout розміщує дочірні віджети в ряд або стовпець.
from kivy.uix.label import Label  # Label показує текст.
from kivy.uix.button import Button  # Button створює кнопку з дією натискання.
from kivy import platform  # platform повідомляє, де запущена програма.
from kivy.properties import NumericProperty, BooleanProperty  # Властивості Kivy стежать за числами та True/False і оновлюють інтерфейс.
from kivy.clock import Clock  # Clock запускає повторювані та відкладені дії.
from kivy.core.audio import SoundLoader  # SoundLoader завантажує звукові файли.
from kivy.uix.widget import Widget  # Widget — базовий клас елементів інтерфейсу.
import json  # json читає й записує прогрес у форматі JSON.
import os  # os працює зі шляхами та файлами.
import random  # random генерує випадкові числа для ефектів.

Builder.load_string(r"""
#:import dp kivy.metrics.dp

# Описуємо елементи головного меню.
<Menu>:
    # Контейнер для вільного розташування елементів.
    FloatLayout:
        # Віджет показує зображення.
        Image:
            # Шлях до файлу зображення або фону.
            source: "assets/images/back_menu_title.png"
            # Ширина та висота елемента.
            size: root.size
            # Координати лівого нижнього кута елемента.
            pos: root.pos
            # Дозволяє розтягнути зображення до розміру віджета.
            allow_stretch: True
            # Зберігає пропорції зображення під час масштабування.
            keep_ratio: False

        # Віджет показує зображення.
        Image:
            # Шлях до файлу зображення або фону.
            source: "assets/images/title.png"
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(440), dp(160)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "center_y": .75}
            # Дозволяє розтягнути зображення до розміру віджета.
            allow_stretch: True
            # Зберігає пропорції зображення під час масштабування.
            keep_ratio: True

        # Кнопка виконує дію після натискання.
        Button:
            # Текст, який показує цей елемент.
            text: "PLAY"
            # Розмір літер.
            font_size: dp(22)
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(280), dp(60)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "center_y": .50}
            # Зображення тла кнопки; порожнє значення прибирає стандартну текстуру.
            background_normal: ""
            # Колір тла кнопки у форматі RGBA.
            background_color: .5, .5, .5,  1   
            # Команда після відпускання натиснутої кнопки.
            on_release: root.go_level_select()

        # Кнопка виконує дію після натискання.
        Button:
            # Текст, який показує цей елемент.
            text: "SETTINGS"
            # Розмір літер.
            font_size: dp(20)
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(280), dp(55)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "center_y": .37}
            # Зображення тла кнопки; порожнє значення прибирає стандартну текстуру.
            background_normal: ""
            # Колір тла кнопки у форматі RGBA.
            background_color: .5, .5, .5,  1
            # Команда після відпускання натиснутої кнопки.
            on_release: root.go_settings()

        # Кнопка виконує дію після натискання.
        Button:
            # Текст, який показує цей елемент.
            text: "EXIT"
            # Розмір літер.
            font_size: dp(20)
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(280), dp(55)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "center_y": .24}
            # Зображення тла кнопки; порожнє значення прибирає стандартну текстуру.
            background_normal: ""
            # Колір тла кнопки у форматі RGBA.
            background_color: .5, .5, .5, 1
            # Команда після відпускання натиснутої кнопки.
            on_release: root.exit_app()


# Описуємо елементи вибору рівня.
<LevelSelect>:
    # Контейнер для вільного розташування елементів.
    FloatLayout:
        # Віджет показує зображення.
        Image:
            # Шлях до файлу зображення або фону.
            source: "assets/images/back_menu_title.png"
            # Ширина та висота елемента.
            size: root.size
            # Координати лівого нижнього кута елемента.
            pos: root.pos
            # Дозволяє розтягнути зображення до розміру віджета.
            allow_stretch: True
            # Зберігає пропорції зображення під час масштабування.
            keep_ratio: False

        # Напис SELECT LEVEL опустили нижче, щоб він не накладався на заголовок
        # Напис показує текст.
        Label:
            # Текст, який показує цей елемент.
            text: "SELECT LEVEL"
            # Розмір літер.
            font_size: dp(28)
            # Вмикає жирний шрифт.
            bold: True
            # Колір тексту у форматі RGBA.
            color: 1, 1, 1, 1
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: 1, None
            # Висота елемента.
            height: dp(40)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "center_y": .8}

        # Список рівнів трохи нижче заголовка
        # Контейнер дає прокручувати вміст.
        ScrollView:
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(280), dp(220)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "center_y": .46}
            
            # Сітка розміщує елементи по рядках і стовпцях.
            GridLayout:
                # Ім’я віджета для доступу з Python через ids.
                id: levels_grid
                # Кількість стовпців сітки.
                cols: 1
                # Висота відносно контейнера; None дозволяє задати вручну.
                size_hint_y: None
                # Висота елемента.
                height: self.minimum_height
                # Відстань між дочірніми віджетами.
                spacing: dp(10)
                # Внутрішній відступ контейнера.
                padding: dp(5)

        # Кнопка виконує дію після натискання.
        Button:
            # Текст, який показує цей елемент.
            text: "BACK"
            # Розмір літер.
            font_size: dp(20)
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(280), dp(55)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "center_y": .24}
            # Зображення тла кнопки; порожнє значення прибирає стандартну текстуру.
            background_normal: ""
            # Колір тла кнопки у форматі RGBA.
            background_color: .5, .5, .5,  1
            # Команда після відпускання натиснутої кнопки.
            on_release: root.go_menu()


# Описуємо елементи налаштувань.
<Settings>:
    # Контейнер для вільного розташування елементів.
    FloatLayout:
        # Віджет показує зображення.
        Image:
            # Шлях до файлу зображення або фону.
            source: "assets/images/back_menu_title.png"
            # Ширина та висота елемента.
            size: root.size
            # Координати лівого нижнього кута елемента.
            pos: root.pos
            # Дозволяє розтягнути зображення до розміру віджета.
            allow_stretch: True
            # Зберігає пропорції зображення під час масштабування.
            keep_ratio: False

        # Напис показує текст.
        Label:
            # Текст, який показує цей елемент.
            text: "SETTINGS"
            # Розмір літер.
            font_size: dp(38)
            # Вмикає жирний шрифт.
            bold: True
            # Колір тексту у форматі RGBA.
            color: 1, 1, 1, 1
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: 1, None
            # Висота елемента.
            height: dp(55)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "top": .85}

        # Напис показує текст.
        Label:
            # Текст, який показує цей елемент.
            text: "Sound volume: " + str(int(app.volume * 100)) + "%"
            # Розмір літер.
            font_size: dp(21)
            # Колір тексту у форматі RGBA.
            color: 1, 1, 1, 1
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(250), dp(45)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "center_y": .75}

        # Повзунок вибирає числове значення.
        Slider:
            # Найменше значення повзунка.
            min: 0
            # Найбільше значення повзунка.
            max: 1
            # Поточне значення властивості.
            value: app.volume
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(280), dp(45)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "center_y": .52}
            # Команда після зміни значення повзунка.
            on_value: app.set_volume(self.value)

        # Кнопка виконує дію після натискання.
        Button:
            # Текст, який показує цей елемент.
            text: "RESET PROGRESS"
            # Розмір літер.
            font_size: dp(18)
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(280), dp(50)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "center_y": .38}
            # Зображення тла кнопки; порожнє значення прибирає стандартну текстуру.
            background_normal: ""
            # Колір тла кнопки у форматі RGBA.
            background_color: .85, .25, .25, 1
            # Команда після відпускання натиснутої кнопки.
            on_release: root.reset_progress_data()

        # Кнопка виконує дію після натискання.
        Button:
            # Текст, який показує цей елемент.
            text: "BACK"
            # Розмір літер.
            font_size: dp(20)
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(280), dp(55)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "center_y": .24}
            # Зображення тла кнопки; порожнє значення прибирає стандартну текстуру.
            background_normal: ""
            # Колір тла кнопки у форматі RGBA.
            background_color: .5, .5, .5,  1
            # Команда після відпускання натиснутої кнопки.
            on_release: root.go_back()


# Описуємо елементи гри.
<Game>:
    # Контейнер для вільного розташування елементів.
    FloatLayout:
        # Віджет показує зображення.
        Image:
            # Ім’я віджета для доступу з Python через ids.
            id: level_bg
            # Шлях до файлу зображення або фону.
            source: "assets/images/level1.png"
            # Ширина та висота елемента.
            size: root.size
            # Координати лівого нижнього кута елемента.
            pos: root.pos
            # Дозволяє розтягнути зображення до розміру віджета.
            allow_stretch: True
            # Зберігає пропорції зображення під час масштабування.
            keep_ratio: False

        # Напис показує текст.
        Label:
            # Ім’я віджета для доступу з Python через ids.
            id: level_title
            # Текст, який показує цей елемент.
            text: "Level 1"
            # Розмір літер.
            font_size: dp(45)
            # Вмикає жирний шрифт.
            bold: True
            # Колір тексту у форматі RGBA.
            color: 1, 1, 1, 1
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: 1, None
            # Висота елемента.
            height: dp(60)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "top": .85}
            # Прозорість: 0 — невидимий, 1 — повністю видимий.
            opacity: 0

        # Напис показує текст.
        Label:
            # Текст, який показує цей елемент.
            text: str(root.score)
            # Розмір літер.
            font_size: dp(48)
            # Вмикає жирний шрифт.
            bold: True
            # Колір тексту у форматі RGBA.
            color: 1, 1, 1, 1
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(100), dp(60)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"x": .05, "top": .95}

        # Напис показує текст.
        Label:
            # Текст, який показує цей елемент.
            text: str(root.elapsed_time) + "s"
            # Розмір літер.
            font_size: dp(44)
            # Вмикає жирний шрифт.
            bold: True
            # Колір тексту у форматі RGBA.
            color: 1, 1, 1, 1
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(120), dp(60)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"right": .95, "top": .95}

        # Напис показує текст.
        Label:
            # Ім’я віджета для доступу з Python через ids.
            id: stars_hint_label
            # Текст, який показує цей елемент.
            text: ""
            # Це значення налаштовує вигляд або поведінку віджета.
            font_name: "DejaVuSans.ttf"
            # Розмір літер.
            font_size: dp(16)
            # Вмикає жирний шрифт.
            bold: True
            # Колір тексту у форматі RGBA.
            color: 1, 0.9, 0.4, 0.9
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: 1, None
            # Висота елемента.
            height: dp(30)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "top": .93}

        # Контейнер для вільного розташування елементів.
        FloatLayout:
            # Ім’я віджета для доступу з Python через ids.
            id: game_window
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: 1, .76
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"x": 0, "y": .12}

            # Віджет риби, на яку натискає гравець.
            Rat:
                # Ім’я віджета для доступу з Python через ids.
                id: rat
                # Частка доступного розміру; None означає ручне задання розміру.
                size_hint: None, None
                # Ширина та висота елемента.
                size: dp(200), dp(200)

        # Напис показує текст.
        Label:
            # Ім’я віджета для доступу з Python через ids.
            id: level_complete
            # Текст, який показує цей елемент.
            text: ""
            # Розмір літер.
            font_size: dp(40)
            # Вмикає жирний шрифт.
            bold: True
            # Колір тексту у форматі RGBA.
            color: 0.07, 0.95, 0.68, 1
            # Вирівнювання тексту по горизонталі.
            halign: "center"
            # Вирівнювання тексту по вертикалі.
            valign: "middle"
            # Область, у якій розміщується текст.
            text_size: self.size
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: 1, None
            # Висота елемента.
            height: dp(120)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "center_y": .62}
            # Прозорість: 0 — невидимий, 1 — повністю видимий.
            opacity: 0

        # Контейнер розташовує елементи в ряд або стовпець.
        BoxLayout:
            # Ім’я віджета для доступу з Python через ids.
            id: stars_container
            # Напрямок розміщення дочірніх віджетів.
            orientation: "horizontal"
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(180), dp(50)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "center_y": .48}
            # Відстань між дочірніми віджетами.
            spacing: dp(10)
            # Прозорість: 0 — невидимий, 1 — повністю видимий.
            opacity: 0

        # Кнопка виконує дію після натискання.
        Button:
            # Ім’я віджета для доступу з Python через ids.
            id: retry_button
            # Текст, який показує цей елемент.
            text: "AGAIN"
            # Розмір літер.
            font_size: dp(18)
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(130), dp(50)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .35, "center_y": .34}
            # Прозорість: 0 — невидимий, 1 — повністю видимий.
            opacity: 0
            # True вимикає кнопку; False дозволяє натискати.
            disabled: True
            # Зображення тла кнопки; порожнє значення прибирає стандартну текстуру.
            background_normal: ""
            # Колір тла кнопки у форматі RGBA.
            background_color: .5, .5, .5,  1
            # Команда після відпускання натиснутої кнопки.
            on_release: root.retry_level()

        # Кнопка виконує дію після натискання.
        Button:
            # Ім’я віджета для доступу з Python через ids.
            id: next_button
            # Текст, який показує цей елемент.
            text: "NEXT LEVEL"
            # Розмір літер.
            font_size: dp(18)
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(150), dp(50)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .67, "center_y": .34}
            # Прозорість: 0 — невидимий, 1 — повністю видимий.
            opacity: 0
            # True вимикає кнопку; False дозволяє натискати.
            disabled: True
            # Зображення тла кнопки; порожнє значення прибирає стандартну текстуру.
            background_normal: ""
            # Колір тла кнопки у форматі RGBA.
            background_color: 0.07, 0.95, 0.68, 1
            # Команда після відпускання натиснутої кнопки.
            on_release: root.next_level()

        # Кнопка виконує дію після натискання.
        Button:
            # Текст, який показує цей елемент.
            text: "LEVELS"
            # Розмір літер.
            font_size: dp(15)
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(100), dp(45)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"x": .05, "y": .03}
            # Зображення тла кнопки; порожнє значення прибирає стандартну текстуру.
            background_normal: ""
            # Колір тла кнопки у форматі RGBA.
            background_color: .5, .5, .5,  1
            # Команда після відпускання натиснутої кнопки.
            on_release: root.go_level_select()

        # Кнопка виконує дію після натискання.
        Button:
            # Текст, який показує цей елемент.
            text: "SETTINGS"
            # Розмір літер.
            font_size: dp(15)
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(110), dp(45)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"right": .95, "y": .03}
            # Зображення тла кнопки; порожнє значення прибирає стандартну текстуру.
            background_normal: ""
            # Колір тла кнопки у форматі RGBA.
            background_color: .5, .5, .5,  1
            # Команда після відпускання натиснутої кнопки.
            on_release: root.go_settings()


# Описуємо елементи перемоги.
<VictoryScreen>:
    # Контейнер для вільного розташування елементів.
    FloatLayout:
        # Віджет показує зображення.
        Image:
            # Шлях до файлу зображення або фону.
            source: "assets/images/back_menu_title.png"
            # Ширина та висота елемента.
            size: root.size
            # Координати лівого нижнього кута елемента.
            pos: root.pos
            # Дозволяє розтягнути зображення до розміру віджета.
            allow_stretch: True
            # Зберігає пропорції зображення під час масштабування.
            keep_ratio: False

        # Віджет показує зображення.
        Image:
            # Ім’я віджета для доступу з Python через ids.
            id: giant_star
            # Шлях до файлу зображення або фону.
            source: "assets/images/star.png"
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(100), dp(100)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "center_y": .60}
            # Прозорість: 0 — невидимий, 1 — повністю видимий.
            opacity: 0

        # Напис показує текст.
        Label:
            # Текст, який показує цей елемент.
            text: "GAME COMPLETE!"
            # Розмір літер.
            font_size: dp(28)
            # Вмикає жирний шрифт.
            bold: True
            # Колір тексту у форматі RGBA.
            color: 0.07, 0.95, 0.68, 1
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: 1, None
            # Висота елемента.
            height: dp(40)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "top": .73}

        # Контейнер розташовує елементи в ряд або стовпець.
        BoxLayout:
            # Ім’я віджета для доступу з Python через ids.
            id: results_list
            # Напрямок розміщення дочірніх віджетів.
            orientation: "vertical"
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(320), dp(220)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "center_y": .48}
            # Відстань між дочірніми віджетами.
            spacing: dp(10)

        # Кнопка виконує дію після натискання.
        Button:
            # Текст, який показує цей елемент.
            text: "MAIN MENU"
            # Розмір літер.
            font_size: dp(20)
            # Частка доступного розміру; None означає ручне задання розміру.
            size_hint: None, None
            # Ширина та висота елемента.
            size: dp(280), dp(55)
            # Розташування відносно контейнера; частки від 0 до 1.
            pos_hint: {"center_x": .5, "center_y": .24}
            # Зображення тла кнопки; порожнє значення прибирає стандартну текстуру.
            background_normal: ""
            # Колір тла кнопки у форматі RGBA.
            background_color: .5, .5, .5,  1
            # Команда після відпускання натиснутої кнопки.
            on_release: root.go_menu()


# Описуємо елементи повороту зображення.
<RotatedImage>:
    # Графічні команди, що малюють до/після основного зображення.
    canvas.before:
        # Зберігаємо або відновлюємо стан малювання для повороту.
        PushMatrix
        # Починаємо вкладений елемент або задаємо його параметр.
        Rotate:
            # Кут повороту в градусах.
            angle: root.angle
            # Точка, навколо якої повертається віджет.
            origin: self.center
    # Графічні команди, що малюють до/після основного зображення.
    canvas.after:
        # Зберігаємо або відновлюємо стан малювання для повороту.
        PopMatrix
""")


class Menu(Screen):  # Оголошуємо клас — шаблон екрана або об’єкта.
    def go_level_select(self, *args):  # Переходимо на екран вибору рівнів.
        self.manager.transition.direction = "left"  # Задаємо значення властивості об’єкта.
        self.manager.current = "level_select"  # Задаємо значення властивості об’єкта.

    def go_settings(self, *args):  # Відкриваємо налаштування.
        self.manager.get_screen("settings").return_screen = "menu"  # Задаємо значення властивості об’єкта.
        self.manager.transition.direction = "up"  # Задаємо значення властивості об’єкта.
        self.manager.current = "settings"  # Задаємо значення властивості об’єкта.

    def exit_app(self, *args):  # Закриваємо застосунок.
        App.get_running_app().stop()  # Викликаємо функцію бібліотеки для таймера, анімації, звуку або роботи з файлами.


class LevelSelect(Screen):  # Оголошуємо клас — шаблон екрана або об’єкта.
    def on_enter(self, *args):  # Kivy викликає метод, коли екран з’являється.
        app = App.get_running_app()  # Обчислюємо й зберігаємо значення у змінній app.
        grid = self.ids.levels_grid  # Обчислюємо й зберігаємо значення у змінній grid.
        grid.clear_widgets()  # очищаємо дочірні віджети

        max_unlocked = app.progress.get("current_level", 0)  # Обчислюємо й зберігаємо значення у змінній max_unlocked.
        saved_stars = app.progress.get("stars", [])  # Обчислюємо й зберігаємо значення у змінній saved_stars.

        for i in range(len(app.LEVELS)):  # Повторюємо вкладені команди для кожного елемента послідовності.
            is_unlocked = i <= max_unlocked  # Обчислюємо й зберігаємо значення у змінній is_unlocked.

            row = BoxLayout(orientation="horizontal", size_hint=(1, None), height=dp(50), spacing=dp(10))  # Обчислюємо й зберігаємо значення у змінній row.

            btn = Button(  # Обчислюємо й зберігаємо значення у змінній btn.
                text=f"Level {i + 1}" if is_unlocked else f"Level {i + 1} (Locked)",  # Обчислюємо й зберігаємо значення у змінній text.
                font_size=dp(18),  # Обчислюємо й зберігаємо значення у змінній font_size.
                bold=True,  # Обчислюємо й зберігаємо значення у змінній bold.
                size_hint_x=0.6,  # Обчислюємо й зберігаємо значення у змінній size_hint_x.
                background_normal="",  # Обчислюємо й зберігаємо значення у змінній background_normal.
                background_color=(0.5, 0.5, 0.5, 1) if is_unlocked else (0.4, 0.4, 0.4, 1),  # Обчислюємо й зберігаємо значення у змінній background_color.
                disabled=not is_unlocked  # Обчислюємо й зберігаємо значення у змінній disabled.
            )  # Продовження багаторядкового виразу: вказуємо ще один аргумент або частину колекції.
            btn.level_index = i  # Обчислюємо й зберігаємо значення у змінній btn.level_index.
            btn.bind(on_release=self.start_selected_level)  # Обчислюємо й зберігаємо значення у змінній btn.bind(on_release.
            row.add_widget(btn)  # Викликаємо метод або функцію.

            stars_box = BoxLayout(orientation="horizontal", size_hint_x=0.4, spacing=dp(4))  # Обчислюємо й зберігаємо значення у змінній stars_box.
            if is_unlocked:  # Перевіряємо умову перед виконанням вкладених команд.
                got = saved_stars[i] if i < len(saved_stars) else 0  # Обчислюємо й зберігаємо значення у змінній got.
                for _ in range(got):  # Повторюємо вкладені команди для кожного елемента послідовності.
                    stars_box.add_widget(Image(source="assets/images/star.png", allow_stretch=True, keep_ratio=True))  # Обчислюємо й зберігаємо значення у змінній stars_box.add_widget(Image(source.

            row.add_widget(stars_box)  # Викликаємо метод або функцію.
            grid.add_widget(row)  # додаємо віджет до контейнера

    def start_selected_level(self, instance):  # Метод start_selected_level виконує окрему дію цього класу.
        app = App.get_running_app()  # Обчислюємо й зберігаємо значення у змінній app.
        app.LEVEL = instance.level_index  # Оновлюємо спільні дані головного застосунку.
        self.manager.transition.direction = "left"  # Задаємо значення властивості об’єкта.
        self.manager.current = "game"  # Задаємо значення властивості об’єкта.

    def go_menu(self):  # Метод go_menu виконує окрему дію цього класу.
        self.manager.transition.direction = "right"  # Задаємо значення властивості об’єкта.
        self.manager.current = "menu"  # Задаємо значення властивості об’єкта.


class Settings(Screen):  # Оголошуємо клас — шаблон екрана або об’єкта.
    return_screen = "menu"  # Обчислюємо й зберігаємо значення у змінній return_screen.

    def go_back(self, *args):  # Повертаємося на попередній екран.
        direction = "down" if self.return_screen == "menu" else "right"  # Обчислюємо й зберігаємо значення у змінній direction.
        self.manager.transition.direction = direction  # Задаємо значення властивості об’єкта.
        self.manager.current = self.return_screen  # Задаємо значення властивості об’єкта.

    def reset_progress_data(self):  # Скидаємо збережений прогрес.
        app = App.get_running_app()  # Обчислюємо й зберігаємо значення у змінній app.
        app.progress = {"current_level": 0, "volume": app.volume, "stars": []}  # Оновлюємо спільні дані головного застосунку.
        app.save_progress()  # зберігаємо прогрес


class VictoryScreen(Screen):  # Оголошуємо клас — шаблон екрана або об’єкта.
    def on_enter(self, *args):  # Kivy викликає метод, коли екран з’являється.
        app = App.get_running_app()  # Обчислюємо й зберігаємо значення у змінній app.
        container = self.ids.results_list  # Обчислюємо й зберігаємо значення у змінній container.
        container.clear_widgets()  # очищаємо дочірні віджети

        all_three_stars = True  # Обчислюємо й зберігаємо значення у змінній all_three_stars.
        saved_stars = app.progress.get("stars", [])  # Обчислюємо й зберігаємо значення у змінній saved_stars.

        for i, lvl in enumerate(app.LEVELS):  # Повторюємо вкладені команди для кожного елемента послідовності.
            row = BoxLayout(orientation="horizontal", size_hint=(1, None), height=dp(40), spacing=dp(10))  # Обчислюємо й зберігаємо значення у змінній row.

            lbl = Label(  # Обчислюємо й зберігаємо значення у змінній lbl.
                text=f"Level {i + 1}:",  # Обчислюємо й зберігаємо значення у змінній text.
                font_size=dp(18),  # Обчислюємо й зберігаємо значення у змінній font_size.
                bold=True,  # Обчислюємо й зберігаємо значення у змінній bold.
                color=(1, 1, 1, 1),  # Обчислюємо й зберігаємо значення у змінній color.
                size_hint_x=0.5  # Обчислюємо й зберігаємо значення у змінній size_hint_x.
            )  # Продовження багаторядкового виразу: вказуємо ще один аргумент або частину колекції.
            row.add_widget(lbl)  # Викликаємо метод або функцію.

            stars_box = BoxLayout(orientation="horizontal", size_hint_x=0.5, spacing=dp(5))  # Обчислюємо й зберігаємо значення у змінній stars_box.
            got_stars = saved_stars[i] if i < len(saved_stars) else 0  # Обчислюємо й зберігаємо значення у змінній got_stars.
            if got_stars < 3:  # Перевіряємо умову перед виконанням вкладених команд.
                all_three_stars = False  # Обчислюємо й зберігаємо значення у змінній all_three_stars.

            for _ in range(got_stars):  # Повторюємо вкладені команди для кожного елемента послідовності.
                stars_box.add_widget(Image(source="assets/images/star.png", allow_stretch=True, keep_ratio=True))  # Обчислюємо й зберігаємо значення у змінній stars_box.add_widget(Image(source.

            row.add_widget(stars_box)  # Викликаємо метод або функцію.
            container.add_widget(row)  # додаємо віджет до контейнера

        giant_star = self.ids.giant_star  # Обчислюємо й зберігаємо значення у змінній giant_star.
        giant_star.opacity = 0  # Обчислюємо й зберігаємо значення у змінній giant_star.opacity.
        giant_star.size = (dp(20), dp(20))  # Обчислюємо й зберігаємо значення у змінній giant_star.size.

        if all_three_stars:  # Перевіряємо умову перед виконанням вкладених команд.
            anim = (  # Обчислюємо й зберігаємо значення у змінній anim.
                           Animation(opacity=1, duration=0.3)  # Обчислюємо й зберігаємо значення у змінній Animation(opacity.
                           & Animation(size=(dp(120), dp(120)), duration=0.5, t="out_back")  # Обчислюємо й зберігаємо значення у змінній & Animation(size.
                   ) + (  # Продовження багаторядкового виразу: вказуємо ще один аргумент або частину колекції.
                       Animation(size=(dp(100), dp(100)), duration=0.2)  # Обчислюємо й зберігаємо значення у змінній Animation(size.
                   )  # Продовження багаторядкового виразу: вказуємо ще один аргумент або частину колекції.
            anim.start(giant_star)  # Викликаємо метод або функцію.

    def go_menu(self):  # Метод go_menu виконує окрему дію цього класу.
        self.manager.transition.direction = "right"  # Задаємо значення властивості об’єкта.
        self.manager.current = "menu"  # Задаємо значення властивості об’єкта.


class RotatedImage(Image):  # Оголошуємо клас — шаблон екрана або об’єкта.
    angle = NumericProperty(0)  # Обчислюємо й зберігаємо значення у змінній angle.


class Rat(RotatedImage):  # Оголошуємо клас — шаблон екрана або об’єкта.
    anim_play = False  # Обчислюємо й зберігаємо значення у змінній anim_play.
    interaction_block = True  # Обчислюємо й зберігаємо значення у змінній interaction_block.
    rat_current = None  # Обчислюємо й зберігаємо значення у змінній rat_current.
    rat_index = 0  # Обчислюємо й зберігаємо значення у змінній rat_index.
    hp_current = 0  # Обчислюємо й зберігаємо значення у змінній hp_current.

    click_music = SoundLoader.load("assets/audios/rat.mp3")  # Обчислюємо й зберігаємо значення у змінній click_music.
    defeat_music = SoundLoader.load("assets/audios/fish_def.ogg")  # Обчислюємо й зберігаємо значення у змінній defeat_music.

    def on_kv_post(self, base_widget):  # Метод on_kv_post виконує окрему дію цього класу.
        self.GAME_SCREEN = self.parent.parent.parent  # Задаємо значення властивості об’єкта.
        return super().on_kv_post(base_widget)  # Передаємо подію базовому класу Kivy для стандартної обробки.

    def new_rat(self, *args):  # Налаштовуємо та показуємо наступну рибу.
        app = App.get_running_app()  # Обчислюємо й зберігаємо значення у змінній app.
        if app.LEVEL >= len(app.LEVELS):  # Перевіряємо умову перед виконанням вкладених команд.
            return  # Завершуємо роботу методу.
        self.rat_current = app.LEVELS[app.LEVEL]["rat"][self.rat_index]  # Задаємо значення властивості об’єкта.
        self.source = app.RAT[self.rat_current]["source"]  # Задаємо значення властивості об’єкта.
        self.hp_current = app.RAT[self.rat_current]["hp"]  # Задаємо поточне здоров’я риби.
        self.swim()  # Виконуємо метод swim цього об’єкта.

    def swim(self):  # Метод swim виконує окрему дію цього класу.
        game = self.GAME_SCREEN  # Обчислюємо й зберігаємо значення у змінній game.
        self.stop_all_animations()  # зупиняємо анімації віджета
        self.size = (dp(200), dp(200))  # Задаємо розмір віджета.
        self.angle = 0  # Задаємо кут повороту.
        self.pos = (-self.width, game.height * .40)  # Задаємо координати віджета.
        self.opacity = 1  # Задаємо прозорість елемента.
        self.interaction_block = True  # Задаємо значення властивості об’єкта.

        swim = Animation(  # Обчислюємо й зберігаємо значення у змінній swim.
            x=game.width / 2 - self.width / 2,  # Обчислюємо й зберігаємо значення у змінній x.
            duration=.8,  # Обчислюємо й зберігаємо значення у змінній duration.
            t="out_quad"  # Обчислюємо й зберігаємо значення у змінній t.
        )  # Продовження багаторядкового виразу: вказуємо ще один аргумент або частину колекції.
        swim.bind(on_complete=lambda *_: setattr(self, "interaction_block", False))  # Обчислюємо й зберігаємо значення у змінній swim.bind(on_complete.
        swim.start(self)  # Викликаємо метод або функцію.

    def stop_all_animations(self):  # Метод stop_all_animations виконує окрему дію цього класу.
        Animation.cancel_all(self)  # Створюємо віджет або анімацію з указаними параметрами.

    def defeated(self):  # Запускаємо анімацію переможеної риби.
        self.interaction_block = True  # Задаємо значення властивості об’єкта.
        old_size = self.size  # Обчислюємо й зберігаємо значення у змінній old_size.
        old_pos = self.pos  # Обчислюємо й зберігаємо значення у змінній old_pos.
        new_size = (self.width * 1.8, self.height * 1.8)  # Обчислюємо й зберігаємо значення у змінній new_size.
        new_pos = (  # Обчислюємо й зберігаємо значення у змінній new_pos.
            self.x - (new_size[0] - self.width) / 2,  # Виконуємо метод x -  цього об’єкта.
            self.y - (new_size[1] - self.height) / 2  # Виконуємо метод y -  цього об’єкта.
        )  # Продовження багаторядкового виразу: вказуємо ще один аргумент або частину колекції.

        anim = (  # Обчислюємо й зберігаємо значення у змінній anim.
                       Animation(angle=self.angle + 360, duration=.45, t="in_cubic")  # Обчислюємо й зберігаємо значення у змінній Animation(angle.
                       & Animation(size=new_size, pos=new_pos, duration=.45, t="out_back")  # Обчислюємо й зберігаємо значення у змінній & Animation(size.
               ) + Animation(opacity=0, duration=.25)  # Обчислюємо й зберігаємо значення у змінній ) + Animation(opacity.

        def restore(*_):  # Метод restore виконує окрему дію цього класу.
            self.size = old_size  # Задаємо розмір віджета.
            self.pos = old_pos  # Задаємо координати віджета.
            self.angle = 0  # Задаємо кут повороту.

        anim.bind(on_complete=restore)  # Обчислюємо й зберігаємо значення у змінній anim.bind(on_complete.
        anim.start(self)  # Викликаємо метод або функцію.

        app = App.get_running_app()  # Обчислюємо й зберігаємо значення у змінній app.
        if app.sound_enabled and self.defeat_music:  # Перевіряємо умову перед виконанням вкладених команд.
            self.defeat_music.play()  # починаємо відтворення звуку

    def on_touch_down(self, touch):  # Обробляємо натискання пальцем або мишею.
        if not self.collide_point(*touch.pos):  # Перевіряємо умову перед виконанням вкладених команд.
            return super().on_touch_down(touch)  # Передаємо подію базовому класу Kivy для стандартної обробки.

        if self.anim_play or self.interaction_block or not self.GAME_SCREEN.game_active:  # Перевіряємо умову перед виконанням вкладених команд.
            return True  # Повертаємо результат виклику.

        app = App.get_running_app()  # Обчислюємо й зберігаємо значення у змінній app.
        self.hp_current -= 1  # Задаємо значення властивості об’єкта.
        self.GAME_SCREEN.score += 1  # Задаємо значення властивості об’єкта.

        if app.sound_enabled and self.click_music:  # Перевіряємо умову перед виконанням вкладених команд.
            self.click_music.play()  # починаємо відтворення звуку

        if self.hp_current > 0:  # Перевіряємо умову перед виконанням вкладених команд.
            old_size = self.size  # Обчислюємо й зберігаємо значення у змінній old_size.
            old_pos = self.pos  # Обчислюємо й зберігаємо значення у змінній old_pos.
            new_size = (self.width * 1.15, self.height * 1.15)  # Обчислюємо й зберігаємо значення у змінній new_size.
            new_pos = (  # Обчислюємо й зберігаємо значення у змінній new_pos.
                self.x - (new_size[0] - self.width) / 2,  # Виконуємо метод x -  цього об’єкта.
                self.y - (new_size[1] - self.height) / 2  # Виконуємо метод y -  цього об’єкта.
            )  # Продовження багаторядкового виразу: вказуємо ще один аргумент або частину колекції.
            zoom_anim = (  # Обчислюємо й зберігаємо значення у змінній zoom_anim.
                    Animation(size=new_size, pos=new_pos, duration=.06)  # Обчислюємо й зберігаємо значення у змінній Animation(size.
                    + Animation(size=old_size, pos=old_pos, duration=.06)  # Обчислюємо й зберігаємо значення у змінній + Animation(size.
            )  # Продовження багаторядкового виразу: вказуємо ще один аргумент або частину колекції.
            self.anim_play = True  # Задаємо значення властивості об’єкта.
            zoom_anim.bind(on_complete=lambda *_: setattr(self, "anim_play", False))  # Обчислюємо й зберігаємо значення у змінній zoom_anim.bind(on_complete.
            zoom_anim.start(self)  # Викликаємо метод або функцію.
        else:  # Виконуємо цей блок, якщо попередні умови не підійшли.
            self.defeated()  # Виконуємо метод defeated цього об’єкта.
            level_rat = app.LEVELS[app.LEVEL]["rat"]  # Обчислюємо й зберігаємо значення у змінній level_rat.
            if self.rat_index + 1 < len(level_rat):  # Перевіряємо умову перед виконанням вкладених команд.
                self.rat_index += 1  # Задаємо значення властивості об’єкта.
                Clock.schedule_once(self.new_rat, .75)  # Викликаємо функцію бібліотеки для таймера, анімації, звуку або роботи з файлами.
            else:  # Виконуємо цей блок, якщо попередні умови не підійшли.
                Clock.schedule_once(self.GAME_SCREEN.check_level_complete, .75)  # Викликаємо функцію бібліотеки для таймера, анімації, звуку або роботи з файлами.

        return True  # Повертаємо результат виклику.


class Game(Screen):  # Оголошуємо клас — шаблон екрана або об’єкта.
    score = NumericProperty(0)  # Обчислюємо й зберігаємо значення у змінній score.
    elapsed_time = NumericProperty(0)  # Обчислюємо й зберігаємо значення у змінній elapsed_time.
    game_active = False  # Обчислюємо й зберігаємо значення у змінній game_active.
    timer_event = None  # Обчислюємо й зберігаємо значення у змінній timer_event.

    back_sound = SoundLoader.load("assets/audios/Black_Swan_part.mp3")  # Обчислюємо й зберігаємо значення у змінній back_sound.
    level_complete_sound = SoundLoader.load("assets/audios/level_complete.ogg")  # Обчислюємо й зберігаємо значення у змінній level_complete_sound.

    def on_pre_enter(self, *args):  # Готуємо екран безпосередньо перед його показом.
        app = App.get_running_app()  # Обчислюємо й зберігаємо значення у змінній app.
        if app.LEVEL >= len(app.LEVELS):  # Перевіряємо умову перед виконанням вкладених команд.
            app.LEVEL = 0  # Оновлюємо спільні дані головного застосунку.

        bg_path = f"assets/images/level{app.LEVEL + 1}.png"  # Обчислюємо й зберігаємо значення у змінній bg_path.
        if os.path.exists(bg_path):  # Перевіряємо умову перед виконанням вкладених команд.
            self.ids.level_bg.source = bg_path  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
        else:  # Виконуємо цей блок, якщо попередні умови не підійшли.
            self.ids.level_bg.source = "assets/images/back_game.png"  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.

        lvl_data = app.LEVELS[app.LEVEL]  # Обчислюємо й зберігаємо значення у змінній lvl_data.
        self.ids.stars_hint_label.text = f"3★ ≤ {lvl_data['t3']}s  |  2★ ≤ {lvl_data['t2']}s"  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.

        self.score = 0  # Задаємо рахунок гравця.
        self.elapsed_time = 0  # Задаємо лічильник секунд.
        self.game_active = False  # Задаємо стан активності гри.

        self.ids.level_complete.opacity = 0  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
        self.ids.stars_container.opacity = 0  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
        self.ids.stars_container.clear_widgets()  # очищаємо дочірні віджети

        self.ids.retry_button.opacity = 0  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
        self.ids.retry_button.disabled = True  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
        self.ids.next_button.opacity = 0  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
        self.ids.next_button.disabled = True  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.

        self.ids.level_title.text = f"Level {app.LEVEL + 1}"  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.

        rat = self.ids.rat  # Обчислюємо й зберігаємо значення у змінній rat.
        rat.rat_index = 0  # Обчислюємо й зберігаємо значення у змінній rat.rat_index.
        rat.opacity = 0  # Обчислюємо й зберігаємо значення у змінній rat.opacity.
        rat.interaction_block = True  # Обчислюємо й зберігаємо значення у змінній rat.interaction_block.

        return super().on_pre_enter(*args)  # Передаємо подію базовому класу Kivy для стандартної обробки.

    def on_enter(self, *args):  # Kivy викликає метод, коли екран з’являється.
        title = (  # Обчислюємо й зберігаємо значення у змінній title.
                Animation(opacity=1, duration=.45)  # Обчислюємо й зберігаємо значення у змінній Animation(opacity.
                + Animation(opacity=0, duration=.55)  # Обчислюємо й зберігаємо значення у змінній + Animation(opacity.
        )  # Продовження багаторядкового виразу: вказуємо ще один аргумент або частину колекції.
        title.bind(on_complete=self.start_game)  # Обчислюємо й зберігаємо значення у змінній title.bind(on_complete.
        title.start(self.ids.level_title)  # Викликаємо метод або функцію.

        app = App.get_running_app()  # Обчислюємо й зберігаємо значення у змінній app.
        if app.music_enabled and self.back_sound:  # Перевіряємо умову перед виконанням вкладених команд.
            self.back_sound.volume = app.volume  # Задаємо гучність.
            self.back_sound.play()  # починаємо відтворення звуку

        return super().on_enter(*args)  # Передаємо подію базовому класу Kivy для стандартної обробки.

    def start_game(self, *args):  # Запускаємо гру, таймер і першу рибу.
        if self.manager.current != "game":  # Перевіряємо умову перед виконанням вкладених команд.
            return  # Завершуємо роботу методу.
        self.game_active = True  # Задаємо стан активності гри.
        self.elapsed_time = 0  # Задаємо лічильник секунд.

        if self.timer_event:  # Перевіряємо умову перед виконанням вкладених команд.
            self.timer_event.cancel()  # скасовуємо заплановану подію
        self.timer_event = Clock.schedule_interval(self.update_timer, 1.0)  # Задаємо значення властивості об’єкта.

        self.ids.rat.new_rat()  # показуємо наступну рибу

    def update_timer(self, dt):  # Щосекунди оновлюємо час гри.
        if self.game_active:  # Перевіряємо умову перед виконанням вкладених команд.
            self.elapsed_time += 1  # Задаємо значення властивості об’єкта.

    def check_level_complete(self, *args):  # Завершуємо рівень, визначаємо зірки та зберігаємо результат.
        if not self.game_active:  # Перевіряємо умову перед виконанням вкладених команд.
            return  # Завершуємо роботу методу.

        self.game_active = False  # Задаємо стан активності гри.
        if self.timer_event:  # Перевіряємо умову перед виконанням вкладених команд.
            self.timer_event.cancel()  # скасовуємо заплановану подію

        app = App.get_running_app()  # Обчислюємо й зберігаємо значення у змінній app.

        lvl_data = app.LEVELS[app.LEVEL]  # Обчислюємо й зберігаємо значення у змінній lvl_data.
        if self.elapsed_time <= lvl_data["t3"]:  # Перевіряємо умову перед виконанням вкладених команд.
            stars_count = 3  # Обчислюємо й зберігаємо значення у змінній stars_count.
        elif self.elapsed_time <= lvl_data["t2"]:  # Перевіряємо цю умову, якщо попередня не виконалась.
            stars_count = 2  # Обчислюємо й зберігаємо значення у змінній stars_count.
        else:  # Виконуємо цей блок, якщо попередні умови не підійшли.
            stars_count = 1  # Обчислюємо й зберігаємо значення у змінній stars_count.

        while len(app.progress["stars"]) <= app.LEVEL:  # Повторюємо вкладений блок, поки умова істинна.
            app.progress["stars"].append(0)  # Виконуємо метод append цього об’єкта.
        if stars_count > app.progress["stars"][app.LEVEL]:  # Перевіряємо умову перед виконанням вкладених команд.
            app.progress["stars"][app.LEVEL] = stars_count  # Оновлюємо спільні дані головного застосунку.

        is_last = app.LEVEL == len(app.LEVELS) - 1  # Обчислюємо й зберігаємо значення у змінній is_last.

        if is_last:  # Перевіряємо умову перед виконанням вкладених команд.
            self.ids.level_complete.text = "LEVEL COMPLETE!"  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
            self.ids.next_button.text = "VICTORY"  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
        else:  # Виконуємо цей блок, якщо попередні умови не підійшли.
            self.ids.level_complete.text = "LEVEL COMPLETE!"  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
            self.ids.next_button.text = "NEXT LEVEL"  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
            if app.LEVEL + 1 > app.progress["current_level"]:  # Перевіряємо умову перед виконанням вкладених команд.
                app.progress["current_level"] = app.LEVEL + 1  # Оновлюємо спільні дані головного застосунку.

        container = self.ids.stars_container  # Обчислюємо й зберігаємо значення у змінній container.
        container.clear_widgets()  # очищаємо дочірні віджети
        for _ in range(stars_count):  # Повторюємо вкладені команди для кожного елемента послідовності.
            star_img = Image(source="assets/images/star.png", allow_stretch=True, keep_ratio=True)  # Обчислюємо й зберігаємо значення у змінній star_img.
            container.add_widget(star_img)  # додаємо віджет до контейнера

        self.ids.stars_container.opacity = 1  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
        app.save_progress()  # зберігаємо прогрес

        Animation(opacity=1, duration=.3).start(self.ids.level_complete)  # Обчислюємо й зберігаємо значення у змінній Animation(opacity.

        self.ids.retry_button.disabled = False  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
        Animation(opacity=1, duration=.3).start(self.ids.retry_button)  # Обчислюємо й зберігаємо значення у змінній Animation(opacity.

        self.ids.next_button.disabled = False  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
        Animation(opacity=1, duration=.3).start(self.ids.next_button)  # Обчислюємо й зберігаємо значення у змінній Animation(opacity.

        if self.back_sound:  # Перевіряємо умову перед виконанням вкладених команд.
            self.back_sound.volume = app.volume * .4  # Задаємо гучність.

        if app.sound_enabled and self.level_complete_sound:  # Перевіряємо умову перед виконанням вкладених команд.
            self.level_complete_sound.play()  # починаємо відтворення звуку

    def retry_level(self):  # Перезапускаємо поточний рівень.
        self.prepare_current_level()  # Виконуємо метод prepare_current_level цього об’єкта.
        Clock.schedule_once(self.start_game, .25)  # Викликаємо функцію бібліотеки для таймера, анімації, звуку або роботи з файлами.

    def next_level(self):  # Переходимо далі або відкриваємо екран перемоги.
        app = App.get_running_app()  # Обчислюємо й зберігаємо значення у змінній app.
        if app.LEVEL == len(app.LEVELS) - 1:  # Перевіряємо умову перед виконанням вкладених команд.
            if self.back_sound:  # Перевіряємо умову перед виконанням вкладених команд.
                self.back_sound.stop()  # зупиняємо відтворення
            self.manager.transition.direction = "left"  # Задаємо значення властивості об’єкта.
            self.manager.current = "victory"  # Задаємо значення властивості об’єкта.
        else:  # Виконуємо цей блок, якщо попередні умови не підійшли.
            app.LEVEL += 1  # Оновлюємо спільні дані головного застосунку.
            app.save_progress()  # зберігаємо прогрес
            self.prepare_current_level()  # Виконуємо метод prepare_current_level цього об’єкта.
            Clock.schedule_once(self.start_game, .25)  # Викликаємо функцію бібліотеки для таймера, анімації, звуку або роботи з файлами.

    def prepare_current_level(self):  # Скидаємо старі значення та готуємо рівень до запуску.
        app = App.get_running_app()  # Обчислюємо й зберігаємо значення у змінній app.
        self.game_active = False  # Задаємо стан активності гри.
        self.elapsed_time = 0  # Задаємо лічильник секунд.
        if self.timer_event:  # Перевіряємо умову перед виконанням вкладених команд.
            self.timer_event.cancel()  # скасовуємо заплановану подію

        bg_path = f"assets/images/level{app.LEVEL + 1}.png"  # Обчислюємо й зберігаємо значення у змінній bg_path.
        if os.path.exists(bg_path):  # Перевіряємо умову перед виконанням вкладених команд.
            self.ids.level_bg.source = bg_path  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
        else:  # Виконуємо цей блок, якщо попередні умови не підійшли.
            self.ids.level_bg.source = "assets/images/back_game.png"  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.

        lvl_data = app.LEVELS[app.LEVEL]  # Обчислюємо й зберігаємо значення у змінній lvl_data.
        self.ids.stars_hint_label.text = f"3★ ≤ {lvl_data['t3']}s  |  2★ ≤ {lvl_data['t2']}s"  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.

        self.score = 0  # Задаємо рахунок гравця.

        rat = self.ids.rat  # Обчислюємо й зберігаємо значення у змінній rat.
        rat.stop_all_animations()  # зупиняємо анімації віджета
        rat.rat_index = 0  # Обчислюємо й зберігаємо значення у змінній rat.rat_index.
        rat.opacity = 0  # Обчислюємо й зберігаємо значення у змінній rat.opacity.
        rat.interaction_block = True  # Обчислюємо й зберігаємо значення у змінній rat.interaction_block.
        rat.angle = 0  # Обчислюємо й зберігаємо значення у змінній rat.angle.
        rat.size = (dp(200), dp(200))  # Обчислюємо й зберігаємо значення у змінній rat.size.

        self.ids.level_complete.opacity = 0  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
        self.ids.stars_container.opacity = 0  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
        self.ids.stars_container.clear_widgets()  # очищаємо дочірні віджети

        self.ids.retry_button.opacity = 0  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
        self.ids.retry_button.disabled = True  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
        self.ids.next_button.opacity = 0  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.
        self.ids.next_button.disabled = True  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.

        self.ids.level_title.text = f"Level {app.LEVEL + 1}"  # Змінюємо властивість віджета, знайденого за KV-ідентифікатором.

        if self.back_sound:  # Перевіряємо умову перед виконанням вкладених команд.
            self.back_sound.volume = app.volume  # Задаємо гучність.

    def go_level_select(self):  # Переходимо на екран вибору рівнів.
        self.game_active = False  # Задаємо стан активності гри.
        if self.timer_event:  # Перевіряємо умову перед виконанням вкладених команд.
            self.timer_event.cancel()  # скасовуємо заплановану подію
        if self.back_sound:  # Перевіряємо умову перед виконанням вкладених команд.
            self.back_sound.stop()  # зупиняємо відтворення

        self.manager.transition.direction = "right"  # Задаємо значення властивості об’єкта.
        self.manager.current = "level_select"  # Задаємо значення властивості об’єкта.

    def go_settings(self):  # Відкриваємо налаштування.
        self.game_active = False  # Задаємо стан активності гри.
        if self.timer_event:  # Перевіряємо умову перед виконанням вкладених команд.
            self.timer_event.cancel()  # скасовуємо заплановану подію
        if self.back_sound:  # Перевіряємо умову перед виконанням вкладених команд.
            self.back_sound.stop()  # зупиняємо відтворення

        settings = self.manager.get_screen("settings")  # Обчислюємо й зберігаємо значення у змінній settings.
        settings.return_screen = "game"  # Обчислюємо й зберігаємо значення у змінній settings.return_screen.
        self.manager.transition.direction = "left"  # Задаємо значення властивості об’єкта.
        self.manager.current = "settings"  # Задаємо значення властивості об’єкта.


class ClickerApp(App):  # Оголошуємо клас — шаблон екрана або об’єкта.
    LEVEL = 0  # Обчислюємо й зберігаємо значення у змінній LEVEL.
    volume = NumericProperty(.7)  # Обчислюємо й зберігаємо значення у змінній volume.
    music_enabled = BooleanProperty(True)  # Обчислюємо й зберігаємо значення у змінній music_enabled.
    sound_enabled = BooleanProperty(True)  # Обчислюємо й зберігаємо значення у змінній sound_enabled.

    RAT = {  # Обчислюємо й зберігаємо значення у змінній RAT.
        "rat1": {"source": "assets/images/rat1.png", "hp": 10},  # Продовжуємо формувати значення для поточної команди.
        "rat2": {"source": "assets/images/rat2.png", "hp": 15},  # Продовжуємо формувати значення для поточної команди.
        "rat3": {"source": "assets/images/rat3.png", "hp": 20},  # Продовжуємо формувати значення для поточної команди.
        "rat4": {"source": "assets/images/rat4.png", "hp": 25},  # Продовжуємо формувати значення для поточної команди.
        "rat5": {"source": "assets/images/rat5.png", "hp": 40},  # Продовжуємо формувати значення для поточної команди.
        "rat6": {"source": "assets/images/rat6.png", "hp": 60}  # Продовжуємо формувати значення для поточної команди.
    }  # Продовження багаторядкового виразу: вказуємо ще один аргумент або частину колекції.

    LEVELS = [  # Обчислюємо й зберігаємо значення у змінній LEVELS.
        {"rat": ["rat1", "rat2"], "t3": 6, "t2": 8},  # Продовження багаторядкового виразу: вказуємо ще один аргумент або частину колекції.
        {"rat": ["rat3", "rat4"], "t3": 15, "t2": 20},  # Продовження багаторядкового виразу: вказуємо ще один аргумент або частину колекції.
        {"rat": ["rat5", "rat6"], "t3": 27, "t2": 30}  # Продовження багаторядкового виразу: вказуємо ще один аргумент або частину колекції.
    ]  # Продовження багаторядкового виразу: вказуємо ще один аргумент або частину колекції.

    def on_start(self):  # Під час запуску відновлюємо збережені налаштування.
        self.progress = self.load_progress()  # Задаємо значення властивості об’єкта.
        self.volume = self.progress["volume"]  # Задаємо гучність.

    def load_progress(self):  # Читаємо файл прогресу або повертаємо початкові дані.
        defaults = {"current_level": 0, "volume": .7, "stars": []}  # Обчислюємо й зберігаємо значення у змінній defaults.
        path = os.path.join(self.user_data_dir, "progress.json")  # Обчислюємо й зберігаємо значення у змінній path.
        try:  # Починаємо блок, де оброблятимемо можливу помилку.
            with open(path, "r", encoding="utf-8") as file:  # Відкриваємо файл; with автоматично закриє його після роботи.
                saved = json.load(file)  # Обчислюємо й зберігаємо значення у змінній saved.
                if isinstance(saved, dict):  # Перевіряємо умову перед виконанням вкладених команд.
                    defaults.update(saved)  # Викликаємо метод або функцію.
        except Exception:  # Обробляємо помилку, щоб програма могла продовжити роботу.
            pass  # Поки не виконуємо дій у цьому блоці.
        return defaults  # Повертаємо результат виклику.

    def save_progress(self):  # Записуємо прогрес у файл на пристрої.
        os.makedirs(self.user_data_dir, exist_ok=True)  # Обчислюємо й зберігаємо значення у змінній os.makedirs(self.user_data_dir, exist_ok.
        path = os.path.join(self.user_data_dir, "progress.json")  # Обчислюємо й зберігаємо значення у змінній path.
        with open(path, "w", encoding="utf-8") as file:  # Відкриваємо файл; with автоматично закриє його після роботи.
            json.dump(self.progress, file, ensure_ascii=False, indent=4)  # Обчислюємо й зберігаємо значення у змінній json.dump(self.progress, file, ensure_ascii.

    def set_volume(self, value):  # Обмежуємо гучність діапазоном 0–1 і зберігаємо її.
        self.volume = max(0, min(float(value), 1))  # Задаємо гучність.
        if hasattr(self, "progress"):  # Перевіряємо умову перед виконанням вкладених команд.
            self.progress["volume"] = self.volume  # Задаємо значення властивості об’єкта.
            self.save_progress()  # зберігаємо прогрес

    def build(self):  # Створюємо менеджер і додаємо до нього всі екрани.
        sm = ScreenManager()  # Обчислюємо й зберігаємо значення у змінній sm.
        sm.add_widget(Menu(name="menu"))  # Обчислюємо й зберігаємо значення у змінній sm.add_widget(Menu(name.
        sm.add_widget(LevelSelect(name="level_select"))  # Обчислюємо й зберігаємо значення у змінній sm.add_widget(LevelSelect(name.
        sm.add_widget(Game(name="game"))  # Обчислюємо й зберігаємо значення у змінній sm.add_widget(Game(name.
        sm.add_widget(Settings(name="settings"))  # Обчислюємо й зберігаємо значення у змінній sm.add_widget(Settings(name.
        sm.add_widget(VictoryScreen(name="victory"))  # Обчислюємо й зберігаємо значення у змінній sm.add_widget(VictoryScreen(name.
        return sm  # Повертаємо результат виклику.


if platform != "android":  # Перевіряємо умову перед виконанням вкладених команд.
    Window.size = (400, 600)  # Обчислюємо й зберігаємо значення у змінній Window.size.

app = ClickerApp()  # Обчислюємо й зберігаємо значення у змінній app.
app.run()  # Виконуємо метод run цього об’єкта.
