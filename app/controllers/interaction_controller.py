from sqlalchemy.orm import Session

from app.controllers.alert_controller import create_alerts
from app.controllers.metrics_controller import calculate_input_metric, calculate_output_metric
from app.models.interaction import Interaction
import csv
from io import StringIO


def create_interaction(input_text: str, output_text: str, db: Session):
    try:
        input_metric_value = calculate_input_metric(input_text)
        output_metric_value = calculate_output_metric(output_text)

        interaction = Interaction(
            input_text=input_text,
            output_text=output_text,
            input_metric=input_metric_value,
            output_metric=output_metric_value
        )

        db.add(interaction)
        db.commit()
        db.refresh(interaction)

        create_alerts(db, interaction)

        return True
    except Exception as e:
        raise e


def create_interactions_from_csv(csv_data: str, db: Session):
    try:
        csv_reader = csv.DictReader(StringIO(csv_data))
        for row in csv_reader:
            input_text = row.get('Input')
            output_text = row.get('Output')

            if input_text is None or output_text is None:
                continue

            input_text = input_text.strip()
            output_text = output_text.strip()

            create_interaction(input_text, output_text, db)

        return True
    except Exception as e:
        raise e
