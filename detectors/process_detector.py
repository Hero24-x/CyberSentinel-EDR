BLACKLIST = [
    "keylogger.exe",
    "stealer.exe",
    "hacktool.exe"
]

class ProcessDetector:

    @staticmethod
    def detect(processes):

        alerts = []

        for process in processes:

            name = str(
                process["name"]
            ).lower()

            if name in BLACKLIST:

                alerts.append({
                    "severity": "HIGH",
                    "message":
                    f"Blacklisted process detected: {name}"
                })

        return alerts
