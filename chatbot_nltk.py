from nltk import Chat, reflections


pairs = [
    ['my name is (.*)', ['Hello %1. Welcome to our fitness coaching service.']],
    ['(hi|hello|hey|hola)', ['Hello there! Welcome to our fitness coaching service. How can I assist you today?']],
    ['(.*)your name', ["I'm your personal fitness coach."]],
    ['(.*)what do you do', ['I provide personalized fitness guidance and support.']],
    ['(.*)fitness|(.*)workout', ['We offer a variety of fitness programs including cardio, strength training, and flexibility exercises.']],
    ['(.*)cardio', ['Cardio exercises like running, cycling, and swimming are excellent for improving cardiovascular health.']],
    ['(.*)strength training', ['Strength training helps build muscle mass and increase metabolism.']],
    ['(.*)flexibility', ['Flexibility exercises such as yoga and stretching improve range of motion and prevent injuries.']],
    ['(.*)nutrition|(.*)diet', ['Nutrition is crucial for achieving fitness goals. We provide guidance on healthy eating habits.']],
    ['(.*)workout plans', ['Our workout plans are tailored to individual needs, focusing on achieving specific goals.']],
    ['(.*)start a workout|(.*)begin workout', ['Great! Let’s start with some warm-up exercises.']],
    ['(.*)workout schedule', ['A consistent workout schedule is essential for progress. We recommend at least 3-5 sessions per week.']],
    ['(.*)tips for beginners', ['For beginners, it’s important to start slow, focus on proper form, and gradually increase intensity.']],
    ['(.*)bye|(.*)exit', ['Goodbye! Remember to stay motivated and consistent in your fitness journey.']],
    ['(.*)', ["I'm sorry, I didn't quite catch that. Could you please rephrase or ask another question?"]],
]

print("Welcome to our Fitness Coaching Service. How can I assist you today?")
chat = Chat(pairs, reflections)
chat.converse()
