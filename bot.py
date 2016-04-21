import time, json, yaml, sys
from slackclient import SlackClient

YAML_FILE="slack.yaml"
STDOUT_LOG="/tmp/modelout.txt"
STDERR_LOG="/tmp/modelerr.txt"
MAXIMUM_WAITING_PERIOD=900 
#waiting period is in seconds
TIMEOUT_MESSAGE="This bot will now stop. There will be no more questions."
user_arr=["anna","bob","carol channing","dave"]
room="your_slack_room"
USERS=user_arr
ROOM=room

opener="Let's begin our "+ROOM.title()+" standup. Press any key to begin."
question_1="What did you do yesterday or the previous work day?"
question_2="What will you do today?"
question_3="Do you have any blockers?"
closer="Thank you for your time. No further response from you is needed."
QUESTION_ARRAY=[opener,question_1,question_2,question_3,closer]
question_1_summary="*Previously:* "
question_2_summary="*Today:* "
question_3_summary="*Blockers:* "
TITLE_ARRAY=[opener,question_1_summary,question_2_summary,question_3_summary,closer]
PROMPT_REMINDER="Please respond and answer the question above."

sys.stdout = open(STDOUT_LOG,"w")
sys.stderr = open(STDERR_LOG,"w")

class Bot(object):

  def __init__(self,slackclient,room,users,question_list,summarized_question_list):
    self.client=slackclient
    self.users=users
    self.questions=question_list
    self.room=room
    self.user_response={}
    self.summarized_questions=summarized_question_list
    self.user_id={}
    self.dm_id={}

  def speak(self,speak_channel,statement):
    self.client.api_call("chat.postMessage", as_user="true", channel=speak_channel, text=statement)

  def get_text(self,speak_channel):
    user_text=self.client.api_call("im.history", channel=speak_channel)
    return user_text

  def asker(self,ask_user):
    question_list=self.questions
    xchannel=self.dm_id[ask_user]
    xuser=self.user_id[ask_user]
    list_length=len(question_list)-1
    question_count=0
    self.speak(xchannel, question_list[question_count])
    question_count=question_count+1
    time_sleep=0
    wait_max=MAXIMUM_WAITING_PERIOD
    prompt_reminder=wait_max*2/3
    while (question_count<=list_length) and (time_sleep < wait_max):
      jsoner = self.get_text(xchannel)
      text=json.loads(jsoner)

      message_latest= text["messages"][0]
      muser= message_latest["user"]
      mtext= message_latest["text"]
      if time_sleep==prompt_reminder:
        question_current=PROMPT_REMINDER
        self.speak(xchannel,question_current)
      if mtext=="ignore":
        return False
      if muser==xuser:
        question_current=question_list[question_count]
        if time_sleep>=wait_max:
          question_current=TIMEOUT_MESSAGE
        else:
          time_sleep=0
        self.speak(xchannel,question_current)
        question_count=question_count+1 
      time.sleep(5)
      time_sleep+=5
    if (time_sleep >= wait_max):
      return False
    else:
      return True

  def fetch(self,user):
    qlist=self.questions
    qa_list=self.summarized_questions
    xchannel=self.dm_id[user]
    xuser=self.user_id[user]
    qa_list = qa_list[::-1]
    jsoner= self.get_text(xchannel)
    raw_text=json.loads(jsoner)
    start_index=0
    message_latest= raw_text["messages"][start_index]
    mtext= message_latest["text"]
    muser= message_latest["user"]
    str_name= "> "+name.title()
    said_something=self.user_response[user]
    if not said_something:
      chronological_order_answer_list=[str_name,"Timeout. No answers."]
      return chronological_order_answer_list
    answers_list=[]
    cnt=0
    while raw_text["messages"][start_index]["text"] != qlist[1]:
      start_index+=1
      if raw_text["messages"][start_index]["user"]==xuser:
        uline=raw_text["messages"][start_index]["text"]
        uencode=uline.encode('utf-8')
        answer_line=qa_list[cnt+1].rstrip()+' '+uencode
        answers_list.append(answer_line)
        cnt=cnt+1
    answers_list.append(str_name)
    return answers_list[::-1]

with open(YAML_FILE, 'r') as f:
  doc = yaml.load(f)

token = doc["token"]
sc = SlackClient(token)

user_arr=USERS
room=ROOM

question_list=QUESTION_ARRAY
question_title=TITLE_ARRAY

robot=Bot(sc,room,user_arr,question_list,question_title)

dm_id={}
user_id={}

for person in robot.users:
  robot.user_id[person]=doc["user"][person]
  robot.dm_id[person]=doc["dm"][person]

robot.room=doc["channel"][room]

for user in robot.users:
  robot.user_response[user]=robot.asker(user)
  #comment out the line above and uncomment the line below if you want to fetch answers without asking
  #robot.user_response[user]=True

merged_answers=[]

for name in robot.users:
  result=robot.fetch(name)
  merged_answers+=result

final_text=""
for line in merged_answers:
  final_text+=line.decode('utf-8','ignore')+"\n"

robot.speak(robot.room,final_text)

