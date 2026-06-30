from datetime import datetime

class ReportGenerator:

    @staticmethod
    def generate(alerts):

        filename = (
            f"reports/report_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )

        with open(filename, "w") as report:

            report.write("CyberSentinel EDR Report\n")
            report.write("=" * 40 + "\n\n")

            for alert in alerts:
                report.write(
                    f"[{alert['severity']}] "
                    f"{alert['message']}\n"
                )

        return filename
