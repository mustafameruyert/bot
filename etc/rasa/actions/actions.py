from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
#from googlesearch import search




class ActionGetUserAge(Action):

     def name(self) -> Text:
            return "action_userage"

     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        age=tracker.get_slot("userage")
        
        if int(age)<30:
            dispatcher.utter_message("Вы так молоды!")
        elif int(age)>=30:  
            dispatcher.utter_message("Очень хороший возраст!")

           
        
class ActionGetUserBirthPlace(Action):

     def name(self) -> Text:
            return "action_birthplace"

     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        birthplace=tracker.get_slot("birthplace")
        west_kz=["Атырау","Актау","Актобе","Жанаозен","Уральск"]
        east_kz=["Усть-Каменогорск","Семей","Зайсан","Урджар"]
        north_kz=["Астана","Нур-Султан","Петропавл","Павлодар","Кокшетау"]
        south_kz=['Алматы','Кызылорда','Шымкент','Тараз']
        central_kz=["Караганда"]
        
        if birthplace in west_kz:
            dispatcher.utter_message("ОО вы из нефтяного края")
        elif birthplace in east_kz:
            dispatcher.utter_message("Мне очень нравиться Алакол!")
        elif birthplace in north_kz:
            dispatcher.utter_message("Красота Бурабая это нечто!")
        elif birthplace in south_kz:
            dispatcher.utter_message("Очень люблю южные города Казахстана!")
        elif birthplace in central_kz:
            dispatcher.utter_message("Наслышан о степях центрального Казахстане!")
        else:
            dispatcher.utter_message("К сожалению не знаю такой город.Расскажите о вашем городе?")

       

class ActionTellTale(Action):

     def name(self) -> Text:
            return "action_tale"

     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #query = "Русские сказки"
        #my_results_list = []
        #for i in search(query,tld = 'com',lang = 'ru',num = 5,start = 0,stop = 2,pause = 2.0):
        #    my_results_list.append(i)
        #for i in my_results_list[:3]:
        #    dispatcher.utter_message(i)
        dispatcher.utter_message("Hello World!")
        
        
    
class ActionFilmRecommendation(Action):

     def name(self) -> Text:
            return "action_film"

     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #filmgenre=tracker.get_slot("filmgenre")
        #query="Фильмы жанра "+filmgenre
        #my_results_list = []
        #for i in search(query,tld = 'com',lang = 'ru',num = 5,start = 0,stop = 5,pause = 2.0):
        #    my_results_list.append(i)
        #for i in my_results_list[:3]:
        #    dispatcher.utter_message(i)
        dispatcher.utter_message("Hello World!")
        
        
class ActionBookRecommendation(Action):

     def name(self) -> Text:
            return "action_book"

     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #bookgenre=tracker.get_slot("bookgenre")
        #query="Книги про "+bookgenre
        #my_results_list = []
        #for i in search(query,tld = 'com',lang = 'ru',num = 5,start = 0,stop = 2,pause = 2.0):
        #    my_results_list.append(i)
        #for i in my_results_list[:3]:
        #    dispatcher.utter_message(i)
        dispatcher.utter_message("Hello World!")
        
        
class ActionTranslate(Action):

     def name(self) -> Text:
            return "action_translate"

     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #text=tracker.latest_message.get('text')
        #translator = Translator()
            
        #tr_word=translator.translate(text, dest='en').text
       
        dispatcher.utter_message("translate.google.com")
        
       
class ActionFoodRecommandation(Action):

     def name(self) -> Text:
            return "action_cooking"

     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #query=tracker.get_slot("cooking")
        #my_results_list = []
        #for i in search(query,tld = 'com',lang = 'ru',num = 5,start = 0,stop = 2,pause = 2.0):
        #    my_results_list.append(i)
        #for i in my_results_list[:3]:
        #    dispatcher.utter_message(i)
        dispatcher.utter_message("Hello World!")
        
class ActionNotFound(Action):

     def name(self) -> Text:
            return "action_fallback"

     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #query=tracker.latest_message.get('text')
        #my_results_list = []
        #for i in search(query,tld = 'com',lang = 'ru',num = 5,start = 0,stop = 5,pause = 2.0):
        #    my_results_list.append(i)
        #for i in my_results_list[:3]:
        #    dispatcher.utter_message(i)
        dispatcher.utter_message("Hello World!")
                
class ActionUserLovelyFood(Action):

     def name(self) -> Text:
            return "action_userlovelyfood"

     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #text=tracker.get_slot("user_lovely_food")
        #query="Интересные факты про "+text
        #my_results_list = []
        #for i in search(query,tld = 'com', lang = 'ru',num = 5,start = 0,stop = 5,pause = 2.0):
        #    my_results_list.append(i)
        #for i in my_results_list[:3]:
        #    dispatcher.utter_message(i)
        dispatcher.utter_message("Hello World!")
        
        
class ActionUserLovelyFood(Action):

     def name(self) -> Text:
            return "action_userlovelysport"

     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #text=tracker.get_slot("user_lovely_food")
        #query="Интересные факты про "+text
        #my_results_list = []
        #for i in search(query,tld = 'com',lang = 'ru',num = 5,start = 0,stop = 5,pause = 2.0):
        #    my_results_list.append(i)
        #for i in my_results_list[:3]:
        #    dispatcher.utter_message(i)
        dispatcher.utter_message("Hello World!")
        
   
                
class ActionUserBirthDate(Action):

     def name(self) -> Text:
            return "action_userbirthdate"

     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            dispatcher.utter_message("Hello World!")
            
class ActionMusicRecommendation(Action):

    def name(self) -> Text:
            return "action_music"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #text=tracker.get_slot("musicgenre")
        #query="Музыка "+text
        #my_results_list = []
        #for i in search(query,tld = 'com',lang = 'ru',num = 5,start = 0,stop = 5,pause = 2.0):
        #    my_results_list.append(i)
        #for i in my_results_list[:3]:
        #    dispatcher.utter_message(i)
        dispatcher.utter_message("Hello World!")

                
class ActionGetUserName(Action):

    def name(self) -> Text:
        return "action_username"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #name=tracker.latest_message.get('text')
        #dispatcher.utter_message("Как ваши дела "+name+" ?")
        #return [SlotSet("username", name)]
        dispatcher.utter_message("Hello World!")
       