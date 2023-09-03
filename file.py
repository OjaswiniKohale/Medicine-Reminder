import time
from plyer import notification

if __name__ == "__main__":
    while(True):
        notification.notify(
            title = "Take your medicines",
            message = "Paracetomol",
            toast= True,
            app_icon = "C:\\Users\HP\Desktop\python\projects\icon.ico",
            timeout=5
        )
        time.sleep(60*60*8)
        