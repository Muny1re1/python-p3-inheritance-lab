#!/usr/bin/env python

from user import User

class Student(User):
    
    def learn(self, string):
        self.knowledge = []
        self.string = string
        self.knowledge.append(self.string)

