#
#  Müəllif hüququ (C) 2021-2022 by offlineflood@Github, < https://github.com/ChatBot >.
#
# Bu faylın bir hissəsidir < https://github.com/offlineflood/ChatBot > layihə,
# və "GNU v3.0 Lisenziya Müqaviləsi" əsasında buraxılır".
# Zəhmət olmasa baxın < https://github.com/offlineflood/ChatBot/blob/master/LICENSE >
#
# Bütün hüquqlar qorunur.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# my.telegram.org saytından əldə edin.
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

## Telegram-da @Botfather-dən əldə edin.
BOT_TOKEN = getenv("BOT_TOKEN")

# SUDO İSTİFADƏÇİLƏRİ
SUDO_USER = list(
    map(int, getenv("SUDO_USER", "").split())
)  # Daxiletmə növü tam ədəd olmalıdır.

# Bunun üçün Şəxsi Qrup ID-sinə ehtiyacınız olacaq.
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))

# Kimsə botunuzu işə saldıqda göstəriləcək mesaj.
PRIVATE_START_MESSAGE = getenv(
    "PRIVATE_START_MESSAGE",
    "Hello! Welcome to my Personal Assistant Bot",
)

# Söhbətlərinizi və statistikalarınızı saxlamaq üçün verilənlər bazası... MongoDB əldə edin:-  https://offline.gitbook.io/ChatBot/deployment/mongodb#4.-youll-see-a-deploy-cloud-database-option.-please-select-shared-hosting-under-free-plan-here
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
