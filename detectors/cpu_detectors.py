class CpuDetector:

    CPU_LIMIT = 80

    @staticmethod
    def detect(system_data):

        alerts = []

        if system_data["cpu"] > \
           CpuDetector.CPU_LIMIT:

            alerts.append({
                "severity": "MEDIUM",
                "message":
                f"High CPU Usage: {system_data['cpu']}%"
            })

        return alerts
