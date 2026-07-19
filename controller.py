# ==========================
# Deek Controller
# Version: 4.0
# ==========================

from brain import DeekBrain
from memory import Memory
from intent import IntentEngine
from tools import ToolEngine


class DeekController:

    def __init__(self):

        self.brain = DeekBrain()
        self.memory = Memory()
        self.intent = IntentEngine()
        self.tools = ToolEngine()

    def process(self, question):

        q = question.strip()

        # --------------------------
        # PHONE ACTIONS
        # --------------------------

        if q.lower().startswith("call "):

            contact = q[5:].strip()

            return {
                 "type": "action",
                "action": "CALL",
                "contact": contact
            }

        if q.lower().startswith("whatsapp "):

            contact = q[9:].strip()

            return {
                "type": "action",
               "action": "WHATSAPP",
                "contact": contact
           }

        if q.lower().startswith("navigate "):

           destination = q[9:].strip()

           return {
                "type": "action",
                "action": "MAPS",
                "destination": destination
           }

        if q.lower().startswith("maps "):

            destination = q[5:].strip()

            return {
                 "type": "action",
                 "action": "MAPS",
                 "destination": destination
            }
        if q.lower().startswith("open "):

            site = q[5:].strip()

            return {
                 "type": "action",
                 "action": "OPEN",
                 "site": site
            }

        if q.lower().startswith("website "):

            site = q[8:].strip()

            return {
                 "type": "action",
                 "action": "OPEN",
                 "site": site
            }  
                if q.lower().startswith("app "):

            app = q[4:].strip()

            return {
                "type": "action",
                "action": "APP",
                "app": app
            }

        if q.lower().startswith("open app "):

            app = q[9:].strip()

            return {
                "type": "action",
                "action": "APP",
                "app": app
            }

        # --------------------------
        # INTENT ENGINE
        # --------------------------

        intent = self.intent.detect(question)

        # --------------------------
        # MEMORY SAVE
        # --------------------------

        if intent == "MEMORY_SAVE":

            text = question[12:]

            key, value = text.split(" is ", 1)

            key = key.strip()
            value = value.strip()

            self.memory.remember(key, value)

            return f"I'll remember your {key} is {value}, Boss."

        # --------------------------
        # MEMORY RECALL
        # --------------------------

        if intent == "MEMORY_RECALL":

            key = question[10:].strip().rstrip("?")

            value = self.memory.recall(key)

            if value:
                return f"Your {key} is {value}."

            return "I don't remember that yet, Boss."

        # --------------------------
        # TOOLS
        # --------------------------

        if intent in ["CALCULATOR", "DATE_TIME"]:

            result = self.tools.execute(intent, question)

            if result is not None:
                return result

        # --------------------------
        # AI CHAT
        # --------------------------

        return self.brain.ask(question)
