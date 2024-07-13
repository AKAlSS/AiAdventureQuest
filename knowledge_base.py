# knowledge_base.py
class KnowledgeBase:
    def __init__(self):
        self.topics = {
            "AI Agents": self.get_ai_agents_info(),
            "AI Frameworks": self.get_ai_frameworks_info(),
            "Agentic Workflows": self.get_agentic_workflows_info(),
            "Agentic Automation": self.get_agentic_automation_info(),
            "AI Concepts": self.get_ai_concepts_info(),
        }

    def get_ai_agents_info(self):
        return [
            "AI agents are autonomous entities which observe through sensors and act upon an environment using actuators and direct their activity towards achieving goals.",
            "Examples of AI agents include chatbots, recommendation systems, and autonomous vehicles."
        ]

    def get_ai_frameworks_info(self):
        return [
            "TensorFlow: An end-to-end open-source platform for machine learning.",
            "PyTorch: An open-source machine learning library based on the Torch library.",
            "Scikit-learn: A machine learning library for Python that features various classification, regression, and clustering algorithms."
        ]

    def get_agentic_workflows_info(self):
        return [
            "Agentic workflows involve the steps and processes that AI agents follow to achieve their objectives.",
            "These workflows typically include data collection, data processing, decision making, and action execution."
        ]

    def get_agentic_automation_info(self):
        return [
            "Agentic automation refers to the use of AI agents to automate tasks and processes without human intervention.",
            "Examples include robotic process automation (RPA) and automated customer service agents."
        ]

    def get_ai_concepts_info(self):
        return [
            "Machine Learning: A subset of AI focused on building systems that learn from data.",
            "Deep Learning: A subset of machine learning involving neural networks with many layers.",
            "Natural Language Processing (NLP): A field of AI that gives machines the ability to read, understand, and derive meaning from human languages."
        ]

    def get_topic_info(self, topic):
        return self.topics.get(topic, "Topic not found.")
