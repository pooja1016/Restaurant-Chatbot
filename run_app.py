from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput
#import warnings
#warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-460835757204-460401092161-460402251201-da5ab3a2f0fab116857eb0056db78628', #app verification token
							'xoxb-460835757204-460910699603-B2L4J2o2rPAya14KOsHuMaxE', # bot verification token
							'LKvebexvqitRg9wu97LFhW7y', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))