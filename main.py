# Import logging
import logging

# Import FastAPI
from fastapi import FastAPI, UploadFile, File, HTTPException, Request

# Import JSONResponse
from fastapi.responses import JSONResponse

# Import Pydantic
from pydantic import BaseModel

# Import our readers
from app.file_reader import read_text_file
from app.json_reader import read_json_file
from app.excel_reader import read_excel_file

# Import our common pipeline
from app.pipeline import process_logs

# Configure application logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Create a logger for this API module
logger = logging.getLogger(__name__)

# Create FastAPI application
app = FastAPI(
    title="Log Analyzer API",
    description="API for analyzing TXT, JSON and Excel log files",
    version="1.0.0"
)


@app.exception_handler(Exception)
async def handle_unexpected_exception(request: Request, exc: Exception):
    logger.error(
        "Unexpected error while handling %s %s: %s",
        request.method,
        request.url.path,
        exc,
        exc_info=(type(exc), exc, exc.__traceback__)
    )

    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error."}
    )

# ---------------------------------------------------------
# Temporary storage for alerts
# ---------------------------------------------------------

alerts_database = []

next_alert_id = 1

# ---------------------------------------------------------
# Root API
# ---------------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "Log Analyzer API is running"
    }

# ---------------------------------------------------------
# POST - Analyze JSON
# ---------------------------------------------------------

@app.post("/analyze/json")
async def analyze_json(file: UploadFile = File(...)):

    # Check file extension
    if not file.filename.lower().endswith(".json"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a JSON file."
        )

    # Temporary file location
    file_path = "data/uploaded.json"

    # Save uploaded file
    with open(file_path, "wb") as buffer:

        content = await file.read()

        buffer.write(content)

    # Read JSON logs
    logs = read_json_file(file_path)

    # Analyze logs
    alerts = process_logs(logs)

    # Store alerts
    store_alerts(alerts, file.filename)

    # Return response
    return {
        "filename": file.filename,
        "file_type": "JSON",
        "total_logs": len(logs),
        "alerts_found": len(alerts),
        "alerts": alerts
    }

# ---------------------------------------------------------
# POST - Analyze TXT
# ---------------------------------------------------------

@app.post("/analyze/txt")
async def analyze_txt(file: UploadFile = File(...)):

    # Check extension
    if not file.filename.lower().endswith(".txt"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a TXT file."
        )

    # Temporary file location
    file_path = "data/uploaded.txt"

    # Save uploaded file
    with open(file_path, "wb") as buffer:

        content = await file.read()

        buffer.write(content)

    # Read TXT logs
    logs = read_text_file(file_path)

    # Analyze logs
    alerts = process_logs(logs)

    # Store alerts
    store_alerts(alerts, file.filename)

    # Return response
    return {
        "filename": file.filename,
        "file_type": "TXT",
        "total_logs": len(logs),
        "alerts_found": len(alerts),
        "alerts": alerts
    }

# ---------------------------------------------------------
# POST - Analyze Excel
# ---------------------------------------------------------

@app.post("/analyze/excel")
async def analyze_excel(file: UploadFile = File(...)):

    # Check extension
    if not file.filename.lower().endswith(".xlsx"):
        raise HTTPException(
            status_code=400,
            detail="Please upload an XLSX Excel file."
        )

    # Temporary file location
    file_path = "data/uploaded.xlsx"

    # Save uploaded file
    with open(file_path, "wb") as buffer:

        content = await file.read()

        buffer.write(content)

    # Read Excel logs
    logs = read_excel_file(file_path)

    # Analyze logs
    alerts = process_logs(logs)

    # Store alerts
    store_alerts(alerts, file.filename)

    # Return response
    return {
        "filename": file.filename,
        "file_type": "Excel",
        "total_logs": len(logs),
        "alerts_found": len(alerts),
        "alerts": alerts
    }

# ---------------------------------------------------------
# Store alerts
# ---------------------------------------------------------

def store_alerts(alerts, filename):

    global next_alert_id

    for alert in alerts:

        alert_record = {
            "id": next_alert_id,
            "filename": filename,
            "message": alert
        }

        alerts_database.append(alert_record)

        next_alert_id += 1

# ---------------------------------------------------------
# GET - Get all alerts
# ---------------------------------------------------------

@app.get("/alerts")
def get_alerts():

    return {
        "total_alerts": len(alerts_database),
        "alerts": alerts_database
    }

# ---------------------------------------------------------
# GET - Get one alert
# ---------------------------------------------------------

@app.get("/alerts/{alert_id}")
def get_alert(alert_id: int):

    for alert in alerts_database:

        if alert["id"] == alert_id:

            return alert

    raise HTTPException(
        status_code=404,
        detail="Alert not found."
    )

# ---------------------------------------------------------
# PUT - Replace an alert
# ---------------------------------------------------------

class AlertUpdate(BaseModel):

    filename: str

    message: str

@app.put("/alerts/{alert_id}")
def update_alert(alert_id: int, alert_data: AlertUpdate):

    for alert in alerts_database:

        if alert["id"] == alert_id:

            alert["filename"] = alert_data.filename

            alert["message"] = alert_data.message

            return {
                "message": "Alert replaced successfully.",
                "alert": alert
            }

    raise HTTPException(
        status_code=404,
        detail="Alert not found."
    )

# ---------------------------------------------------------
# PATCH - Partially update an alert
# ---------------------------------------------------------

class AlertPatch(BaseModel):

    filename: str | None = None

    message: str | None = None

@app.patch("/alerts/{alert_id}")
def patch_alert(alert_id: int, alert_data: AlertPatch):

    for alert in alerts_database:

        if alert["id"] == alert_id:

            if alert_data.filename is not None:

                alert["filename"] = alert_data.filename

            if alert_data.message is not None:

                alert["message"] = alert_data.message

            return {
                "message": "Alert updated successfully.",
                "alert": alert
            }

    raise HTTPException(
        status_code=404,
        detail="Alert not found."
    )

# ---------------------------------------------------------
# DELETE - Delete an alert
# ---------------------------------------------------------

@app.delete("/alerts/{alert_id}")
def delete_alert(alert_id: int):

    for index, alert in enumerate(alerts_database):

        if alert["id"] == alert_id:

            deleted_alert = alerts_database.pop(index)

            return {
                "message": "Alert deleted successfully.",
                "alert": deleted_alert
            }

    raise HTTPException(
        status_code=404,
        detail="Alert not found."
    )
