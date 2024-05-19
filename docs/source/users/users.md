# Модуль работы с пользователями

Модуль включает функции для работы с пользователями.

## Функция create_user

Функция регистрирует нового пользователя и добавляет его в базу данных. При успешной регистрации сразу же запускается функция login_user

**Parametrs:**

* `name`(string): имя пользователя, должен быть уникальный в базе данных
* `email`(EmailString): почта пользователя, должна быть уникальной в базе данных
* `phone` (string): телефон пользователя, должен быть уникальный в базе данных
* `password`(string): пароль пользователя

**Returns:**

```json
{
    "name": <username>, 
    "token": <usertoken>
}
```

**Raises**

* `email_collision`: попытка создать дубликат уникального значения в поле `email`
* `phone_collision`: попытка создать дубликат уникального значения в поле `phone`
* `name_collision`: попытка создать дубликат уникального значения в поле `name`


## Функция login_user

Функция авторизует пользователя и выдает ему token, нужный для использования других функций.

**Parametrs:**

* `name`(string): имя пользователя
* `password`(string): пароль пользователя

**Return**

```json
{
    "name": <username>, 
    "token": <usertoken>
}
```

**Raises**

* `invalid_login`: пользователя с таким именем не существует, или веден неверный пароль

## Функция read_user

Функция выводит информацию о выбранном пользователе.

**Parameters:**

* `token` (string): токен авторизации. Выдается функцией `login_user`
* `user_id` (integer): id пользователя, о котором мы хотим вывести информацию.

**Returns**

```json
    "id": <user_id>,
    "name": <username>,
    "email": <user_email>,
    "phone": <user_phone>,
    "token": "##########"
}
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции
* `user_not_found`: пользователя с указанным id не существует

## Функция read_users

Функция выподит информацию о всех пользователях в базе данных.

**Parameters:**

* `token`(string): токен авторизации. Выдается функцией `login_user`

**Returns**

```json
{
    [
        {
	    "id": <user_id>,
            "name": <username>,
            "email": <user_email>,
            "phone": <user_phone>,
            "token": "##########"
	},
        {
            "id": <user_id>,
            "name": <username>,
            "email": <user_email>,
            "phone": <user_phone>,
            "token": "##########"
        }
	...
    ]
}
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции

