# 🌟 Burmese Astrology AI App

A Flask-based web application that predicts astrological insights in Burmese based on a user's birthdate. Powered by DeepSeek's language model, it generates weekly, monthly, and yearly forecasts, personality traits, and lucky/unlucky attributes.

## ✨ Features

* **Weekly, Monthly, and Yearly Predictions** in Burmese language.
* **Personality Analysis** based on birthdate.
* **Things To Do / Avoid** including:
  - Lucky and unlucky colors
  - Lucky and unlucky numbers
  - Lucky and unlucky places
* **User-Friendly UI:** Built using Flask + Jinja templates.
* **Markdown to HTML Rendering** for rich display.
* **Powered by DeepSeek API** for accurate AI predictions.

## 🧠 Technologies Used

* **Flask** — Python web framework
* **OpenAI / DeepSeek API** — AI-based content generation
* **Markdown2** — Convert Markdown to HTML
* **dotenv** — For secure API key management
* **Jinja2** — HTML templating

## 📁 Project Structure

```
ai_baydin/
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
│   └── base.html
├── static/
│   └── css/
│     └── style.css
├── .env
├── requirements.txt
```

## 🔑 Environment Setup

1. **Create `.env` file** in your project root:

```
DEEPSEEK_API_KEY=sk-your-deepseek-api-key
```

> Never expose your API key publicly.

## 📦 Installation & Running

1. Clone the repository:

```bash
git clone https://github.com/PhoneMinKhant203/ai_baydin.git
```

2. Create virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the Flask server:

```bash
python app.py
```

## 💡 Usage

1. Enter your **birthdate** in YYYY-MM-DD format.
2. Choose one of the prediction types:
   - Weekly
   - Monthly
   - Yearly
   - Personality
   - Dos and Don'ts
3. Submit the form and view the prediction in beautifully rendered Burmese text.

## 🧪 Sample Prompts Used

* Weekly Forecast:
  > "Based on the birthdate 1995-03-15, predict the future for the current week in Burmese language..."

* Monthly Forecast:
  > "Based on the birthdate 1995-03-15, predict the future for the current month in Burmese language..."

* Personality:
  > "Based on the birthdate 1995-03-15, describe the personality traits..."

* Dos and Don’ts:
  > "Provide 5 lucky things, unlucky things, lucky colors, numbers, etc..."
