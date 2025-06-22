# main.py

def ask_questions():
    print(" Welcome to AI Career Advisor Bot!")
    interest = input("1. What interests you most (AI / Web / Hardware)? ")
    coding = input("2. Do you enjoy coding? (yes / no): ")
    math = input("3. Are you good at math? (yes / no): ")

    print("\n Based on your answers...")

    if interest.lower() == "ai" and coding.lower() == "yes" and math.lower() == "yes":
        print(" You can become an AI Engineer or Data Scientist!")
    elif interest.lower() == "web":
        print(" You can become a Web Developer or UI/UX Designer!")
    elif interest.lower() == "hardware":
        print(" You can explore Embedded Systems or Robotics!")
    else:
        print(" Try exploring multiple fields and find what you love!")

ask_questions()
