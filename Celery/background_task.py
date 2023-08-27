import time

from fastapi import FastAPI, BackgroundTasks

app = FastAPI()


def send_push_notification(device_token: str):
    time.sleep(10)
    with open("notification.log", mode="a")  as notification_log:
        response = f"Successfully sent push notification to device: {device_token}"
        notification_log.write(response)


@app.get("/push/{device_token}")
async def notify(device_token: str, backgroundtask: BackgroundTasks):
    backgroundtask.add_task(send_push_notification, device_token)
    return {"message": "Notification sent to device"}
