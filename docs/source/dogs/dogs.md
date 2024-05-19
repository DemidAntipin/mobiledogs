# Модуль работы с собаками

Модуль включает функции для работы с собаками и ошейниками.

## Функция create_dog

Функция добавляет в базу данных новую собаку.

**Parametrs:**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `name`(string): кличка собаки
* `description` (string): описание и приметы собаки
* `collar_id`(integer): id ошейника, должен существовать в базе и не быть привязанным к другой собаке

**Returns:**

```json
{
    "success": true,
    "exception": null,
    *dog_id*: <dog_id>
}
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции
* `collar_not_found`: ошейника с указанным id не существует

## Функция read_dog

Функция выводит информацию о конкретной собаке

**Parameters**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `dog_id` (integer): id собаки

**Returns**

```json
{
    "name": <dog_name>,
    "description": <dog_description>,
    "collar_id": <collar_id>,
    "datas": 
        [
            {
                "longitute": <longitude>,
                "latitude": <latitude>,
                "datetime": <datetime>
            },
            {
                "longitute": <longitude>,
                "latitude": <latitude>,
                "datetime": <datetime>
            }
            ...
        ]
}
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции
* `dog_not_found`: собака с указанным id не зарегистрирована в базе

## Функция read_dogs

Функция выводит информацию о `limit` собаках, пропуская `skip` первых.

**Parameters**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `skip` (integer) optional: кол-во пропущенных строк в таблице
* `limit` (integer) optional: кол-во собак

**Returns**

```json
{
    [
        {
            "name": <dog_name>,
    	    "description": <dog_description>,
    	    "collar_id": <collar_id>,
    	    "datas":
        	[
            	    {
                	"longitute": <longitude>,
                	"latitude": <latitude>,
                	"datetime": <datetime>
                },
                {
                	"longitute": <longitude>,
                	"latitude": <latitude>,
                	"datetime": <datetime>
                }
                ...
                ]
         },
        {
            "name": <dog_name>,
            "description": <dog_description>,
            "collar_id": <collar_id>,
            "datas":
                [
                    {
                        "longitute": <longitude>,
                        "latitude": <latitude>,
                        "datetime": <datetime>
                    },
                    {
                        "longitute": <longitude>,
                        "latitude": <latitude>,
                        "datetime": <datetime>
                    }
                    ...
                ]
         }
         ...
    ]
}
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции

## Функция create_collar

Функция добавляет в базу данных новый ошейник.

**Parameters:**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `ip` (string): ip ошейника

**Returns**

```json
    {
        "success": true,
        "exception": null,
        "id": <collar_id>
    }
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции
* `ip_collision`: указаный ip уже присвоен другому ошейнику в базе

### Функция read_collar_by_id

Функция выдает информацию об ощейнике по его id

**Parameters:**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `id` (integer): id ошейника

**Returns**

```json
    {
        "id": <collar_id>,
        "ip": <collar_ip>
    }
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции
* `collar_not_found`: ошейника с указанным id нет в базе данных

### Функция read_collar_by_ip

Функция выдает информацию об ошейнике по его ip

**Parameters:**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `ip` (string): ip ошейника

**Returns**

```json
    {
        "id": <collar_id>,
        "ip": <collar_ip>
    }
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции
* `collar_not_found`: ошейника с указанным ip нет в базе данных

### Функция read_collars

Функция выдает информацию о `limit` ошейниках в базе данных, пропуская `skip` первых

**Parameters:**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `skip` (integer) optional: кол-во пропущенных строк в таблице
* `limit` (integer) optional: кол-во ошейников

**Returns**

```json
    {
        [
            {
                "id": <collar_id>,
                "ip": <collar_ip>
            },
            {
                "id": <collar_id>,
                "ip": <collar_ip>
            }
            ...
        ]
    }
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции

### Функция create_data_for_dog

Функция обрабатывает запросы от ошейника и записывает в базу данных информацию о собаке

**Parameters:**

* `ip` (string): ip ошейника
* `dog_id` (integer): id собаки
* `latutude` (float): примерная координата широты
* `longitude` (float): примерная координата долготы
* `datetime` (datetime): время получения запроса

**Returns**

```json
    {
        "id": <id>,
	"dog_id": <dog_id>,
        "longitute": <longitude>,
        "latitude": <latitude>,
        "datetime": <datetime>
    }
```

**Raises**

* `invalid_ip`: указан невалидный ip

### Функция get_data_for_dog

Функция выводит данные о месторасположении конкретной собаки

**Parameters:**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `dog_id` (integer): id собаки

**Returns:**

```json
    [
        {
                "id": <id>,
                "dog_id": <dog_id>,
                "longitute": <longitude>,
                "latitude": <latitude>,
                "datetime": <datetime>
        },
        {
                "id": <id>,
                "dog_id": <dog_id>,
                "longitute": <longitude>,
                "latitude": <latitude>,
                "datetime": <datetime>
        }
        ...
    ]
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции
* `dog_not_found`: собака с указанным id не зарегистрирована в базе

### Функция read_dogsdata

Функция выводит данные о `limit` месторасположениях собак, пропуская `skip` строчек

**Parameters**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `skip` (integer) optional: кол-во пропущенных строк в таблице
* `limit` (integer) optional: кол-во месторасположений

**Returns:**

```json
    [
        {
                "id": <id>,
                "dog_id": <dog_id>,
                "longitute": <longitude>,
                "latitude": <latitude>,
                "datetime": <datetime>
        },
        {
                "id": <id>,
                "dog_id": <dog_id>,
                "longitute": <longitude>,
                "latitude": <latitude>,
                "datetime": <datetime>
        }
        ...
    ]
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции
