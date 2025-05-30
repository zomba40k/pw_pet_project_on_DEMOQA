# Playwright Pet Project for DEMOQA

Мой пет проект с тестами для сайта-тренажера DEMOQA

Тесты написаны с использованием python 3.13

## Установка и запуск

1. **Перейди в папку проекта**:

В cmd:  `cd путь к\pw_pet_project_on_DEMOQA`

Должно быть что-то вроде : `cd C:\Users\UserName\pw_pet_project_on_DEMOQA`.


4. **Создай и активируй виртуальное окружение**:

  `python -m venv venv`

`venv\Scripts\activate`

>Слева в строке должно быть (venv)

4. **Установи зависимости**:
`pip install -r requirements.txt`
Если Playwright не установлен автоматически, установите его отдельно:
`pip install playwright`


5. **Установите браузеры для Playwright**:
`playwright install`
Это загрузит браузеры (Chrome, Firefox и др.), которые нужны для тестов.


6. **Запустите тесты**:
- Для запуска smoke-тестов:
`pytest -m smoke`

- Для запуска всех тестов:
`pytest`
