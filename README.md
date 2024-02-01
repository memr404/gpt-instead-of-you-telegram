# Telegram Bot with GPT Integration README (Ниже на русском языке)

This project is a Telegram bot integrated with the GPT model to provide automated responses to messages. It uses the Telethon library to interact with Telegram's API and a custom GPT module for generating responses. The bot can be started or stopped by sending specific commands and maintains a history of conversations to provide contextually relevant replies.

## Features

- **Automated Responses**: Utilizes GPT to generate conversational replies to messages.
- **Start/Stop Commands**: Control the bot's operation by sending 'start' or 'stop' messages.
- **Conversation History**: Maintains a history of interactions for each chat to provide context to the GPT model.
- **User and Bot Filtering**: Ignores messages from bots and only responds to messages from user-initiated chats.

## Requirements

- Python 3.6+
- Telethon
- asyncio
- A custom GPT model or API (assumed to be accessed via a `chat_with_gpt` function in a `gpt` module)

## Configuration

Before running the bot, you need to set up your configuration file (`config.py`). This file should contain:

- `api_id`: Your Telegram API ID
- `api_hash`: Your Telegram API Hash
- `your_id`: Your Telegram User ID (to control the start/stop commands)
- `gpt_key`: Your GPT API key

## Installation

1. Clone this repository or copy the code to your local machine.
2. Install the required Python packages:

```bash
pip install telethon asyncio
```

3. Create a `config.py` file with your Telegram and GPT configuration details.
4. Ensure the `gpt` module and the `chat_with_gpt` function are correctly set up and accessible.

## Usage

Run the script using Python:

```bash
python your_script_name.py
```

Once running, the bot will listen for messages. You can control the bot by sending the following commands from your Telegram account:

- Send `start` to activate the bot's response feature.
- Send `stop` to deactivate the bot's response feature.

The bot will automatically respond to incoming messages from user chats when activated.

## How It Works

- The bot initializes a `TelegramClient` session and listens for new messages.
- If a message containing 'stop' or 'start' is received from the configured user ID, the bot's working state is toggled accordingly.
- For other incoming messages from user chats, the bot checks if it's in the working state.
- If so, it retrieves the conversation history, interacts with the GPT model to generate a response, and sends this back to the chat.
- The bot includes a delay between actions to mimic a more natural conversation pace and to comply with Telegram's rate limits.



# README для Telegram бота с интеграцией GPT

Этот проект представляет собой Telegram бота, интегрированного с моделью GPT для автоматического ответа на сообщения. Используется библиотека Telethon для взаимодействия с API Telegram и пользовательский модуль GPT для генерации ответов. Бот может быть запущен или остановлен с помощью специальных команд и поддерживает историю беседы для предоставления контекстуально релевантных ответов.

## Особенности

- **Автоматизированные ответы**: Использование GPT для генерации ответов на сообщения.
- **Команды запуска/остановки**: Управление работой бота с помощью сообщений 'start' или 'stop'.
- **История беседы**: Поддержка истории взаимодействий для каждого чата для предоставления контекста модели GPT.
- **Фильтрация пользователей и ботов**: Игнорирование сообщений от ботов и ответ только на сообщения от пользовательских чатов.

## Требования

- Python 3.6+
- Telethon
- asyncio
- Пользовательская модель GPT или API (предполагается, что доступ осуществляется через функцию `chat_with_gpt` в модуле `gpt`)

## Настройка

Перед запуском бота необходимо настроить файл конфигурации (`config.py`). Этот файл должен содержать:

- `api_id`: Ваш Telegram API ID
- `api_hash`: Ваш Telegram API Hash
- `your_id`: Ваш Telegram User ID (для управления командами start/stop)
- `gpt_key`: Ваш ключ API GPT

## Установка

1. Клонируйте этот репозиторий или скопируйте код на локальный компьютер.
2. Установите необходимые пакеты Python:

```bash
pip install telethon asyncio
```

3. Создайте файл `config.py` с деталями конфигурации Telegram и GPT.
4. Убедитесь, что модуль `gpt` и функция `chat_with_gpt` правильно настроены и доступны.

## Использование

Запустите скрипт с помощью Python:

```bash
python имя_вашего_скрипта.py
```

После запуска бот будет ожидать сообщений. Управлять ботом можно, отправляя следующие команды с вашего аккаунта Telegram в "Избарнное":

- Отправьте `start`, чтобы активировать функцию ответов бота.
- Отправьте `stop`, чтобы деактивировать функцию ответов бота.

Бот будет автоматически отвечать на входящие сообщения от пользовательских чатов при активации.

## Как это работает

- Бот инициализирует сессию `TelegramClient` и ожидает новые сообщения.
- Если от конфигурированного пользователя ID получено сообщение с 'stop' или 'start', состояние работы бота переключается соответственно.
- Для других входящих сообщений от пользовательских чатов бот проверяет своё состояние работы.
- Если активно, он извлекает историю беседы, взаимодействует с моделью GPT для генерации ответа и отправляет его обратно в чат.
- Бот включает задержку между действиями, чтобы имитировать более естественный темп беседы и соблюдать ограничения Telegram по частоте сообщений.


