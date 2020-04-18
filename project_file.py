## This is the project file that I used as the whole project
## any update will be update here

## let's say our project is a basic class 

## we want to simulate the things a boy do in one day
## 1. get up in the morning
## 2. 


# timeline

# create project --> (*) add get up function -->
class myprojectclass():
    name = 'git_practice_project'
    def __init__(self,):
        self.branch = 'master'
        self.stage = 'dev'
        self.version = 1.0
    
    def do_something(self):
        self.get_up()
        pass

    
    def get_up(self):
        print('get up in the morning')
    
    def wash_hand(self):
        self.runing_water()
        self.apply_sop()
        self.scrub_hand()
        self.rinse_hand()


### sub-functions in wash_hand
    def runing_water(self):
        print('open tap, let water runing to both your hands.')
        print('make sure hands have been full wet and close the tap.')

    def apply_sop(self):
        print('Lather your hands by rubbing them together with the soap.')

    def scrub_had(self):
        print('rub your hands for at least 20 seconds.')
    
    def rinse_hand(self):
        print('nse your hands well under clean, running water.')
## 
