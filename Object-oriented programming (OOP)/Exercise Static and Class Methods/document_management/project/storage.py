from typing import List, Union

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        self.__edit_object(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.__edit_object(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        self.__edit_object(document_id, self.documents, new_file_name)

    def delete_category(self, category_id):
        self.__delete_object(category_id, self.categories)

    def delete_topic(self, topic_id):
        self.__delete_object(topic_id, self.topics)

    def delete_document(self, document_id):
        self.__delete_object(document_id, self.documents)

    def get_document(self, document_id):
        return self.__find_object(document_id, self.documents)

    def __repr__(self):
        return "\n".join([str(d) for d in self.documents])

    def __edit_object(self, object_id, collection, *args) -> None:
        current_object = self.__find_object(object_id, collection)
        if current_object:
            current_object.edit(*args)

    @staticmethod
    def __find_object(object_id, collection) -> Union[Category, Topic, Document]:
        return next((o for o in collection if o.id == object_id), None)

    def __delete_object(self, object_id, collection: list) -> None:
        current_object = self.__find_object(object_id, collection)
        if current_object:
            collection.remove(current_object)
