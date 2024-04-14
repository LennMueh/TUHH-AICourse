from monkey_banana.agents import RandomAgent, RuleBasedAgent, PlanningAgent
from monkey_banana.banana_environment import MonkeyBananaEnvironmentTask, MonkeyBananaAction
from monkey_banana.banana_environment import MonkeyBananaFOEnvironmentTask, MonkeyBananaPOEnvironmentTask
import numpy as np



def question1():
    environment = MonkeyBananaEnvironmentTask(7, 2, 10)
    environment.visualize()
    return environment
    return

def question2():
    environment = question1()
    for _ in range(5):
        environment.perform_action(MonkeyBananaAction.MOVE_BOX_RIGHT)
    environment.perform_action(MonkeyBananaAction.CLIMB)
    environment.perform_action(MonkeyBananaAction.GRAB)
    environment.visualize()
    return environment

def question10():
    goal_environment = question1()
    for _ in range(5):
        goal_environment.perform_action(MonkeyBananaAction.MOVE_BOX_RIGHT)
    goal_environment.perform_action(MonkeyBananaAction.CLIMB)
    goal_environment.perform_action(MonkeyBananaAction.GRAB)
    for _ in range(10):
        test_environment = question1()
        agent = RandomAgent()
        test_environment = agent.run(test_environment, 1000)
    return

def question11():
    environment = MonkeyBananaFOEnvironmentTask(7, 2, 10)
    agent = RuleBasedAgent()
    agent.run(environment, 10)
    return

def question12():
    # TODO: Question 12
    return

def question15():
    # TODO: Question 15
    return

def question16():
    # TODO: Question 16
    return

question11()