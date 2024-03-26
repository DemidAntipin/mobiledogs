База данных:
Таблица "osheinic" обновляется время от времени (запросы от ошейника)
id
charge(int %)
location(coords)
last_modify(datetime)
danger_or_lost(bool true если локация не меняется (с любой точностью координат) а время модификации меняется несколько раз)

Таблица "dog" обновляется после запросов от приложения
id
name(varchar(255))
osheinic_id(int foreign key)
last_cared(datetime)

Таблица "user" Обновляется после запросов от приложения
id
email
password_hash
service(bool default false)
is_active(bool)
location(coords) пока пользователь активен получает периодические запросы на обновления от приложения

Табле "connections" обновляется после запросов от приложения
id
user_id(int foreign key)
dog_id(int foreign key)

Функции приложения
user_registration(email, password) - добавить новую запись в таблицу "user"
user_login(email, password) - сделать пользователя активным начать периодические запросы на обновление локации
<функции ниже требуют авторизации авторизация проверяется библиотекой "login manager">
dog_list(user_id default your) - посмотреть список собак пользователя (dog_id из таблицы connections, расстояние как разница координат, last_cared из таблицы собак)
dog_list_all() - посмотреть список всех собак (dog.id, расстояние как разница координат, last_cared из таблицы собак)
care_about(dog_id) - пользователь добавляет собаку в свой список
stop_care(dog_id) - пользователь удаляет собаку из своего списка
choose_dog(dog_id) - получить координаты собаки, кличку, запрос подтверждения, когда подтвержден обновить last_cared datetime
give_task(user_id, dog_id, message) - открыть меню подтверждения, уведомить пользователя, показать сообщение, пользователь может принять задание коммандой choose_dog(dog_id) или проигорировать чтоб отказаться, (пользователь должен быть активным, а собака быть в его списке) 
confirm_task(user_id, upload file) - отправить файл пользователю, он может принять его и завершить задание или запросить переподтверждение 
track(dog_id) - показывать расстояние до собаки и направление (обновляется время от времени)
stop_track() - остановить трэкинг
user_logout() - пользователь становится не активным выход с помощью указанной библиотеки
alert(тригерится когда поле danger_or_lost true) - уведомить всех активных пользователь о подозрительном ошейнике и дать его координаты

Функции обслуживания
give_priviledges(user_id, secret key) - установить user.service true
remove_priviledges(user_id, another secret key) - установить user.service false
<Функции требуют авторизации и user.service true>
osheinic_registration() - добавить запись в таблицу "osheinic"
new_dog() - добавить запись в таблицу "dog"
watch_troubles() - список ошейников с датой последнего обновления более 2 часов назад
service(osheinic id) - получить последнии координаты ошейника
