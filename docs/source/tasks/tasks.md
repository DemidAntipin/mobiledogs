# Модуль работы с задачами

Модуль включает функции для работы с задачами.

## Функция create_task

Функция создает новую задачу и добавляет её в базу данных.

**Parameters:**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `dog_id` (integer): id собаки
* `type` (string): описание самой задачи

**Returns:**

```json
    {
        "success": true,
        "exception": null,
        "task_id": task_id
    }
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции
* `dog_not_found`: собака с указанным id отсутствует в базе данных

## Функция read_task

Функция выдает информацию об определенной задаче

**Parameters:**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `task_id` (integer): id задачи

**Returns:**

```json
    {
        "id": task_id,
        "dog_id": dog_id,
        "type": task_type,
        "status": task_status,
        "responses": []
    }
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции
* `task_not_found`: задача с указанным id отсутствует в базе данных

## Функция read_tasks

Функция выдает информацию о `limit` задачах в базе данных, пропуская `skip` первых.

**Parameters:**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `skip` (integer): число задач к пропуску
* `limit` (integer): максимальное число задач в выборке

**Returns:**

```json
    [
            {
                "id": task_id,
                "dog_id": dog_id,
                "type": task_type,
                "status": task_status,
                "responses": []
            },
            {
                "id": task_id,
                "dog_id": dog_id,
                "type": task_type,
                "status": task_status,
                "responses": []
            }
            ...
    ]
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции

## Функция change_task

Функция обновляет статус задачи.

**Parameters:**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `task_id` (integer): id задачи
* `status` (boolean): статус задачи (`True` - задание выполнено, `False` - задание ещё не выполнено)

**Returns**

```json
    {
        "success": true,
        "exception": null,
        "task_id": task_id
    }
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции
* `dog_not_found`: собака с указанным id отсутствует в базе данных

## Функция create_task_response

Функция создает отчёт о задании и записывает его в базу данных.

**Parameters:**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `task_id` (integer): id задачи
* `proof` (string): доказательство выполненного задания

**Returns**

```json
    {
        "id": response_id,
        "user_id": user_id,
        "task_id": task_id,
        "proof": proof,
        "status": False
    }
```

**Raise**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции
* `task_not_found`: задача с указанным id отсутствует в базе данных

## Функция change_response

Функция принимает отчёт к задаче. Задача считается выполненной.

**Parameters:**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `response_id` (integer): id отчёта

**Returns**

```json
    {
        "success": true,
        "exception": null,
        "response_id": <response_id>
    }
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции
* `response_not_found`: отчёт с указанным id отсутствует в базе данных

## Функция get_task_responses

Функция выдает все отчёты по конкретному заданию

**Parameters:**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `task_id` (integer): id задачи

**Returns**

```json
    [
        {
            "id": response_id,
            "task_id": task_id,
            "user_id": user_id,
            "proof": response_proof,
            "deleted": response_status
        },
        {
            "id": response_id,
            "task_id": task_id,
            "user_id": user_id,
            "proof": response_proof,
            "deleted": response_status
        }
        ...
    ]
```

**Raises**

* `invalid_token`: указан неверный токен, недостаточно прав для выполнения функции
* `task_not_found`: задача с указанным id отсутствует в базе данных

## Функция read_all_responses

Функция выдает `limit` отчётов на задания, пропуская `skip` строчек

**Parameters:**

* `token` (string): токен пользователя. Выдается функцией `login_user`
* `skip` (integer): число задач к пропуску
* `limit` (integer): максимальное число задач в выборке

**Returns**

```json
    [
        {
            "id": <response_id>,
            "task_id": <task_id>,
            "user_id": <user_id>,
            "proof": <response_proof>,
            "deleted": <response_status>
        },
        {
            "id": <response_id>,
            "task_id": <task_id>,
            "user_id": <user_id>,
            "proof": <response_proof>,
            "deleted": <response_status>
        }
        ...
    ]
```

**Raises**

* `invalid_login`: пользователя с таким именем не существует, или веден неверный пароль

