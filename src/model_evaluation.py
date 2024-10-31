# model_evaluation.py
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(model, X_test, y_test):
    """Evaluates model performance and prints MSE and R-squared."""
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r_squared = r2_score(y_test, y_pred)
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R^2 Score: {r_squared:.2f}")
    return mse, r_squared
