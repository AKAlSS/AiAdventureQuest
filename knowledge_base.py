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
            "### AI Agents\n\n"
            "#### Introduction\n\n"
            "AI agents are autonomous entities which observe through sensors and act upon an environment using actuators "
            "and direct their activity towards achieving goals. They can operate without human intervention and can adapt "
            "to changing environments. Examples of AI agents include chatbots, recommendation systems, and autonomous vehicles.\n\n"
            "#### Key Characteristics\n\n"
            "1. **Autonomy**: Ability to operate without human intervention.\n"
            "2. **Social Ability**: Ability to interact with other agents and humans.\n"
            "3. **Reactivity**: Ability to perceive and respond to changes in the environment.\n"
            "4. **Proactiveness**: Ability to take initiative and exhibit goal-directed behavior.\n\n"
            "#### Types of AI Agents\n\n"
            "1. **Reactive Agents**: Simple agents that respond to specific stimuli.\n"
            "2. **Deliberative Agents**: Agents that use complex reasoning and planning.\n"
            "3. **Hybrid Agents**: Combine reactive and deliberative capabilities.\n\n"
            "#### Applications\n\n"
            "- **Chatbots**: Provide customer service and support.\n"
            "- **Recommendation Systems**: Suggest products or content to users.\n"
            "- **Autonomous Vehicles**: Navigate and drive without human input.\n"
            "#### Conclusion\n\n"
            "AI agents are a cornerstone of modern AI applications, enabling autonomous and intelligent behavior in a wide "
            "range of environments."
        ]

    def get_ai_frameworks_info(self):
        return [
            "### AI Frameworks\n\n"
            "#### Introduction\n\n"
            "AI frameworks are software libraries and tools that provide the building blocks for developing AI models. They "
            "simplify the implementation of complex AI algorithms and models, allowing researchers and developers to focus on "
            "designing and refining their models rather than on low-level details.\n\n"
            "#### Popular AI Frameworks\n\n"
            "1. **TensorFlow**: An end-to-end open-source platform for machine learning, developed by Google. It offers a "
            "comprehensive ecosystem for building and deploying ML models.\n"
            "2. **PyTorch**: An open-source machine learning library developed by Facebook. It is known for its flexibility "
            "and ease of use, particularly in research settings.\n"
            "3. **Scikit-learn**: A machine learning library for Python that features various classification, regression, "
            "and clustering algorithms. It is built on top of NumPy, SciPy, and Matplotlib.\n"
            "4. **Keras**: A high-level neural networks API, written in Python and capable of running on top of TensorFlow, "
            "CNTK, or Theano. It is designed to enable fast experimentation with deep neural networks.\n\n"
            "#### Features of AI Frameworks\n\n"
            "1. **Model Building**: Tools for defining and training machine learning models.\n"
            "2. **Data Handling**: Utilities for processing and managing datasets.\n"
            "3. **Visualization**: Capabilities for visualizing model performance and data.\n"
            "4. **Deployment**: Support for deploying models in various environments, from mobile devices to cloud services.\n\n"
            "#### Conclusion\n\n"
            "AI frameworks are essential tools for AI development, providing the infrastructure and support needed to build "
            "sophisticated AI models efficiently and effectively."
        ]

    def get_agentic_workflows_info(self):
        return [
            "### Agentic Workflows\n\n"
            "#### Introduction\n\n"
            "Agentic workflows involve the steps and processes that AI agents follow to achieve their objectives. These workflows "
            "typically include data collection, data processing, decision making, and action execution.\n\n"
            "#### Common Stages in Agentic Workflows\n\n"
            "1. **Perception**: Collecting data from the environment through sensors or other means.\n"
            "2. **Reasoning**: Analyzing and processing the data to make informed decisions.\n"
            "3. **Learning**: Improving performance over time by learning from past experiences.\n"
            "4. **Action**: Executing decisions and taking actions based on reasoning and learning.\n\n"
            "#### Example Workflow\n\n"
            "A recommendation system collects user data, processes it to understand preferences, learns from interactions, "
            "and provides personalized recommendations.\n\n"
            "#### Conclusion\n\n"
            "Agentic workflows are crucial for the functionality of AI agents, enabling them to perform tasks autonomously and "
            "efficiently."
        ]

    def get_agentic_automation_info(self):
        return [
            "### Agentic Automation\n\n"
            "#### Introduction\n\n"
            "Agentic automation refers to the use of AI agents to automate tasks and processes without human intervention. It "
            "is widely used in various industries to improve efficiency, reduce errors, and handle complex tasks.\n\n"
            "#### Applications of Agentic Automation\n\n"
            "- **Robotic Process Automation (RPA)**: Automates repetitive tasks in business processes.\n"
            "- **Automated Customer Service Agents**: Handle customer inquiries and support tasks.\n"
            "- **Supply Chain Management**: Optimizes logistics and inventory management.\n\n"
            "#### Benefits of Agentic Automation\n\n"
            "1. **Increased Efficiency**: Automates time-consuming tasks, freeing up human resources.\n"
            "2. **Reduced Errors**: Minimizes human errors by following predefined rules and logic.\n"
            "3. **Cost Savings**: Reduces operational costs by automating tasks.\n"
            "4. **Scalability**: Easily scales to handle increased workloads without additional human resources.\n\n"
            "#### Challenges in Agentic Automation\n\n"
            "1. **Reliability**: Ensuring the AI agents perform tasks correctly and consistently.\n"
            "2. **Integration**: Integrating AI agents with existing systems and processes.\n"
            "3. **Handling Unexpected Situations**: Designing agents to deal with unforeseen circumstances.\n\n"
            "#### Conclusion\n\n"
            "Agentic automation is transforming industries by automating complex tasks and processes, leading to significant "
            "improvements in efficiency and productivity."
        ]

    def get_ai_concepts_info(self):
        return [
            "### AI Concepts\n\n"
            "#### Introduction\n\n"
            "Understanding the fundamental concepts of AI is essential for grasping how AI systems work. This section covers "
            "key concepts such as machine learning, deep learning, natural language processing (NLP), and reinforcement learning.\n\n"
            "#### Machine Learning\n\n"
            "Machine learning is a subset of AI focused on building systems that learn from data. It involves training models "
            "on datasets to make predictions or decisions without being explicitly programmed.\n\n"
            "1. **Supervised Learning**: Learning from labeled data, where the model is trained on input-output pairs.\n"
            "2. **Unsupervised Learning**: Learning from unlabeled data, where the model tries to find patterns or clusters.\n"
            "3. **Semi-supervised Learning**: A combination of supervised and unsupervised learning.\n\n"
            "#### Deep Learning\n\n"
            "Deep learning is a subset of machine learning that involves neural networks with many layers. It excels in "
            "tasks such as image and speech recognition, where it can automatically learn hierarchical representations of data.\n\n"
            "#### Natural Language Processing (NLP)\n\n"
            "NLP is a field of AI that gives machines the ability to read, understand, and derive meaning from human languages. "
            "It is used in applications like chatbots, language translation, and sentiment analysis.\n\n"
            "#### Reinforcement Learning\n\n"
            "Reinforcement learning is a type of machine learning where agents learn by interacting with their environment and "
            "receiving rewards or penalties. It is used in applications like game playing, robotics, and autonomous driving.\n\n"
            "#### Conclusion\n\n"
            "AI concepts form the foundation of modern AI systems, enabling the development of intelligent applications that "
            "can learn, adapt, and perform complex tasks."
        ]

    def get_topic_info(self, topic):
        return self.topics.get(topic, "Topic not found.")
