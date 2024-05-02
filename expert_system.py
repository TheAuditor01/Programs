def load_disease_symptoms(filename):
    disease_symptoms = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                disease, symptoms = line.split(":")
                disease = disease.strip()
                symptoms = [symptom.strip() for symptom in symptoms.split(",")]
                disease_symptoms[disease] = symptoms
    return disease_symptoms

def ask_question(question):
    while True:
        response = input(question + " (Yes/No/Not Sure) :-  ").strip().lower()
        if response in ['yes', 'no', 'not sure']:
            if response == 'yes':
                return True
            elif response == 'no':
                return False
            else:
                return None
        else:
            print("\nInvalid response. Please enter 'Yes', 'No', or 'Not Sure'.")

def diagnose(disease_symptoms, symptoms):
    matched_diseases = []
    for disease, symptom_list in disease_symptoms.items():
        if all(symptoms.get(symptom, None) in [True, None] for symptom in symptom_list):
            matched_diseases.append(disease)

    if matched_diseases:
        print("\n\nBased on your symptoms, the possible illnesses you might be suffering from are:")
        for disease in matched_diseases:
            print(f"- {disease}")
    else:
        reported_symptoms = [symptom for symptom, present in symptoms.items() if present]
        if reported_symptoms:
            print(f"\n\nYou reported the following symptoms: {', '.join(reported_symptoms)}")
            print("However, based on our knowledge base, we could not match these symptoms to any known illness.")
            print("It is recommended that you seek medical advice from a doctor for further evaluation.")
        else:
            print("\n\nNo symptoms were reported. You appear to be healthy!")

def run():
    print("Hello, This is a simple rule-based Medical Expert System.")
    print("Please answer the following questions with 'Yes', 'No', or 'Not Sure'.")
    print("The system will try to diagnose if you have any illness based on your responses.")

    username = input("What's your name? :- ")
    print(f"Hello {username}! Let's start the diagnosis process.")

    disease_symptoms = load_disease_symptoms("disease.txt")

    questions = [
        ("cough", "Do you have cough?"),
        ("fever", "Do you have fever?"),
        ("chest_pain", "Do you have chest pain?"),
        ("fatigue", "Do you experience fatigue?"),
        ("headache", "Are you currently experiencing any headaches?"),
        ("sunken_eyes", "Do you experience sunken eyes?"),
        ("fainting", "Do you faint occasionally?"),
        ("restlessness", "Are you experiencing restlessness?"),
        ("sore_throat", "Do you have sore throat?")
    ]

    symptoms = {}
    for symptom, question in questions:
        answer = ask_question(question)
        symptoms[symptom] = answer

    diagnose(disease_symptoms, symptoms)

if __name__ == "__main__":
    run()