#!/usr/bin/python2
# -*- coding: utf8 -*-
import aiml
import os
import config as cfg

class TalkBot(aiml.Kernel):
    def __init__(self,properties=cfg.BOT_PROPERTIES):
        aiml.Kernel.__init__(self)
        self.verbose(cfg.DEBUG)
        if os.path.isfile("aliceTalkbot.brn"):
            self.bootstrap(brainFile = "aliceTalkbot.brn")
        else:
            self.init_bot()
            self.saveBrain("aliceTalkbot.brn")
        for p in properties:
            self.setBotPredicate( p, properties[p] )
    
    def init_bot(self):
        for file in os.listdir(cfg.AIML_SET):
            if file[-4::]=="aiml":
                self.learn(os.path.join(cfg.AIML_SET,file) )

