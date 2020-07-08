#!/usr/bin/env python


class SocialMediaUser:
    def __init__(self,  name):
        self.name = name
        self.upvotes = 0

    def recieve_upvote(self):
        self.upvote += 1

