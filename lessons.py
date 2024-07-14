from knowledge_base import KnowledgeBase

class Lesson:
    def __init__(self, topic, content):
        self.topic = topic
        self.content = content

class Lessons:
    def __init__(self):
        self.knowledge_base = KnowledgeBase()
        self.lessons = self.create_lessons()

    def create_lessons(self):
        lessons = []
        for topic, content in self.knowledge_base.topics.items():
            lessons.append(Lesson(topic, content))
        return lessons

    def get_lesson(self, topic):
        for lesson in self.lessons:
            if lesson.topic == topic:
                return lesson.content
        return "Lesson not found."
