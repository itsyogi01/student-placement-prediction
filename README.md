# 🎓 Student Placement Prediction

A Machine Learning project using Logistic Regression to predict student placement based on **CGPA** and **IQ**.  
Includes a Streamlit web app for interactive predictions.  
Achieved ~90% accuracy on test data.

---

## 📂 Project Structure
- `app.py` → Streamlit app
- `model.pkl` → Trained Logistic Regression model
- `requirements.txt` → Required Python libraries
- `README.md` → Project documentation

---

## ⚙️ Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/<your-username>/student-placement-prediction.git
cd student-placement-prediction
pip install -r requirements.txt
🚀 Usage
Run the Streamlit app:

bash
streamlit run app.py
Open the browser at http://localhost:8501 and enter student details (CGPA, IQ) to predict placement.

📊 Model
Algorithm: Logistic Regression

Features: CGPA, IQ

Accuracy: ~90%

🔮 Future Improvements
Add more features (e.g., communication skills, projects)

Try other ML models (Random Forest, SVM)

Deploy on cloud (Heroku/Streamlit Cloud)
