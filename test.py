import random
import json

jokesss = [
    {
        "joke": "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25! \ud83c\udf83\ud83c\udf84",
        "id": 1
    },
    {
        "joke": "Why did the developer go broke? Because he used up all his cache! \ud83d\udcb8",
        "id": 2
    },
    {
        "joke": "How do you comfort a JavaScript bug? You console it. \ud83d\ude02",
        "id": 3
    }
]

with open('data/jokes.json', 'r') as jsonfile:
    read = jsonfile.read()
    
jokesss.pop(3 -1 )
print(jokesss)
