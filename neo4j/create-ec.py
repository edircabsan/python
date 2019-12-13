from neo4j import GraphDatabase

class ECManager(object):
    def __init__(self, uri, username, password):
        self._driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self._driver.close()
    
    def createEC(self, id, name):
        with self._driver.session as session:
            session.run("MERGE (ec:Merchant {id: $id})")

obj = ECManager("bolt://localhost:7687", "neo4j", "teste")
obj.createEC("1", "Padoca do Zé")
obj.createEC("2", "Bistrô da Ana")
obj.createEC("3", "Restaurante da Paula")
obj.createEC("4", "Boteco do João")
obj.createEC("5", "Lanchonete da Tia Maria")