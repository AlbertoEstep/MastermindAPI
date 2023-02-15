# Documentación API Mastermind

API Restful para el juego Mastermind.

## **_Ping_**

Endpoint para verificar que la API está en funcionamiento.

### Request

`GET /`

### Response

- `200 OK` con un objeto JSON con el mensaje `"response": "Mastermind"`

## **_Nuevo Juego_**

Endpoint para crear una nueva instancia del juego Mastermind.

### Request

`POST /mastermind/new_game`

### Response

- `200 OK` con un objeto JSON que contiene el ID del juego creado: `{"game_id": game_id}`

## **_Estado del Juego_**

Endpoint para obtener el estado actual de un juego específico.

### Request

`GET /mastermind/status/<game_id>`

Donde `<game_id>` es el ID del juego que se desea obtener.

### Response

- `200 OK` con un objeto JSON que contiene el estado actual del juego.

## **_Hacer una Jugada_**

Endpoint para hacer una jugada en un juego específico.

### Request

`POST /mastermind/guess/<game_id>`

Donde `<game_id>` es el ID del juego en el que se desea hacer una jugada.

El cuerpo de la solicitud debe contener un objeto JSON con la jugada a realizar en el siguiente formato: `{"guess": guess}`

Donde `guess` es una cadena de 4 letras que representa la jugada.

### Response

- `200 OK` con un objeto JSON que contiene el resultado de la jugada: `{"result": result}`

## **_Verificar una Jugada_**

Endpoint para verificar si una jugada es válida.

### Request

`POST /mastermind/check_guess/<game_id>`

Donde `<game_id>` es el ID del juego en el que se desea verificar la jugada.

El cuerpo de la solicitud debe contener un objeto JSON con la jugada a verificar en el siguiente formato: `{"guess": guess}`

Donde `guess` es una cadena de 4 letras que representa la jugada.

### Response

- `200 OK` si la jugada es válida.
- `400 Bad Request` si la jugada no es válida, en cuyo caso se devuelve un objeto JSON con un mensaje de error: `{"error": error_message}`

## **_Verificar el Estado de un Juego_**

Endpoint para verificar si un juego existe.

### Request

`GET /mastermind/check_game/<game_id>`

Donde `<game_id>` es el ID del juego que se desea verificar.

### Response

- `200 OK` si el juego existe.
- `400 Bad Request` si el juego no existe, en cuyo caso se devuelve un objeto JSON con un mensaje de error: `{"error": error_message}`
