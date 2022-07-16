from .category import Category
from .topic import Topic
from .document import Document


class Storage:

    def __init__(self):
        self.categories = list()
        self.topics = list()
        self.documents = list()

    def add_category(self, category: Category):
        if category in self.categories:
            return
        self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic in self.topics:
            return
        self.topics.append(topic)

    def add_document(self, document: Document):
        if document in self.documents:
            return
        self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.__find_by_id(self.categories, category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__find_by_id(self.topics, topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__find_by_id(self.documents, document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id: int):
        category = self.__find_by_id(self.categories, category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id: int):
        topic = self.__find_by_id(self.topics, topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id: int):
        document = self.__find_by_id(self.documents, document_id)
        self.documents.remove(document)

    def get_document(self, document_id: int):
        return self.__find_by_id(self.documents, document_id)

    def __repr__(self):

        return '\n'.join([repr(x) for x in self.documents])

    @staticmethod
    def __find_by_id(entities, entity_id):
        for entity in entities:
            if entity.id == entity_id:
                return entity
