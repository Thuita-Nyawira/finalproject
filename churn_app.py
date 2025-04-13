{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "902f4f47-1ecc-40b0-8df4-958809067b7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\emma\\anaconda3\\lib\\site-packages (1.37.1)\n",
      "Requirement already satisfied: scikit-learn in c:\\users\\emma\\anaconda3\\lib\\site-packages (1.5.1)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (5.3.3)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<3,>=1.20 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (24.1)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (2.2.2)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (10.4.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (4.25.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (16.1.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (13.7.1)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (8.2.3)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (4.11.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (3.1.43)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: watchdog<5,>=2.1.5 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from streamlit) (4.0.1)\n",
      "Requirement already satisfied: scipy>=1.6.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from scikit-learn) (1.13.1)\n",
      "Requirement already satisfied: joblib>=1.2.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from scikit-learn) (1.4.2)\n",
      "Requirement already satisfied: threadpoolctl>=3.1.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from scikit-learn) (3.5.0)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
      "Requirement already satisfied: toolz in c:\\users\\emma\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\emma\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2025.1.31)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\emma\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit scikit-learn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "97501531-bd78-4c9a-919f-0766e613bd9d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import joblib  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a8e864c2-96aa-441f-b692-74f8aa0c69b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load the Pre-trained Model ---\n",
    "try:\n",
    "    model = joblib.load('CPmodel.sav') \n",
    "except FileNotFoundError:\n",
    "    st.error(\"Error: 'CPmodel.sav' not found. Make sure the file is in the same directory.\")\n",
    "    st.stop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "66edbd44-0409-45d7-adf1-2722b5f2aaf9",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-13 19:37:15.343 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Emma\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "st.title(\"Customer Churn Prediction\")\n",
    "st.write(\"Enter the customer details below to predict if they will churn.\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "74dbfa57-efcd-4a1b-b192-77529352bec5",
   "metadata": {},
   "outputs": [],
   "source": [
    "gender = st.selectbox(\"Gender\", [\"Female\", \"Male\"])\n",
    "senior_citizen = st.selectbox(\"Senior Citizen\", [\"No\", \"Yes\"])\n",
    "partner = st.selectbox(\"Partner\", [\"No\", \"Yes\"])\n",
    "dependents = st.selectbox(\"Dependents\", [\"No\", \"Yes\"])\n",
    "tenure = st.number_input(\"Tenure (months)\", min_value=0, step=1)\n",
    "phone_service = st.selectbox(\"Phone Service\", [\"No\", \"Yes\"])\n",
    "multiple_lines = st.selectbox(\"Multiple Lines\", [\"No phone service\", \"No\", \"Yes\"])\n",
    "internet_service = st.selectbox(\"Internet Service\", [\"DSL\", \"Fiber optic\", \"No\"])\n",
    "online_security = st.selectbox(\"Online Security\", [\"No\", \"Yes\", \"No internet service\"])\n",
    "online_backup = st.selectbox(\"Online Backup\", [\"No\", \"Yes\", \"No internet service\"])\n",
    "device_protection = st.selectbox(\"Device Protection\", [\"No\", \"Yes\", \"No internet service\"])\n",
    "tech_support = st.selectbox(\"Tech Support\", [\"No\", \"Yes\", \"No internet service\"])\n",
    "streaming_tv = st.selectbox(\"Streaming TV\", [\"No\", \"Yes\", \"No internet service\"])\n",
    "streaming_movies = st.selectbox(\"Streaming Movies\", [\"No\", \"Yes\", \"No internet service\"])\n",
    "contract = st.selectbox(\"Contract\", [\"Month-to-month\", \"One year\", \"Two year\"])\n",
    "paperless_billing = st.selectbox(\"Paperless Billing\", [\"No\", \"Yes\"])\n",
    "payment_method = st.selectbox(\"Payment Method\", [\"Electronic check\", \"Mailed check\", \"Bank transfer (automatic)\", \"Credit card (automatic)\"])\n",
    "monthly_charges = st.number_input(\"Monthly Charges\", min_value=0.0)\n",
    "total_charges = st.number_input(\"Total Charges\", min_value=0.0)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "26b3d381-3b31-48ba-ac18-59628129fd5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "feature_data = {\n",
    "    'gender': 1 if gender == 'Male' else 0,\n",
    "    'SeniorCitizen': 1 if senior_citizen == 'Yes' else 0,\n",
    "    'Partner': 1 if partner == 'Yes' else 0,\n",
    "    'Dependents': 1 if dependents == 'Yes' else 0,\n",
    "    'tenure': tenure,\n",
    "    'PhoneService': 1 if phone_service == 'Yes' else 0,\n",
    "    'MultipleLines': 2 if multiple_lines == 'Yes' else (1 if multiple_lines == 'No phone service' else 0),\n",
    "    'InternetService': {'DSL': 0, 'Fiber optic': 1, 'No': 2}[internet_service],\n",
    "    'OnlineSecurity': {'No': 0, 'Yes': 1, 'No internet service': 2}[online_security],\n",
    "    'OnlineBackup': {'No': 0, 'Yes': 1, 'No internet service': 2}[online_backup],\n",
    "    'DeviceProtection': {'No': 0, 'Yes': 1, 'No internet service': 2}[device_protection],\n",
    "    'TechSupport': {'No': 0, 'Yes': 1, 'No internet service': 2}[tech_support],\n",
    "    'StreamingTV': {'No': 0, 'Yes': 1, 'No internet service': 2}[streaming_tv],\n",
    "    'StreamingMovies': {'No': 0, 'Yes': 1, 'No internet service': 2}[streaming_movies],\n",
    "    'Contract': {'Month-to-month': 0, 'One year': 1, 'Two year': 2}[contract],\n",
    "    'PaperlessBilling': 1 if paperless_billing == 'Yes' else 0,\n",
    "    'PaymentMethod': {'Electronic check': 0, 'Mailed check': 1, 'Bank transfer (automatic)': 2, 'Credit card (automatic)': 3}[payment_method],\n",
    "    'MonthlyCharges': monthly_charges,\n",
    "    'TotalCharges': total_charges\n",
    "}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "cac86496-88ef-4f75-8065-b7bda2763402",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "input_df = pd.DataFrame([feature_data])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": none,
   "id": "770fa103-4981-456a-bcad-dea05f483e02",
   "metadata": {},
   "outputs": [],
   "source": [
    "# --- 4. Make Prediction ---\n",
    "if st.button(\"Predict Churn\"):\n",
    "    try:\n",
    "        prediction = model.predict(input_df)\n",
    "        # Assuming your model outputs 0 for No Churn and 1 for Churn\n",
    "        if prediction[0] == 1:\n",
    "            st.error(\"Prediction: Customer is likely to CHURN.\")\n",
    "        else:\n",
    "            st.success(\"Prediction: Customer is NOT likely to churn.\")\n",
    "    except Exception as e:\n",
    "        st.error(f\"An error occurred during prediction: {e}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": none,
   "id": "7a72baa5-c721-4569-9462-a1eab9a04fb8",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.sidebar.header(\"About\")\n",
    "st.sidebar.info(\"This is a simple customer churn prediction app.\")\n",
    "st.sidebar.info(\"The model was trained on historical customer data.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
