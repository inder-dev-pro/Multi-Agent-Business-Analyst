import numpy as np
from tensorflow.keras.models import load_model
loaded_model = load_model(r"models\startup_prediction_model.h5")
loaded_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# ✅ New Data for Prediction
new_data = {
    "funding_total_usd": [5000000],   # Example: $5M in funding
    "funding_rounds": [3],            # 3 funding rounds
    "first_funding_years": [2.5],     # First funding happened 2.5 years after founding
    "last_funding_years": [5.0],      # Last funding happened 5 years after founding
    "country_code": [0.75],           # Encoded country value
    "category_index": [15]            # Category index (from LabelEncoder)
}

# ✅ Convert Data to NumPy Arrays
X_numerical = np.array([new_data["funding_total_usd"],
                         new_data["funding_rounds"],
                         new_data["first_funding_years"],
                         new_data["last_funding_years"],
                         new_data["country_code"]]).T.astype(np.float32)

X_category = np.array(new_data["category_index"]).reshape(-1, 1).astype(np.int32)
# Evaluate model to check if it's working
test_loss, test_acc = loaded_model.evaluate([X_numerical,X_category], np.array([[1, 0, 0, 0]]))
print(f"Test Loss: {test_loss}, Test Accuracy: {test_acc}")

# ✅ Make Prediction
predictions = loaded_model.predict([X_numerical, X_category])

# ✅ Convert to Class Label
status_classes = ["operating", "closed", "acquired", "ipo"]
predicted_index = np.argmax(predictions, axis=1)[0]

# ✅ Print Final Prediction
print("Predicted Startup Status:", predictions)