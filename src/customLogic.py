from typing import List
from abc import ABC

class Statement(ABC):
    '''
    A base class for all statements used.
    '''
    def __init__(self, statement: str):
        self.statement = statement

class AtomicStatement(Statement):
    def __init__(self, statement: str):
        '''
        A class representing an atomic statement.
        '''
        super().__init__(statement)

    def statement(self):
        return self.statement

    def __eq__(self, statement: 'AtomicStatement'):
        return self.statement == statement.statement

    def __hash__(self):
        return hash(self.statement)

class ConditionalStatement(Statement):
    def __init__(self, statement: str, conditions: List[Statement]):
        '''
        A class representing a statement that would be true
        if other statements are present.
        '''
        super().__init__(statement)
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
            
        if present == len(self.conditions):
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.statement + str(self.conditions))
            


class StatementList:
    def __init__(self):
        self.statements = []

    def add(self, statement: Statement):
        if not issubclass(type(statement), Statement):
            raise ValueError("adding a non-Statement")
        self.statements.append(statement)

    def query(self, statement_query: str):
        for statement in self.statements:
            if statement.statement == statement_query:
                if type(statement) is AtomicStatement:
                    return True
                
                elif type(statement) is ConditionalStatement:
                    if statement.evaluate(self.statements):
                        return True
                
        return False
                
##a = AtomicStatement("a")
##l = StatementList()
##l.add(a)
##b = AtomicStatement("b")
##c = ConditionalStatement("c", [AtomicStatement("a"), AtomicStatement("b")])
##l.add(c)
