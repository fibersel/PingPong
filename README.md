# Pong online
Проект для курса PythonDevelopment2019

# Описание
В далеком 1972 году вышла аркадная игра Pong, разработанная и выпущенная Atari. Мы решили взять за основу эту легендарную игру и реализовать ее онлайн версию. 

## Реализация
Непосредственно логику игры делаем на клиенте в браузере (js+canvas), в качестве бэкенда выступает приложение на питоне (asyncio, aiohttp), общение между клиентами и бэкендом идет через websocket. Бэкенд отвечает за подбор соперников и синхронизацию событий в сессии. Приложение деплоится в докере.

## Как это выглядит
### Главное меню  
![Main menu](https://i.imgur.com/loz38mJ.png)
### Геймплей
![In-game screen](https://www.funstockretro.co.uk/news/wp-content/uploads/2017/07/Pong-653x400.png)

## Если успеем...
Есть идея сделать таблицу лидеров и подбор соперников по рейтингу. Для этого нужно будет реализовать механизм авторизации и сбора статистики игровых сессий.
