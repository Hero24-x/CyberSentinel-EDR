class AlertResponder:

    @staticmethod
    def send(alert):

        print(
            f"[ALERT] "
            f"{alert['severity']} | "
            f"{alert['message']}"
        )
