from neo4j import GraphDatabase
import sys

class HelloWorldExample(object):
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        print("CLOSING...")
        self._driver.close()
        

    def print_greeting(self, message):
        with self._driver.session() as session:
            greeting = session.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
            print(greeting.single()[0])

obj = HelloWorldExample("bolt://localhost:7687", "neo4j", "neo4jadmin")
obj.print_greeting("Ola Meu!!!")