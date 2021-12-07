import schedule
import time

def job():
    print("I'm working...")

#schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
#schedule.every().day.at("22:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


#schedule.every().day.at("22:34").do(bot.loop.call_soon_threadsafe, send_channel)
schedule.every().day.at("22:34").do(job())