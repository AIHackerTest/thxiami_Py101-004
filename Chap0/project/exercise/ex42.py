from sys import exit
from random import randint


class Game(object):
    def __init__(self, start):
        self.quips = [
            'You died.You kinda suck at this.',
            'Your mom would be proud. if she were smarter.',
            'Such a loser.',
            "I have a small puppy that's better at this."
        ]
        self.start = start

    def play(self):
        next = self.start

        while True:
            print('\n-----------------')
            room = getattr(self, next)
            next = room()

    def death(self):
        print(self.quips[randint(0, len(self.quips) - 1)])
        exit(1)

    def princess_lives_here(self):
        print("You see a beautiful Princess with a shiny crown.")
        print("She offers you some cake.")

        eat_it = input("> ")

        if eat_it == "eat it":
            print("You explode like a pinata full of frogs.")
            print("The Princess cackles and eats the frogs. Yum!")
            return 'death'
        elif eat_it == "do not eat it":
            print("She throws the cake at you and it cuts off your head.")
            print("The last thing you see is her munching on your torso. Yum!")
            return 'death'

        elif eat_it == "make her eat it":
            print("""
            The Princess screams as you cram the cake in her mouth.\n
            Then she smiles and cries and thanks you for saving her.\n
            She points to a tiny door and says, 'The Koi needs cake too.'\n
            She gives you the very last bit of cake and shoves you in.
            """)
            return 'gold_koi_pond'

        else:
            print("The princess looks at you confused and just points at the cake.")
            return 'princess_lives_here'

    def gold_koi_pond(self):
        print(
            """
            There is a garden with a koi pond in the center.\n
            You walk close and see a massive fin poke out.\n
            You peek in and a creepy looking huge Koi stares at you.\n
            It opens its mouth waiting for food.
            """)

        feed_it = input("> ")

        if feed_it == "feed it":
            print("""
            The Koi jumps up, and rather than eating the cake, eats your arm.\n
            You fall in and the Koi shrugs than eats you.\n
            You are then pooped out sometime later.
            """)
            return 'death'

        elif feed_it == "do not feed it":
            print("""
            The Koi grimaces, then thrashes around for a second.\n
            It rushes to the other end of the pond,braces against the wall...\n
            then it *lunges* out of the water, up in the air and over your
            entire body, cake and all.\n
            You are then pooped out a week later.
            """)
            return 'death'

        elif feed_it == "throw it in":
            print("""
            The Koi wiggles, then leaps into the air to eat the cake.
            You can see it's happy, it then grunts,thrashes...
            and finally rolls over and poops a magic diamond into the air at your feet.
            """)
            return 'bear_with_sword'

        else:
            print("The Koi gets annoyed and wiggles a bit.")
            return 'gold_koi_pond'


    def bear_with_sword(self):
        print("""
        Puzzled, you are about to pick up the fish poop diamond
        when a bear bearing a load bearing sword walk in.\n
        Hey! That' my diamond! Where'd you get that!?\n
        It holds its paw out and looks at you.
        """)

        give_it = input("> ")

        if give_it == "give it":
            print("""
                The bear swipes at your hand to grab the diamond and
                rips your hand off in the process. It then looks at
                your bloody stump and says, Oh crap, sorry about that.\n
                It tries to put your hand back on, but you collapse.\n
                The last thing you see is the bear shrug and eat you.
            """)
            return 'death'

        elif give_it == "say no":
            print("""
            The bear looks shocked.  Nobody ever told a bear with a broadsword 'no'.\n
            It asks, Is it because it's not a katana? I could go get one!\n
            It then runs off and now you notice a big iron gate.\n
            Where the hell did that come from?  You say.
            """)
            return 'big_iron_gate'

    def big_iron_gate(self):
        print("You walk up to the big iron gate and see there's a handle.")

        open_it = input("> ")

        if open_it == 'open it':
            print("""
                You open it and you are free!\n
                There are mountains.  And berries! And...\n
                Oh, but then the bear comes with his katana and stabs you.
                Who's laughing now!?\n
                Love this katana."'
            """)
            return 'death'

        else:
            print("That doesn't seem sensible.  I mean, the door 's right there.")
            return 'big_iron_gate'

a_game = Game('princess_lives_here')
a_game.play()
