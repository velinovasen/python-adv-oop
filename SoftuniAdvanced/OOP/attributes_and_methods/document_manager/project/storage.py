from project.topic import Topic
from project.category import Category
from project.document import Document


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        category_check = [x for x in self.categories if x.id == category.id]
        if not category_check:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        topic_check = [x for x in self.topics if topic.id == x.id]
        if not topic_check:
            self.topics.append(topic)

    def add_document(self, document: Document):
        document_check = [x for x in self.documents if document.id == x.id]
        if not document_check:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = [x for x in self.categories if category_id == x.id]
        if category:
            category = category[0]
            category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = [x for x in self.topics if topic_id == x.id]
        if topic:
            topic = topic[0]
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = [x for x in self.documents if document_id == x.id]
        if document:
            document = document[0]
            document.file_name = new_file_name

    def delete_category(self, category_id):
        category = [x for x in self.categories if x.id == category_id]
        if category:
            category = category[0]
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [x for x in self.topics if topic_id == x.id]
        if topic:
            topic = topic[0]
            self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [x for x in self.documents if document_id == x.id]
        if document:
            document = document[0]
            self.documents.remove(document)

    def get_document(self, document_id):
        document = [x for x in self.documents if document_id == x.id]
        if document:
            document = document[0]
            return document

    def __repr__(self):
        token = ""
        for l in self.documents:
            token += repr(l)
        return token
