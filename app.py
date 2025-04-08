from flask import Flask, render_template, request, redirect, url_for
from markupsafe import Markup
from datetime import datetime
from openai import OpenAI
import os
from dotenv import load_dotenv
import markdown2 

app = Flask(__name__)

# Configure OpenAI/DeepSeek API
load_dotenv()  # Load from .env file

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def render_markdown(markdown_text):
    html = markdown2.markdown(markdown_text)
    return Markup(html)

def get_astrological_response(prompt):
    """Helper function to get response from DeepSeek API"""
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a professional astrologer with deep knowledge of zodiac signs, birth charts, and planetary movements. Provide accurate predictions in Burmese language."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            stream=False,
            max_tokens=7000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def predict_weekly_future(birthdate):
    """Predict weekly future based on birthdate"""
    prompt = f"""
    Based on the birthdate {birthdate}, predict the future for the current week in Burmese language.
    Organize the prediction in these four categories:
    1. Economic (ငွေကြေးအခြေအနေ)
    2. Love (အချစ်ရေး)
    3. Education (ပညာရေး)
    4. Health (ကျန်းမာရေး)
    
    Make each prediction 3-4 sentences long and specific to this week.
    """
    return get_astrological_response(prompt)

def predict_monthly_future(birthdate):
    """Predict monthly future based on birthdate"""
    prompt = f"""
    Based on the birthdate {birthdate}, predict the future for the current month in Burmese language.
    Organize the prediction in these four categories:
    1. Economic (ငွေကြေးအခြေအနေ)
    2. Love (အချစ်ရေး)
    3. Education (ပညာရေး)
    4. Health (ကျန်းမာရေး)
    
    Make each prediction 4-5 sentences long and specific to this month.
    """
    return get_astrological_response(prompt)

def predict_yearly_future(birthdate):
    """Predict yearly future based on birthdate"""
    prompt = f"""
    Based on the birthdate {birthdate}, predict the future for the current year in Burmese language.
    Organize the prediction in these four categories:
    1. Economic (ငွေကြေးအခြေအနေ)
    2. Love (အချစ်ရေး)
    3. Education (ပညာရေး)
    4. Health (ကျန်းမာရေး)
    
    Make each prediction 5-6 sentences long and specific to this year.
    """
    return get_astrological_response(prompt)

def describe_personality(birthdate):
    """Describe personality based on birthdate"""
    prompt = f"""
    Based on the birthdate {birthdate}, describe the personality traits of this person in Burmese language.
    Include both positive and negative traits, about 8-10 sentences total.
    """
    return get_astrological_response(prompt)

def dos_and_donts(birthdate):
    """Provide recommendations based on birthdate"""
    prompt = f"""
    Based on the birthdate {birthdate}, provide the following in Burmese language:
    1. Things to do (ပြုလုပ်သင့်သည်များ) - 5 items
    2. Things not to do (မပြုလုပ်သင့်သည်များ) - 5 items
    3. Lucky colors (ကံကောင်းသည့်အရောင်များ) - 3 items
    4. Unlucky colors (ကံမကောင်းသည့်အရောင်များ) - 3 items
    5. Lucky numbers (ကံကောင်းသည့်နံပါတ်များ) - 3 items
    6. Unlucky numbers (ကံမကောင်းသည့်နံပါတ်များ) - 3 items
    7. Lucky places (ကံကောင်းသည့်နေရာများ) - 3 items
    8. Unlucky places (ကံမကောင်းသည့်နေရာများ) - 3 items
    
    Format the output clearly with headings for each section.
    """
    return get_astrological_response(prompt)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        birthdate = request.form['birthdate']
        prediction_type = request.form['prediction_type']
        
        # Validate date format
        try:
            datetime.strptime(birthdate, "%d-%m-%Y")
        except ValueError:
            return render_template('index.html', error="မှားယွင်းသော ရက်စွဲ format ဖြစ်နေပါသည်။ DD-MM-YYYY format ဖြင့် ပြန်လည်ရိုက်ထည့်ပါ။")
        
        result = ""
        title = ""
        
        if prediction_type == "weekly":
            result = render_markdown(predict_weekly_future(birthdate))
            title = "တစ်ပတ်အတွက် ကံကြမ္မာခန့်မှန်းချက်"
        elif prediction_type == "monthly":
            result = render_markdown(predict_monthly_future(birthdate))
            title = "တစ်လအတွက် ကံကြမ္မာခန့်မှန်းချက်"
        elif prediction_type == "yearly":
            result = render_markdown(predict_yearly_future(birthdate))
            title = "တစ်နှစ်အတွက် ကံကြမ္မာခန့်မှန်းချက်"
        elif prediction_type == "personality":
            result = render_markdown(describe_personality(birthdate))
            title = "ကိုယ်ရေးကိုယ်တာ စရိုက်လက္ခဏာများ"
        elif prediction_type == "dos_donts":
            result = render_markdown(dos_and_donts(birthdate))
            title = "ပြုလုပ်သင့်သည်များနှင့် ရှောင်ကြဉ်သင့်သည်များ"
        elif prediction_type == "all":
            weekly = render_markdown(predict_weekly_future(birthdate))
            monthly = render_markdown(predict_monthly_future(birthdate))
            yearly = render_markdown(predict_yearly_future(birthdate))
            personality = render_markdown(describe_personality(birthdate))
            dosdonts = render_markdown(dos_and_donts(birthdate))
            
            result = Markup(f"""
            <h3>တစ်ပတ်အတွက် ကံကြမ္မာခန့်မှန်းချက်:</h3>
            {weekly}
            <hr>
            <h3>တစ်လအတွက် ကံကြမ္မာခန့်မှန်းချက်:</h3>
            {monthly}
            <hr>
            <h3>တစ်နှစ်အတွက် ကံကြမ္မာခန့်မှန်းချက်:</h3>
            {yearly}
            <hr>
            <h3>ကိုယ်ရေးကိုယ်တာ စရိုက်လက္ခဏာများ:</h3>
            {personality}
            <hr>
            <h3>ပြုလုပ်သင့်သည်များနှင့် ရှောင်ကြဉ်သင့်သည်များ:</h3>
            {dosdonts}
            """)
            title = "အားလုံးခန့်မှန်းချက်များ"
        
        return render_template('result.html', title=title, result=result, birthdate=birthdate)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
