class FitnessTrainer:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.height = 0
        self.weight = 0
        self.training_time = ""
        self.training_days = 0

    def introduce(self):
        print("Hi there! I'm your personal fitness trainer.")
        print("I'm here to help you achieve your fitness goals.")

    def get_user_data(self):
        print("First, let's start by getting some information about you.")
        self.name = input("What's your name? ")
        print(f"Nice to meet you, {self.name}!")
        self.age = int(input("How old are you? "))
        self.height = float(input("What's your height in centimeters? ")) / 100  # Convert to meters
        self.weight = float(input("What's your weight in kilograms? "))
    
    def get_training_time(self):
        print("When do you prefer to exercise?")
        self.training_time = input("Enter 'morning', 'evening', or 'anytime': ")

    def get_training_days(self):
        self.training_days = int(input("How many days do you want to do this workout streak? "))
    
    def beginner_training(self):
        print("Beginner training:")
        print("1. Push-ups - 3 sets of 10 repetitions each")
        print("2. Squats - 3 sets of 12 repetitions each")
        print("3. Lunges - 3 sets of 10 repetitions each")
        print("4. Planks - 3 sets of 30 seconds each")

    def intermediate_training(self):
        print("Intermediate training:")
        print("1. Burpees - 3 sets of 10 repetitions each")
        print("2. Deadlifts - 3 sets of 8 repetitions each")
        print("3. Pull-ups - 3 sets of 8 repetitions each")
        print("4. Russian twists - 3 sets of 15 repetitions each")

    def fat_burn_training(self):
        print("Fat burn training:")
        print("1. Jumping jacks - 3 sets of 20 repetitions each")
        print("2. Mountain climbers - 3 sets of 15 repetitions each")
        print("3. High knees - 3 sets of 20 repetitions each")
        print("4. Bicycle crunches - 3 sets of 12 repetitions each")

    def suggest_training(self):
        print("Choose your training option:")
        print("1. Beginner Training")
        print("2. Intermediate Training")
        print("3. Fat Burn Training")

        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            self.beginner_training()
        elif choice == 2:
            self.intermediate_training()
        elif choice == 3:
            self.fat_burn_training()
        else:
            print("Invalid choice. Please choose again.")

    def suggest_exercises(self):
        print("Based on your age and fitness level, here are some recommended exercises:")
        if 15 <= self.age <= 20:
            print("Your age group: 15-20")
            print("It's recommended to start with light to moderate intensity exercises.")
        elif 21 <= self.age <= 30:
            print("Your age group: 21-30")
            print("You can focus on building strength and endurance.")
        elif 31 <= self.age <= 45:
            print("Your age group: 31-45")
            print("Balanced workouts combining strength training and cardio are beneficial.")
        else:
            print("Your age group: 45+")
            print("Low-impact exercises like walking, swimming, and yoga can be beneficial.")

    def provide_information(self):
        print("Here's your daily exercise training information:")
        print("1. Warm-up: Start with 5-10 minutes of light cardio (e.g., jogging, jumping jacks).")
        print("2. Main workout: Perform the specified number of sets and repetitions for each exercise.")
        print("3. Cool-down: Finish with 5-10 minutes of stretching exercises.")

    def get_feedback(self):
        feedback = input("Do you have any feedback or questions? (yes/no): ")
        if feedback.lower() == "yes":
            user_feedback = input("Please provide your feedback or ask your question: ")
            print("Thank you for your feedback! We'll make sure to address it.")
        else:
            print("If you have any questions or feedback later, feel free to reach out!")

    def say_goodbye(self):
        print("Great job today! Remember to stay consistent with your workouts.")
        print("If you have any questions or need further assistance, feel free to ask.")
        print("Have a fantastic day!")

    def start(self):
        self.introduce()
        self.get_user_data()
        self.get_training_time()
        self.get_training_days()
        self.suggest_training()
        self.suggest_exercises()
        self.provide_information()
        self.get_feedback()
        self.say_goodbye()


if __name__ == "__main__":
    trainer = FitnessTrainer()
    trainer.start()
