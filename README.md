# Family Weather Assistant ☀️

A bilingual, mobile-first weather PWA designed to help families stay connected across different cities.

🌐 **Live App:**  
https://ivyzhang1113.github.io/family-weather-assistant/

📱 Installable on supported mobile devices as a Progressive Web App (PWA).

---

## About

Family Weather Assistant is a lightweight weather app for families whose members live in different cities or countries.

Instead of checking several weather apps separately, users can save multiple cities and quickly view each location's weather, local time, air quality, and practical daily recommendations in one place.

The project started as a Python/Streamlit prototype and was later rebuilt as a mobile-first Progressive Web App using HTML, CSS, and JavaScript.

---

## Features

### 🌍 Multi-City Weather
Search, add, save, remove, and reorder multiple cities.

Each city card includes:
- Current temperature
- Feels-like temperature
- Weather conditions
- Rain probability
- Wind speed
- UV index
- US AQI
- PM2.5
- Local date and time

### 🌏 Bilingual Location System
The interface supports both **Chinese and English**. City, state/province, and country names change together when the language is switched.

Examples:
- 广州 — 广东 · 中国
- 亚特兰大 — 佐治亚州 · 美国
- Guangzhou — Guangdong · China
- Atlanta — Georgia · United States

Search results also include state/province and country information to help distinguish places with the same name.

### 👕 Daily Recommendations
Weather data is converted into simple everyday suggestions, including umbrella recommendations, clothing suggestions, sun protection, and air-quality precautions.

### 🔄 City Comparison
Saved cities can be compared directly by local time difference and temperature difference.

### 💾 Persistent Cities
Saved cities and their order are stored locally in the browser and remain available when the app is reopened.

### 📱 Progressive Web App
Family Weather Assistant can be installed on supported mobile devices and launched directly from the Home Screen. No App Store installation is required.

---

## Tech Stack
- HTML
- CSS
- JavaScript
- Open-Meteo Forecast API
- Open-Meteo Geocoding API
- Open-Meteo Air Quality API
- Progressive Web App (PWA)
- LocalStorage
- Service Worker
- GitHub Pages

The app runs entirely in the browser and does not require an API key or backend server.

---

## Try It
Open the live application:

https://ivyzhang1113.github.io/family-weather-assistant/

### Install on iPhone
1. Open the website in Safari.
2. Tap **Share**.
3. Select **Add to Home Screen**.
4. Launch Family Weather directly from the Home Screen.

---

## Local Development
Clone the repository and start a local HTTP server:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

`localhost` is only used for local development. The public version runs through GitHub Pages.

---

## Project Status
**Stable**

Current public version includes multi-city weather, bilingual location support, state/province/country disambiguation, air quality, local date and time, daily recommendations, city comparison, persistent city storage, and mobile PWA installation.

Future improvements may include forecasts, notifications, location-based weather, and additional personalization.

---

## License
MIT License
