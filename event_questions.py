import random

def IQ_test():
  rc=0
  quiz = {
  "Quelle est la capital de la France?": "Paris",
  "Combien y a-t-il de départements en France?": "96",
  "Quelle est la langue officielle de la France?": "Le Français",
  "Quel est le plus grand fleuve de France?": "La Loire",
  "Quel est le plus haut sommet de la France?": "Mont Blanc",
  "Quel est le nom du président actuel de la France?": "Emmanuel Macron",
  "Quel est le nom de la devise nationale de la France?": "Liberté égalité fraternité",
  "Quel est le nom de la tour la plus célèbre de Paris?": "La Tour Eiffel",
  "Quel est le nom de la plus grande île de France?": "Corsica",
  "Combien y a-t-il de régions en France?": "13"
  }
  for i in range(1,4):
    print(f"Question {i}")
    question = random.choice(list(quiz.keys()))
    answer = quiz[question]

    print(question)
    response = input()
    if response.lower() == answer.lower():
      print("Correct!")
      rc+=1
    else:
      print("Incorrect. La réponse était: " + answer)
IQ_test()
