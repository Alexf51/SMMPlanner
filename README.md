# SMMPlanner

Для работы данного приложения необходимо наличие следующих важных компонентов:
1.	Язык программирования Python
2.	Группа и приложение в социальной сети ВКонтакте
3.	Среда разработки PyCharm или похожая другая
4.	Токен полученный с помощью ссылки с запросом прав доступа
Также в данном руководстве подразумевается, что настройка будет проводиться в среде Windows.
Группа создается пользователем в самой социальной сети ВКонтакте. Приложение создается на сайте ВКонтакте для разработчиков.
Токен создается по документации VK API. Нужно в адресной строке задать ссылку. Пример состава ссылки: https://oauth.vk.com/authorize?client_id=12345&redirect_uri=https://oauth.vk.com/blank.html&scope=wall&response_type=token.
В ссылке после «client_id=» указываем ID своего приложения. После «scope=» пишем права, которые хотим выдать (например: wall – стена группы и др.). Далее получаем другую ссылку, в которой находится наш токен, после слов «access_token». Данная ссылка нам пригодиться в самой программе для обращения к методам, такие как отправка постов, анализ и др.
Далее в программе мы задаем переменную token в которую и записываем полученный токен. Также в переменную «owner_id» или «group_id» записываем ID группы.
В созданный текстовый документ jokes.txt можно записывать любую заготовленную информацию. Например, заготовленные шутки про программистов. Они преобразуются в текст, который будет выведен на картинки с разноцветным фоном.
Также, указав ID группы, можно посмотреть статистику группы на графике и в текстовом виде.
После запуска программы открывается интерфейс с возможностью:
1.	Написать текст поста
2.	Сгенерировать картинку с заготовленной информацией
3.	Запланировать время публикации либо опубликовать мгновенно
4.	Анализировать группы, просматривая статистику с выводом на графике количества лайков, комментариев, репостов
5.	Предпросмотр постов, с выводом информации о заготовленных постах или уже выложенных ранее


Перечень программных модулей
1.	main.py (главный модуль)
2.	posting.py (функции отправки поста)
3.	image.py (функция создания картинки)
4.	joke.py (функция создания шутки)
5.	joke.png (предварительный пост картинки с шуткой)
6.	jokes.txt (текст с заготовленными шутками)
