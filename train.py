import mlflow
import mlflow.sklearn
import joblib

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

print("Training Started...")

# Load Dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Start MLflow
mlflow.set_experiment("Iris Classification")

with mlflow.start_run():

    # Create Model
    model = DecisionTreeClassifier(random_state=42)

    # Train
    model.fit(X_train, y_train)

    # Prediction
    predictions = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, predictions)

    print("Accuracy:", accuracy)

    # Log Parameters
    mlflow.log_param("model", "DecisionTree")
    mlflow.log_param("random_state", 42)
    mlflow.log_param("test_size", 0.2)

    # Log Metric
    mlflow.log_metric("accuracy", accuracy)

    # Save Model
    joblib.dump(model, "model.pkl")

    # Log Model
    mlflow.sklearn.log_model(model, "model")

    print("Model Saved Successfully")