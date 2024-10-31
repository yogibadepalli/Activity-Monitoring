# main_pipeline.py
from src.data_loader import load_data, preprocess_data, split_data
from src.feature_engineering import select_features
from src.model_training import train_model
from src.model_evaluation import evaluate_model
from src.utils import get_data_path

def main():
    # Step 1: Load and preprocess the data
    data_path = get_data_path('collected_data.csv')
    data = load_data(data_path)
    clean_data = preprocess_data(data)
    
    # Step 2: Split the data into training and test sets
    X_train, X_test, y_train, y_test = split_data(clean_data)
    
    # Step 3: Feature selection
    selected_features = select_features(X_train, y_train, num_features=5)
    X_train_selected = X_train[selected_features]
    X_test_selected = X_test[selected_features]
    
    # Step 4: Train model with selected features
    model = train_model(X_train_selected, y_train, model_type='random_forest')
    
    # Step 5: Evaluate the model
    evaluate_model(model, X_test_selected, y_test)

if __name__ == "__main__":
    main()
