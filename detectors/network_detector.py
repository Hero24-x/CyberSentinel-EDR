class NetworkDetector:

    @staticmethod
    def detect(connections):

        alerts = []

        count = len(connections)

        if count > 500:

            alerts.append({
                "severity": "MEDIUM",
                "message":
                f"Large number of connections: {count}"
            })

        return alerts
