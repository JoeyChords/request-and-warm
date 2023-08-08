import datetime, logging, time, requests
from dotenv import dotenv_values

config = dotenv_values(".env")
COLD_URL = config["COLD_URL"]
logging.basicConfig(filename="warmer.log", level=logging.INFO)
timeStarted = datetime.datetime.now()
logging.info(
    timeStarted.strftime("%m/%d/%Y, %H:%M:%S")
    + "   requestAndWarm started on "
    + COLD_URL
)

while True:
    timeOfRequest = datetime.datetime.now()
    try:
        r = requests.get(COLD_URL)
        if r.status_code == 200:
            logging.info(
                timeOfRequest.strftime("%m/%d/%Y, %H:%M:%S")
                + "   "
                + COLD_URL
                + " returned status code "
                + str(r.status_code)
            )
        else:
            raise Exception()
    except:
        logging.exception(
            timeOfRequest.strftime("%m/%d/%Y, %H:%M:%S")
            + "   Status code "
            + str(r.status_code)
        )
    time.sleep(840)
