# model_training.py
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

def train_model(X_train, y_train, model_type='linear'):
    """Trains a specified model type and returns the trained model."""
    if model_type == 'linear':
        model = LinearRegression()
        model.fit(X_train, y_train)
    elif model_type == 'random_forest':
        rf = RandomForestRegressor(random_state=42)
        param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20]}
        model = GridSearchCV(rf, param_grid, cv=3)
        model.fit(X_train, y_train)
    return model
