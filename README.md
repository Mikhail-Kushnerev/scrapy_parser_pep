# Ассинхронный парсер manual по Python

## Описание

Парсер, собирающий информацию с сайта https://www.python.org/
- версии языка и авторов версий;
- статусы всех стандартов PEP.

Вся собранная информация сохраняется в файлы с расширением **csv**:
- Информация о стандарте: номер, статус, автор-(ы);
- Колличество каждого статуса на сайте + общая сумма.

## Оглавление
- [технологии](#технологии)
- <a href="#t1"> структура парсера </a>
- [описание работы](#описание-работы)
- [запуск](#запуск-парсера)
- [автор](#автор)

## Технологии
- Python;
- Scrapy.

<details open>
  <summary>
    <h2 id="t1"> Структура парсера </h2>
  </summary>

```cmd
scrapy_parser_pep
|   .flake8
|   .gitignore
|   constants.py  <-- Константные данные
|   pytest.ini
|   README.md
|   requirements.txt
|   scrapy.cfg
|
+---pep_parse
|   |   items.py  <-- Создание объекта Items из спарсенных данных
|   |   middlewares.py
|   |   pipelines.py  <-- Обработка Items (запись данных в CSV-файлы)
|   |   settings.py  <-- Настройки парсера
|   |   __init__.py
|   |   
|   +---spiders
|   |   |   pep.py  <-- Метод обработки данных
|   |   |   __init__.py
|   |   |
|   |   \---__pycache__
|   |           
|   \---__pycache__
|           
+---results  <-- Директория с результами парсера
|       pep_2022-08-10T19-36-00.csv  <-- Все полученные данные (номер, статус, автор(ы))
|       status_summary_2022-08-10_22-36-18.csv  <-- Подсчёт кол-ва
|       
+---tests
|
+---venv
```

</details>

[⬆️Оглавление](#оглавление)

# Описание работы

Парсер собирает информацию с сайта и сводит все данные в 2 таблицы:
1. Список PEP;
2. Сводка по статусам.
Таблицы находятся в директории **results** (см. <a href="#t1">дерево проекта</a>)  


<table align="center">
  <thead>
    <tr>
      <th colspan="2">
        Результат работы
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        Таблица №1
      </td>
      <td>
        Таблица №2
      </td>
    </tr>
    <tr>
      <td>
        <img
          align="top"
          alt="table_№1"
          width="40%"
          src="https://github.com/Mikhail-Kushnerev/image/blob/main/Parse_Scrapy/table_1.png"
        >
      </td>
      <td>
        <img
          align="top"
          alt="table_№2"
          src="https://github.com/Mikhail-Kushnerev/image/blob/main/Parse_Scrapy/table_2.png"
        >
      </td>
    </tr>
  </tbody>
</table>

[⬆️Оглавление](#оглавление)

## Запуск парсера
- Установите вирт. окружение:
    ```python
    python -m venv venv
    ```
- Активируйте вирт. окружение и установите зависимости:
    ```python
    (win) source venv/Scripts/activate
    (linux) source venv/bin/activate
    python -r requirements.txt
    ```
- В терминале введите команду:
    ```python
    scrapy crawl pep
    ```
    [⬆️Оглавление](#оглавление)


## Автор

[Mikhail Kushnerev](https://github.com/Mikhail-Kushnerev)  
[в начало](#парсер-manual-по-python)