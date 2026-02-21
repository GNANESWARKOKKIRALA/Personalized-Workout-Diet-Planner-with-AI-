import json
import os

print("\n===========================================")
print("💪 AI-POWERED BODYBUILDER MUSCLE GAIN PLANNER 💪")
print("===========================================\n")

# ------------------------------
# User details input
# ------------------------------
name = input("Enter your name: ").capitalize()
weight = float(input("Weight (kg): "))
height = float(input("Height (cm): "))
age = int(input("Age: "))
activity_level = input("Activity level (low/medium/high): ").lower()
goal = "muscle"  # fixed for bodybuilding
day = input("Enter the day to see your workout: ").lower()

# ------------------------------
# AI logic for calories
# ------------------------------
if activity_level == "low":
    tdee_multiplier = 1.2
elif activity_level == "medium":
    tdee_multiplier = 1.5
else:
    tdee_multiplier = 1.75

# BMR calculation (Mifflin-St Jeor)
bmr = 10*weight + 6.25*height - 5*age + 5  # male version
tdee = bmr * tdee_multiplier
calories = tdee + 300  # +300 for muscle gain

# ------------------------------
# AI Workout Database
# ------------------------------
workout_db = {
    "monday": {
        "muscle_group": "Chest & Triceps",
        "exercises": ["Bench Press", "Incline Dumbbell Press", "Chest Fly", "Triceps Pushdown", "Dips"]
    },
    "tuesday": {
        "muscle_group": "Back & Biceps",
        "exercises": ["Pull-Ups", "Barbell Row", "Lat Pulldown", "Dumbbell Curls", "Hammer Curls"]
    },
    "wednesday": {"muscle_group": "Rest / Cardio", "exercises": ["Light Cardio 20-30 min", "Stretching"]},
    "thursday": {
        "muscle_group": "Shoulders & Abs",
        "exercises": ["Overhead Press", "Lateral Raises", "Front Raises", "Plank", "Hanging Leg Raises"]
    },
    "friday": {
        "muscle_group": "Legs",
        "exercises": ["Squats", "Leg Press", "Lunges", "Leg Curl", "Calf Raises"]
    },
    "saturday": {
        "muscle_group": "Full Body / Functional",
        "exercises": ["Deadlift", "Pull-Ups", "Push-Ups", "Farmer's Walk", "Plank"]
    },
    "sunday": {"muscle_group": "Rest", "exercises": ["Complete Rest / Optional Stretching"]}
}

# ------------------------------
# AI progression logic
# ------------------------------
progress_file = "progress.json"
if os.path.exists(progress_file):
    with open(progress_file, "r") as f:
        progress = json.load(f)
else:
    progress = {}

# Increment intensity based on past workouts
if day in progress:
    intensity = progress[day] + 1  # simple AI: increase sets/reps each week
else:
    intensity = 1

progress[day] = intensity

with open(progress_file, "w") as f:
    json.dump(progress, f)

# ------------------------------
# Display AI workout plan
# ------------------------------
if day in workout_db:
    print(f"\n📅 {day.capitalize()} - {workout_db[day]['muscle_group']} Workout (Intensity Level: {intensity})")
    for ex in workout_db[day]["exercises"]:
        print(f"- {ex} | {3+intensity} sets x {8+intensity} reps")
else:
    print("❌ Invalid day entered. Use Monday-Sunday.")

# ------------------------------
# AI diet suggestion
# ------------------------------
diet_plan = [
    "Breakfast: Oats + Eggs + Banana + Whey Protein",
    "Snack: Almonds + Protein Shake",
    "Lunch: Rice + Chicken + Vegetables + Whey Protein",
    "Snack: Peanut Butter Sandwich + Fruits",
    "Dinner: Fish/Chicken + Quinoa + Salad",
    "Pre-Bed: Casein Protein + Milk"
]

print(f"\n🍽️ Daily Muscle Gain Diet (Calories: {int(calories)} kcal):")
for meal in diet_plan:
    print(f"- {meal}")

print("\n💪 AI Tip: Track your weights, gradually increase sets/reps weekly, stay hydrated!")
