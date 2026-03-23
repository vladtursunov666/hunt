# Hunt Auto Bankruptcy Analytics MVP

MVP Telegram Mini App + Bot для аналитики авто-лотов с торгов по банкротству в РФ.

## Что внутри

- `backend/` — FastAPI API, хранение лотов, аналитика рынка, избранное.
- `bot/` — Telegram bot с кнопкой запуска Mini App и заглушкой подписки.
- `frontend/` — React + Vite Telegram Mini App.

## Быстрый старт

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API будет доступен на `http://localhost:8000`.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Mini App ожидает API по адресу `VITE_API_URL`, по умолчанию — `http://localhost:8000`.

### Bot

```bash
cd bot
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export TELEGRAM_BOT_TOKEN=... 
export TELEGRAM_WEBAPP_URL=https://your-mini-app-url
python bot.py
```

## MVP-функции

- хранение авто-лотов из одного источника торгов;
- расчёт средней рыночной цены по аналогам;
- классификация отклонения от рынка;
- фильтрация списка автомобилей;
- избранное по `telegram_id`;
- Telegram bot с deep entry в Mini App;
- premium-флаг и paywall-заглушка.

## Структура данных

- `cars`
- `market_comparables`
- `users`
- `favorites`

## Ограничения MVP

- 1 источник торгов — seed/stub ingestion;
- 1 источник рынка — seed/stub classifieds;
- обновление раз в день реализуется cron/worker-скриптом по расписанию;
- без фото-AI и без live-подписок.
