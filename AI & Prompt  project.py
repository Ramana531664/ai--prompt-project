import random

# Define the story branches with evolving prompts
story_branches = {
    "start": {
        "prompt": "You wake up in a mysterious room with two doors. One is red, and the other is blue.",
        "choices": {
            "red": "You enter the red door and find a dark hallway with faint whispers.",
            "blue": "You open the blue door and discover a magical library with floating books."
        }
    },
    "red": {
        "prompt": "The whispers grow louder. You see a shadow moving in the darkness.",
        "choices": {
            "approach": "You approach the shadow, and it reveals a hidden passage.",
            "run": "You run back to the starting room, feeling safer but more anxious."
        }
    },
    "blue": {
        "prompt": "The floating books start circling you, glowing with ancient symbols.",
        "choices": {
            "touch": "You touch a glowing book, and visions of distant worlds flood your mind.",
            "ignore": "You ignore the books and explore the library for clues."
        }
    },
    "approach": {
        "prompt": "The hidden passage leads to a secret chamber filled with treasures.",
        "choices": {
            "take": "You take a mysterious gem, and the room begins to collapse!",
            "leave": "You decide to leave the gem and escape just in time."
        }
    },
    "run": {
        "prompt": "You stumble back into the room, but the red door has vanished!",
        "choices": {
            "search": "You search the room and find a hidden key under the rug.",
            "wait": "You wait, hoping someone will come to help."
        }
    },
    "touch": {
        "prompt": "The book transports you to a new dimension where you are the hero of an epic quest.",
        "choices": {
            "accept": "You accept your fate and begin your quest as the chosen one.",
            "decline": "You refuse and are transported back to the library, confused but safe."
        }
    },
    "ignore": {
        "prompt": "You find a hidden door behind the bookshelf, slightly ajar.",
        "choices": {
            "open": "You open the door and discover a secret underground lab.",
            "leave": "You leave the library, feeling like you missed something important."
        }
    },
    "take": {
        "prompt": "You clutch the mysterious gem tightly. Suddenly, the ground shakes violently!",
        "choices": {
            "escape": "You run towards the exit, dodging falling debris.",
            "stay": "You stay to examine the gem, hoping to understand its power."
        }
    },
    "leave": {
        "prompt": "You escape just in time, leaving the treasure behind. The room collapses behind you.",
        "choices": {
            "exit": "You walk away from the ruins, feeling a mix of relief and regret.",
            "explore": "You decide to explore the area outside the ruins for more secrets."
        }
    },
    "escape": {
        "prompt": "You sprint towards the exit, barely making it out alive with the gem in hand.",
        "choices": {
            "celebrate": "You celebrate your survival and the treasure you've found.",
            "regret": "You wonder if you missed out on something greater inside."
        }
    },
    "stay": {
        "prompt": "As you examine the gem, it begins to glow intensely, and you feel a surge of energy.",
        "choices": {
            "embrace": "You embrace the energy, feeling powerful and invincible.",
            "resist": "You resist the energy, fearing its unknown consequences."
        }
    },
    "search": {
        "prompt": "You search the room and find a hidden key under the rug.",
        "choices": {
            "use_key": "You use the key to open a locked chest, finding mysterious artifacts inside.",
            "ignore_key": "You ignore the key, feeling uneasy about its purpose."
        }
    },
    "wait": {
        "prompt": "You wait patiently, but no one arrives. The room grows colder.",
        "choices": {
            "explore": "You decide to explore the room further, looking for clues.",
            "give_up": "You give up and sit in silence, waiting for something to happen."
        }
    },
    "exit": {
        "prompt": "You walk away from the ruins, feeling a mix of relief and regret.",
        "choices": {
            "reflect": "You reflect on your journey and the choices you made.",
            "move_on": "You decide to move on, leaving the past behind."
        }
    },
    "explore": {
        "prompt": "You explore the area outside the ruins for more secrets.",
        "choices": {
            "discover": "You discover an ancient map leading to hidden treasures.",
            "return": "You decide to return to the ruins, feeling like you missed something important."
        }
    },
    "use_key": {
        "prompt": "You use the key to open a locked chest, finding mysterious artifacts inside.",
        "choices": {
            "take_artifacts": "You take the artifacts, feeling their magical power.",
            "leave_artifacts": "You leave the artifacts, unsure of their true nature."
        }
    },
    "ignore_key": {
        "prompt": "You ignore the key, feeling uneasy about its purpose.",
        "choices": {
            "wait": "You wait, hoping someone will come to help.",
            "search_again": "You search the room again, feeling there's more to discover."
        }
    },
    "take_artifacts": {
        "prompt": "You take the artifacts, feeling their magical power.",
        "choices": {
            "use_power": "You decide to use the artifacts' power to alter reality.",
            "keep_safe": "You keep the artifacts safe, unsure of their true potential."
        }
    },
    "leave_artifacts": {
        "prompt": "You leave the artifacts, unsure of their true nature.",
        "choices": {
            "leave": "You leave the room, feeling a mix of relief and regret.",
            "explore": "You decide to explore more, feeling there's more to uncover."
        }
    },
    "use_power": {
        "prompt": "You unleash the artifacts' power, altering reality itself!",
        "choices": {
            "control": "You try to control the new reality, shaping it to your will.",
            "surrender": "You surrender to the power, becoming part of the altered world forever."
        }
    },
    "surrender": {
        "prompt": "You surrender to the power, becoming part of the altered world forever.",
        "choices": {
            "eternal_peace": "You find eternal peace in this new reality.",
            "eternal_trap": "You realize too late that you are trapped forever."
        }
    },
    "eternal_peace": {
        "prompt": "You find eternal peace in this new reality.",
        "choices": {
            "reflect": "You reflect on your journey and accept your fate.",
            "move_on": "You move on, finding a new purpose in this peaceful existence."
        }
    },
    "eternal_trap": {
        "prompt": "You realize too late that you are trapped forever.",
        "choices": {
            "escape": "You desperately try to escape, but it's too late.",
            "accept": "You accept your fate, knowing you'll never escape."
        }
    },
    # ✅ Game over node
    "game_over": {
        "prompt": "Congratulations! You've reached the end of the adventure!",
        "choices": {
            "celebrate": "Celebrate your journey and choices!",
        }
    }
}

def play_game(current_node):
    # Check if the current node exists to prevent KeyError
    if current_node not in story_branches:
        print("\nThe path you've chosen doesn't exist. Game over!")
        return

    story = story_branches[current_node]
    print(f"\n{story['prompt']}")
    
    for choice in story['choices']:
        print(f"- {choice.capitalize()}")

    user_choice = input("\nWhat will you do? (choose one): ").lower()

    if user_choice in story['choices']:
        next_node = user_choice
        # Check if it's an ending node
        if next_node == "game_over" or next_node not in story_branches:
            print("\n🎉 Congratulations! You've reached your goal!")
            return
        play_game(next_node)
    else:
        print("Invalid choice. Please try again.")
        play_game(current_node)

# Start the game
print("Welcome to the Interactive Adventure Game!")
play_game("start")
