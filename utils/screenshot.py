import os
import allure
from datetime import datetime


def take_screenshot(driver, name):

    folder = "reports/screenshots"
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = f"{folder}/{name}_{timestamp}.png"

    driver.save_screenshot(file_path)

    with open(file_path, "rb") as file:
        allure.attach(
            file.read(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    return file_path
