# Playwright Pet Project for DEMOQA

Этот проект содержит автоматизированные тесты для сайта [DEMOQA](https://demoqa.com/) с использованием Playwright и Pytest.

## Требования
- Рекомендуется Python 3.13.3
  Скачайте Python с [официального сайта](https://www.python.org/downloads/). Во время установки поставьте галочку "Add Python to PATH".

## Установка и запуск

1. **Склонируйте репозиторий** (если еще не сделали):
git clone https://github.com/zomba40k/pw_pet_project_on_DEMOQA.git


3. **Перейдите в папку проекта**:
Откройте cmd и выполните:
cd путь к\pw_pet_project_on_DEMOQA
Например: `cd C:\Users\UserName\pw_pet_project_on_DEMOQA`.


3. **Создайте виртуальное окружение**:
python -m venv venv


4. **Активируйте виртуальное окружение**:
venv\Scripts\activate
После этого в командной строке слева появится `(venv)` — это значит, что окружение активно.


5. **Установите зависимости**:
pip install -r requirements.txt
Если Playwright не установлен автоматически, установите его отдельно:
pip install playwright


6. **Установите браузеры для Playwright**:
playwright install
Это загрузит браузеры (Chrome, Firefox и др.), которые нужны для тестов.


7. **Запустите тесты**:
- Для запуска smoke-тестов:
pytest -m smoke

- Для запуска всех тестов:
pytest
