from flask import Blueprint
from flask import render_template

from app.services.process_service import ProcessService
from app.services.detection_service import DetectionService

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)

@dashboard_bp.route("/")
def home():

    processes = (
        ProcessService.get_processes()
    )

    alerts = (
        DetectionService.analyze(
            processes
        )
    )

    return render_template(
        "dashboard.html",
        process_count=len(processes),
        alerts=alerts
    )
