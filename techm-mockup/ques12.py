#create a function that takes a student name and their scores as argument. inside that function calculate total score of that student and print the message "Hi <name> your total score is <totalscore>. The number of score entered for a student might vary."
def calculate_score(name, *score):
    total_score=0
    for i in score:
        total_score +=i
    print("Hi",name, "your total score is",total_score)
    return
calculate_score("Toshu",67,78,89,90,95)
