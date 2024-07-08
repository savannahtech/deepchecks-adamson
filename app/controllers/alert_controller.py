from sqlalchemy.orm import Session
import numpy as np

from app.models.alert import Alert
from app.models.interaction import Interaction


def check_threshold(metric_value: float, threshold: float) -> bool:
    return metric_value > threshold


def check_outlier(metric_value: float, values: list) -> bool:
    mean = np.mean(values)
    std_dev = np.std(values)
    return abs(metric_value - mean) > 2 * std_dev


def create_alerts(db: Session, interaction: Interaction):
    input_values = [i.input_metric for i in db.query(Interaction).all()]
    output_values = [i.output_metric for i in db.query(Interaction).all()]

    if check_threshold(interaction.input_metric, 50):  # Example threshold
        alert = Alert(
            interaction_id=interaction.id,
            element="input",
            metric_value=interaction.input_metric,
            alert_type="threshold"
        )
        db.add(alert)

    if check_outlier(interaction.input_metric, input_values):
        alert = Alert(
            interaction_id=interaction.id,
            element="input",
            metric_value=interaction.input_metric,
            alert_type="outlier"
        )
        db.add(alert)

    if check_threshold(interaction.output_metric, 50):  # Example threshold
        alert = Alert(
            interaction_id=interaction.id,
            element="output",
            metric_value=interaction.output_metric,
            alert_type="threshold"
        )
        db.add(alert)

    if check_outlier(interaction.output_metric, output_values):
        alert = Alert(
            interaction_id=interaction.id,
            element="output",
            metric_value=interaction.output_metric,
            alert_type="outlier"
        )
        db.add(alert)

    db.commit()


def get_alerts(db: Session, interaction_id: int = None):
    if interaction_id:
        alerts = db.query(Alert).filter(Alert.interaction_id == interaction_id).all()
    else:
        alerts = db.query(Alert).all()
    return [alert.as_dict() for alert in alerts]
