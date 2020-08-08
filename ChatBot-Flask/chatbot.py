# importing the chatterbot and flask libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from flask import *

app = Flask(__name__)

# creating instance(object) for our ChatBot and naming our ChatBot as 'Tom'.
my_chatbot = ChatBot('Tom',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db_file.sqlite3',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'sorry, Iam donot understand what you are saying',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

# opening the traning data for our ChatBot from the file using open function
# and storing it in identifier named as 'training_data_for_mybot'.
training_data_for_mybot = open('training_data_for_mychatbot/Ques and Anes.txt').read().splitlines()

# training the ChatBot using our personal data from the file
trainer = ListTrainer(my_chatbot)
trainer.train(training_data_for_mybot)

# training the ChatBot with english corpus data
trainer = ChatterBotCorpusTrainer(my_chatbot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_request = request.args.get('msg')
    # get_response() returns the responses for the user_request
    return str(my_chatbot.get_response(user_request))

if __name__ == "__main__":
    app.run(debug = True)

    
