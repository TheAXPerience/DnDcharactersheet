# DnD Character Sheet

A standard character sheet for the Dungeon and Dragons tabletop game.
Will display all the necessary elements for a campaign but must manually be input by users.
Thus, it will have the same feel as filling out a physical sheet but on the computer.

September 2nd, 2020

Status: Draft

Author: Alvin Xu

## Overview
This will be a chance to learn how to craft a website using Django, with a focus on user input into a database.
This website is expected to be small-scale, so may lack security or database refinery.

### Goals
* Learn how to deal with forms
* Learn to manage a website with users
* Learn to manage a server using Django
* Learn to manage a database with Django (SQLite default, might branch out to others)

### Non-Goals
* Create something to fully run a D&D campaign
* Create something that makes character creation an ease for players

## Models

This section will describe the database models that will need to be created.

### User Data

The information present for the user will be very minimal, and just enough for the user to login and recover their account.
That means the following data will be present:

* Username [CharField]
* Password [CharField]
* Email Address [CharField] (for account recovery)

### Character Information

The information present for the character model will be based on the Dungeons and Dragon's character sheet
This means that the following data needs to be present:

* Character Name [CharField]
* Class [CharField]
* Level [IntegerField]
* Background [CharField]
* Race [CharField]
* Alignment [CharField]
* Experience (?) [IntegerField]
* Proficiency Bonus [IntegerField]
* Strength [IntegerField]
* Dexterity [IntegerField]
* Constitution [IntegerField]
* Intelligence [IntegerField]
* Wisdom [IntegerField]
* Charisma [IntegerField]
* Saving Throws (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma) [IntegerField x6]
* Skills (Acrobatics, Animal Handling, Arcana, Athletics, Deception, History, Insight, Intimidation, Investigation, Medicine, Nature, Perception, Performance, Persuasion, Religion, Sleight of Hand, Stealth, Survival + is proficiency for each) [IntegerField, BooleanField x18]
* Armor Class [IntegerField]
* Initiative [IntegerField]
* Speed [IntegerField]
* Maximum HP [IntegerField]
* Current HP [IntegerField]
* Temporary HP [IntegerField]
* Death Saves (0-3 success, 0-3 failure) [IntegerField]
* Hit Dice [CharField] (not sure what this is supposed to be)
* Attacks & Spellcasting (name, attack bonus, damage/type) [List of CharField, IntegerField, CharField]
* Equipment [TextField]
* Money (CP, SP, EP, GP, PP) [FloatField x5]
* Passive Wisdom (Perception) [IntegerField]
* Proficiencies and Languages [TextField]
* Personality Traits [TextField]
* Ideals [TextField]
* Bonds [TextField]
* Flaws [TextField]
* Features and Traits [TextField]
* Age [CharField]
* Height [CharField]
* Weight [CharField]
* Eye Color [CharField]
* Skin Color [CharField]
* Hair Color [CharField]
* Character Appearance [TextField]
* Character Backstory [TextField]
* Allies and Organizations [TextField]
* Treasure [TextField]
* Spellcasting Ability [CharField]
* Spell Save DC [CharField]
* Spell Attack Bonus [CharField]
* Levels 0-9 Spell Slots (total + expended) [IntegerField x20]
* Spells (name, level, prepared?) [CharField, IntegerField, BooleanField x?]

Due to the sheer amount of information, some of it may not be present during earlier builds, and might not be present at all in the final build.

Notice that some of these are lists of things rather than singular objects themselves.
We can break down the model even more with the following:

#### Character
We will remove information that relate to the character involving a large amount of text pertaining to background and story, rather than character essentials.

