import boto3
import datetime
from flask import Flask, render_template, Blueprint

# Initialize Flask app
app = Flask(__name__)
blueprint = Blueprint("aws_billing", __name__)


def fetch_aws_bills(start_date, end_date):
    """Fetch AWS billing details using Boto3 Cost Explorer API."""
    session = boto3.Session()  # Uses environment variables or IAM role
    ce_client = session.client("ce")

    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    response = ce_client.get_cost_and_usage(
        TimePeriod={"Start": start_date_str, "End": end_date_str},
        Granularity="MONTHLY",
        Metrics=["BlendedCost"],
    )

    return response.get("ResultsByTime", [])  # Return bill details safely


@blueprint.route("/aws/")
def billing():
    """Flask route to display AWS billing data."""
    start_date = datetime.datetime(2024, 1, 14)
    end_date = datetime.datetime(2024, 2, 15)

    try:
        aws_bills = fetch_aws_bills(start_date, end_date)
    except Exception as e:
        return f"Error fetching AWS billing: {str(e)}"

    return render_template("billing.html", aws_bills=aws_bills)


# Register Blueprint
app.register_blueprint(blueprint)


@app.route("/")
def home():
    return "Welcome to the AWS Cost Explorer Web App! Navigate to /aws/ to view billing details."


if __name__ == "__main__":
    app.run(debug=True)
