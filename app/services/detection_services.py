BLACKLIST = [
    "keylogger.exe",
    "stealer.exe",
    "hacktool.exe"
]

class DetectionService:

    @staticmethod
    def analyze(processes):

        alerts = []

        for process in processes:

            name = str(
                process["name"]
            ).lower()

            if name in BLACKLIST:

                alerts.append({
                    "severity": "HIGH",
                    "message":
                    f"Suspicious Process: {name}"
                })

        return alerts
