import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB
  
        1. Check to see if fact is of Type:Fact

        2. Check to see if fact is in KB
        """


        print("Asserting {!r}".format(fact))
        
        is_fact = True    

        if fact.name != "fact":
            is_fact = False

        if is_fact == True:
            for i in self.facts:
                if (i == fact):
                    return
            self.facts.append(fact)

        
        """
        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """

        print("Asking {!r}".format(fact))

        output = ListOfBindings()
        binds = None

        """check to see foreach item in facts: new_fact = self.fact[i]"""
        """if there exists fact, there is a binding, add to list of bindings""" 
        for i in self.facts:
            status = match(i.statement, fact.statement)
            if (status != False):
                binds = status
                """add_bindings in logical_classes for ListOfBindings"""
                output.add_bindings(binds, fact)

        """len defined in logical_classes.py"""
        if len(output) == 0:
            return False
        
        return output

