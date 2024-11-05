# Сервис для телеграм бота "Бункер", который является аналогом настольной игры.

## Установка проекта на Windows

- Clone repository
    ```console
    git clone https://github.com/FrozZzy1/bunker-backend.git
    cd bunker-backend
    ```

- Create and fill environment variables
    ```console
    cp .env.exameple .env
    ```

- Create virtual environments
    ```console
    python -m venv venv
    venv/scripts/activate
    ```

- Installing requirements
    ```console
    pip install poetry
    poetry install
    ```

- Start app
    ```console
    uvicorn app.run:app
    ```

## Установка проекта на Linux

- Clone repository
    ```bash
    git clone https://github.com/FrozZzy1/bunker-backend.git
    cd bunker-backend
    ```

- Create and fill environment variables
    ```bash
    cp .env.exameple .env
    ```

- Create virtual environments
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

- Installing requirements
    ```bash
    pip3 install poetry
    poetry install
    ```

- Start app
    ```bash
    uvicorn app.run:app
    ```
