<h1 align="center">Telehack</h1>
<h3 align="center">Автоматическая проверка доступности заданных интернет-ресурсов с возможностью сохранения результатов и вызова дополнительных функций.<h3>

<h4 align="justify">Данная праграмма была написана во время участия в “Хакатон связи” (http://telehack.ru/about) осенью 2022 года и заняла первое место среди работ 1-2 курсов.<h3>

#### Участники команды:  
- https://github.com/AleksandrSedelnikov
- https://github.com/cooleid
- https://github.com/Gerdelezhov

## Цель работы:  
Разработать ПО для автоматизация и упрощение процесса проверки интернет-ресурсов на сети операторов связи.

## Постановка задачи:  
Разработать ПО с минимальным интерфейсом для проверки доступности интернет-ресурсов и реализовать в нем следующие возможности (средства для разработки на усмотрение исполнителя):
- загрузка списка необходимых для проверки доступности интернет-ресурсов из текстового файла
- осуществление проверки интернет-ресурсов на доступность согласно загруженному списку (количество попыток должно быть равным пяти)
- создание скриншотов после проверки, скриншот обязателен в обоих случаях, если есть доступ или нет доступа к интернет-ресурсу, просмотр скриншота по запросу пользователя
- создание таблицы трассировки к интернет-ресурсам после проверки, активации функции по запросу пользователя
- автоматический запуск из программы необходимого интернет-ресурса в браузере после проверки, активация функции по запросу пользователя
- автоматическая проверка социально-значимых интернет-ресурсов vk.com и gosuslugi.ru.
- сохранение результатов проверки


### Технологии используемые в проекте:  
Интерпретатор Python и его библиотеки (tkinter, selenium, subprocess) – для выполнения кода и конвертации его в системные инструкции.

### Настройка проекта:  
Для работы проекта необходим браузер "Mozilla Firefox".

## Пример работы:
<div align="center">
<img align="center" src = 'https://github.com/Gerdelezhov/telehack/blob/master/Docs/pictures%20for%20readme/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA1.png'><br>
1. Программа сразу после запуска

<img align="center" src = 'https://github.com/Gerdelezhov/telehack/blob/master/Docs/pictures%20for%20readme/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA2.png'><br>
2. Выбор Файла

<img align="center" src = 'https://github.com/Gerdelezhov/telehack/blob/master/Docs/pictures%20for%20readme/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA3.png'><br>
3. Программа после загрузки файла.

<img align="center" src = 'https://github.com/Gerdelezhov/telehack/blob/master/Docs/pictures%20for%20readme/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA4.png'><br>
4. Программа после запуска проверки.

<img align="center" src = 'https://github.com/Gerdelezhov/telehack/blob/master/Docs/pictures%20for%20readme/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA5.png'><br>
5. Программа после окончания проверки.

<img align="center" src = 'https://github.com/Gerdelezhov/telehack/blob/master/Docs/pictures%20for%20readme/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA6.png'><br>
6. Результат трассировки сайта e1.ru (нажатие на кнопку 1), выводится в новом окне.

<img align="center" src = 'https://github.com/Gerdelezhov/telehack/blob/master/Docs/pictures%20for%20readme/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA7.png'><br>
7. Изображение ya.ru (нажатие на кнопку 2).

<img align="center" src = 'https://github.com/Gerdelezhov/telehack/blob/master/Docs/pictures%20for%20readme/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA8.png'><br>
8. Запущенный браузер www.gosuslugi.ru (нажатие на кнопку 3).

<img align="center" src = 'https://github.com/Gerdelezhov/telehack/blob/master/Docs/pictures%20for%20readme/%D0%A0%D0%B8%D1%81%D1%83%D0%BD%D0%BE%D0%BA9.png'><br>
9. Содержимое файла results.txt (нажатие на кнопку ‘Сохранить результат’).

</div>
