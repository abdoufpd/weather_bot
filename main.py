from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
import datetime
import requests

token  = "8068914760:AAFVBkBxhs9EYn_0PqYcwoOw7-zvXS0Su4w"
bot_username = "Weather_checker_f_bot"
apikey = "a4ef56c17068a780cec02bccbab76aec"

async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hii 🙋‍♂️ , thanks for chatting with me i will try to give u the right weather info 😉")

async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am weather checker bot so u can give me ur city ! \\start")

async def custom_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("custom command")


def handle_response(text:str) ->str :
    processed:str = text.lower()
    if "hello" in processed:
        return "Hey , i am here to help u , can u provide me for ur city!"
    if "weather" in processed:
        return "oka can u enter ur city"  
    def basic_imojie(icon_code:str):
        mapping = {
            "01d": "☀️",      # clear sky (day)
            "01n": "🌙",      # clear sky (night)
            "02d": "⛅",      # few clouds (day)
            "02n": "🌙☁️",    # few clouds (night)
            "03d": "☁️",      # scattered clouds
            "03n": "☁️",
            "04d": "☁️☁️",    # broken clouds
            "04n": "☁️🌙",    # broken clouds at night
            "09d": "🌧️",      # shower rain
            "09n": "🌧️",
            "10d": "🌦️",      # rain (day)
            "10n": "🌧️🌙",    # rain (night)
            "11d": "⛈️",      # thunderstorm
            "11n": "⛈️",
            "13d": "❄️",      # snow
            "13n": "❄️",
            "50d": "🌫️",      # mist
            "50n": "🌫️",
        }

        icon_code = icon_code.strip().lower()  # clean up just in case
        emoji = mapping.get(icon_code)

        if emoji is None:
            print(f"[DEBUG] Unknown icon code: {icon_code}")
            return "❓"  # default emoji

        return emoji
    
    


    apiUrl =f'https://api.openweathermap.org/data/2.5/weather?q={text}&appid={apikey}'
    response =requests.get(apiUrl)
    if response.status_code ==200:
        data = response.json()
       
        organized_data = f'The weather in {data['name'] } is :\n {data['weather'][0]['main']} ( {data['weather'][0]['description']})\n Tempurature:{round(data['main']["temp"]-273.15,2)}°C \n Humidity:{data['main']["humidity"]}\n Sunrise : {datetime.datetime.utcfromtimestamp(data['sys']["sunrise"]+data["timezone"])}\n Sunset : {datetime.datetime.utcfromtimestamp(data['sys']["sunset"]+data["timezone"])}'
        return organized_data.encode('utf-8').decode('utf-8')
    else : return "please enter a correct city !"




async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type
    text:str = update.message.text
    t_info = f'User ({update.message.chat.id}) in {message_type}: "{text}"'
    with open("txt.txt",'a') as file :file.write(t_info)

    if message_type=='group':
        if bot_username in text:
            new_text:str= text.replace(bot_username,'').strip()
            response:str=handle_response(new_text)
        else :return    
    else:response:str = handle_response(text)
    with open("txt.txt",'a') as file :file.write(response)
    await update.message.reply_text(response)
async def error(update:Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused an error {context.error}')

if __name__=="__main__":
    print("starting...")
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start",start_command))
    app.add_handler(CommandHandler("help",help_command))
    app.add_handler(CommandHandler("custom",custom_command))

    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    app.add_error_handler(error)

    print("polling...")
    app.run_polling(poll_interval=3) 