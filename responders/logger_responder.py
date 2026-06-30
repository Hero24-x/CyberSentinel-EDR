from datetime import datetime

class LoggerResponder:

    LOG_FILE = "logs/alerts.log"

    @staticmethod
    def save(alert):

        with open(
            LoggerResponder.LOG_FILE,
            "a"
        ) as f:

            f.write(
                f"[{datetime.now()}] "
                f"{alert['severity']} "
                f"{alert['message']}\n"
            )