Includes:
* Character Name [CharField]
* Creator [CharField] -> [ForeignKey] (change once user system is in place)
* Class [CharField]
* Level [IntegerField]
* Background [CharField]
* Race [CharField]
* Alignment [CharField]
* Experience [CharField]
* Inspiration [BooleanField]
* Proficiency Bonus [IntegerField]
* Strength [IntegerField]
* Dexterity [IntegerField]
* Constitution [IntegerField]
* Intelligence [IntegerField]
* Wisdom [IntegerField]
* Charisma [IntegerField]
* Maximum HP [IntegerField]
* Current HP [IntegerField]
* Temporary HP [IntegerField]
* Death Saves Success [IntegerField]
* Death Saves Failure [IntegerField]
* Armor Class [IntegerField]
* Initiative [IntegerField]
* Speed [IntegerField]
* Strength Saving Throw + Proficiency [IntegerField, BooleanField]
* Dexterity Saving Throw + Proficiency [IntegerField, BooleanField]
* Constitution Saving Throw + Proficiency [IntegerField, BooleanField]
* Intelligence Saving Throw + Proficiency [IntegerField, BooleanFIeld]
* Wisdom Saving Throw + Proficiency [IntegerField, BooleanField]
* Charisma Saving Throw + Proficiency [IntegerField, BooleanField]
* Acrobatics + Proficiency [IntegerField, BooleanField]
* Animal Handling + Proficiency [IntegerField, BooleanField]
* Arcana + Proficiency [IntegerField, BooleanField]
* Athletics + Proficiency [IntegerField, BooleanField]
* Deception + Proficiency [IntegerField, BooleanField]
* History + Proficiency [IntegerField, BooleanField]
* Insight + Proficiency [IntegerField, BooleanField]
* Intimidation + Proficiency [IntegerField, BooleanField]
* Investigation + Proficiency [IntegerField, BooleanField]
* Medicine + Proficiency [IntegerField, BooleanField]
* Nature + Proficiency [IntegerField, BooleanField]
* Perception + Proficiency [IntegerField, BooleanField]
* Performance + Proficiency [IntegerField, BooleanField]
* Persuasion + Proficiency [IntegerField, BooleanField]
* Religion + Proficiency [IntegerField, BooleanField]
* Sleight of Hand + Proficiency [IntegerField, BooleanField]
* Stealth + Proficiency [IntegerField, BooleanField]
* Survival + Proficiency [IntegerField, BooleanField]
* Passive Wisdom (Perception) [IntegerField]
* Money (CP) [FloatField]
* Money (SP) [FloatField]
* Money (EP) [FloatField]
* Money (GP) [FloatField]
* Money (PP) [FloatField]
* Spellcasting Ability [CharField]
* Spell Attack Bonus [IntegerField]
* Spell Save DC [IntegerField]
* Proficiencies and Languages [TextField]
* Features and Traits [TextField]
* Personality [TextField] (include ideals, bonds, and flaws here)
* Background [TextField] (+ allies, treasure, etc. Things important to the character lore-wise)

Note: Personality and Background may not be available at first.

#### Equipment
Includes:
* Character [ForeignKey]
* Equipment [CharField]
* Quantity [IntegerField]
* Weight [FloatField]

#### SpellSlots
Includes:
* Character [ForeignKey]
* Level [IntegerField] (0 - 9)
* Used Slots [IntegerField]
* Total Slots [IntegerField]

#### AttacksSpellcasting
Includes:
* Character [ForeignKey]
* Attack Name [CharField]
* Hit/DC [CharField]
* Range [IntegerField]
* Damage/Type [CharField]

#### CharacterSpells
Includes:
* Character [ForeignKey]
* Spell Name [CharField]
* Level [IntegerField]
* Prepared [BooleanField]

## Website Layout

The website will comprise of the following types of pages:
1. Index page, which will list characters and their creators
2. Submission page, where users can post their cahracters
3. Character page, where users can view characters
4. Edit page, which appears like submission but with information automatically filled out

## Milestones
* Set up a Django project and an app for the D&D pages (<1 hour)
* Set up the models for the databases, based on a D&D character sheet. (3-4 hours to get right)
* Prototype character pages (2-3 days)
* Set up the character pages, showing the information stored in the database (several days)
* Prototype submission page in HTML (2-3 days)
* Set up a submission page that takes in a user's character's information (several days)
* Set up character editing (several days + research)

### Bonus Milestones
* Set up the user system, including mapping users to characters (several days + research)
* Set up user creation (several days)
* CSS (2-3 days, since its just appearance)
* Search function (???????)
