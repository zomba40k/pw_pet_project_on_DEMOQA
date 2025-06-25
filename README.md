# Playwright Pet Project for DEMOQA

Мой пет проект с тестами для сайта-тренажера DEMOQA

Тесты написаны с использованием python 3.13

## Установка и запуск

1. **Перейди в папку проекта**:

- В cmd:  `cd путь к\pw_pet_project_on_DEMOQA`

Должно быть что-то вроде : `cd C:\Users\UserName\pw_pet_project_on_DEMOQA`.

2. **Создай и активируй виртуальное окружение**:

`python -m venv venv`

`venv\Scripts\activate`

> Слева в строке должно быть (venv)

3. **Установи зависимости**:
   `pip install -r requirements.txt`

- Если Playwright не установлен автоматически, установите его отдельно:
  `pip install playwright`


4. **Установите браузеры для Playwright**:
   `playwright install`
   Это загрузит браузеры (Chrome, Firefox и др.), которые нужны для тестов.


7. **Запустите тесты**:

- Для запуска smoke-тестов:
  `pytest -m smoke`

- Для запуска всех тестов:
  `pytest`
  
- Для запуска всех тестов с отчетами Allure:
- 
   `pytest --alluredir=allure-results` - Для запуска тестов
  
 -  `allure serve allure-results` - Для просмотра отчета


## Чек-лист с проверками

Для просмотра чек-листа с проверками перейдите
по [ссылке](https://docs.google.com/spreadsheets/d/1qLVzIyZvB2_evSFlhEFmePSKPTvBv_a805ZzSr8LY64/edit?usp=sharing).
