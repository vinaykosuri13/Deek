# ==========================
# Deek Memory
# Version: 2.0
# ==========================

import json
import os


class Memory:

    FILE_NAME = "memory.json"

    def __init__(self):

        self.preferences = {}
        self.tasks = []
        self.notes = []

        self.load()

    # --------------------------
    # Load Memory
    # --------------------------

    def load(self):

        if not os.path.exists(self.FILE_NAME):
            return

        with open(self.FILE_NAME, "r") as file:

            data = json.load(file)

        self.preferences = data.get("preferences", {})
        self.tasks = data.get("tasks", [])
        self.notes = data.get("notes", [])

    # --------------------------
    # Save Memory
    # --------------------------

    def save(self):

        data = {
            "preferences": self.preferences,
            "tasks": self.tasks,
            "notes": self.notes
        }

        with open(self.FILE_NAME, "w") as file:

            json.dump(data, file, indent=4)

    # --------------------------
    # Preferences
    # --------------------------

    def remember(self, key, value):

        self.preferences[key] = value

        self.save()

    def recall(self, key):

        return self.preferences.get(key)

    # --------------------------
    # Tasks
    # --------------------------

    def add_task(self, task):

        self.tasks.append(task)

        self.save()

    def get_tasks(self):

        return self.tasks

    # --------------------------
    # Notes
    # --------------------------

    def add_note(self, note):

        self.notes.append(note)

        self.save()

    def get_notes(self):

        return self.notes
