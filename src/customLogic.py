from typing import List
from abc import ABC
from src.EmotionMap import EmotionMap

class Statement(ABC):
    '''
    A base class for all statements used.
    '''
    def __init__(self, statement: str, agent_map: EmotionMap):
        self.statement = statement
        self.agent_map = agent_map

    def __hash__(self):
        return hash(self.statement)

class AtomicStatement(Statement):
    def __init__(self, statement: str, agent_map: EmotionMap):
        '''
        A class representing an atomic statement.
        '''
        super().__init__(statement, agent_map)

    def statement(self):
        return self.statement

    def __eq__(self, statement: 'AtomicStatement'):
        return self.statement == statement.statement

    def __hash__(self):
        return hash(self.statement)

class ConditionalStatement(Statement):
    def __init__(self, statement: str, agent_map: EmotionMap, conditions: List[Statement]):
        '''
        A class representing a statement that would be true
        if other statements are present.
        '''
        super().__init__(statement, agent_map)
        self.conditions = conditions

    def evaluate(self, conditions):
        present = 0
        for statement in self.conditions:
            if hash(statement) == hash(self):
                continue
            else:
                if type(statement) is AtomicStatement:
                    if statement in conditions:
                        present += 1
                else:
                    if statement.evaluate(conditions):
                        present += 1
            
        return present == len(self.conditions)

    def __hash__(self):
        return hash(self.statement + str(self.conditions))
            


class StatementList:
    
    def __init__(self):
        self.statements = []

    def add(self, statement: Statement):
        if not issubclass(type(statement), Statement):
            raise ValueError("adding a non-Statement")
        self.statements.append(statement)

    def remove(self, statement):
        self.statements.remove(statement)

    def query(self, statement_query: str):
        '''
        Queries if a statement is true.

        Returns numbers to consider for repeated atomic statements.

        0 means that the queried statement is not present. If higher then the statement is present.
        '''
        count = 0
        for statement in self.statements:
            if statement.statement == statement_query:
                if type(statement) is AtomicStatement:
                    count += 1
                
                elif type(statement) is ConditionalStatement:
                    if statement.evaluate(self.statements):
                        count += 1
                
        return count

    def __iter__(self):
        return iter(self.statements)
                
##a = AtomicStatement("a")
##l = StatementList()
##l.add(a)
##b = AtomicStatement("b")
##c = ConditionalStatement("c", [AtomicStatement("a"), AtomicStatement("b")])
##l.add(c)
