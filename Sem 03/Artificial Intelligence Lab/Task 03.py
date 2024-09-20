#!/usr/bin/env python
# coding: utf-8
Model Base Reflex Agent
This agent has a model of its environment (the current temperature) and uses that model to make decisions about actions. This allows it to consider the context of the situation, rather than simply reacting to input
# In[190]:


class ModelBaseReflexAgent:
    def __init__(self,temp, prev_action):
        self.desired_temp = temp
        self.prev_action = None
        
    def preceiver(self, current_temp):
        self.current_temp = current_temp
    
    def actuator(self):
        if self.prev_action is None:
            self.prev_action = "Turn on heater" if current_temp < self.desired_temp else "Turn off heater"
        else:
            if self.prev_action == "Turn on heater" and current_temp >= self.desired_temp:
                self.prev_action = "Turn off heater"
            elif self.prev_action == "Turn off heater" and current_temp < self.desired_temp:
                self.prev_action = "Turn on heater"

        return self.prev_action
        
rooms = {"Living room" : 27,
         "Kitchen": 17,
         "Bedrom": 35,
         "Bathroom":24}


# In[189]:


agent = ModelBaseReflexAgent(25, None)


# In[191]:


for rooms, temp in rooms.items():
    agent.preceiver(temp)
    print(f"{rooms}:{temp}==>{agent.actuator()}")


# In[192]:


agent.preceiver(24)
agent.actuator()


# In[ ]:




