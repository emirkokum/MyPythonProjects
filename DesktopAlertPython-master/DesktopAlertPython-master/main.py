import time
from plyer import notification

alert_hour = input("Please enter hour:")

alert_minute = input("Please enter minute:")

notify_title = "Hello Emir"
notify_message = f"It's {alert_hour} : {alert_minute}"

while True:
    myHour = time.localtime(time.time())

    if int(alert_hour) == myHour.tm_hour and int(alert_minute) == myHour.tm_min:
        notification.notify(title=notify_title, app_name="Alarm", message=notify_message, app_icon="icon/clock_icon.ico", timeout=5, toast=False)
        break
    else:
        pass
print("Alert is Over.")


