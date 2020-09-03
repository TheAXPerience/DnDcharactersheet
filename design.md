# DnD Character Sheet

A standard character sheet for the Dungeon and Dragons tabletop game.
Will display all the necessary elements for a campaign but must manually be input by users.
Thus, it will have the same feel as filling out a physical sheet but on the computer.

September 2nd, 2020
Status: Draft
Author: Alvin Xu

## Context
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

## Overview

The website will consist of a database used by Django to store user information, such as usernames, passwords, and character info.

### User Data

Users will be able to select a username and password for themselves on the website.
As such, the database must be able to store a username and password for each user, with usernames being unique.
There would need to be a character limit for both, so I will assume 30 for the time being.

Also, each user will need a mapping from their own account to the characters that they make. This will be a separate model, with foreign keys to users and characters.

### Character Information

The information present for the character model will be based on the Dungeons and Dragon's character sheet
This means that the following data needs to be present:

* Character Name
* Class
* Level
* Background
* Race
* Alignment
* Experience (?)
* Proficiency Bonus
* Strength
* Dexterity
* Constitution
* Intelligence
* Wisdom
* Charisma
* Saving Throws (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma)
* Skills (Acrobatics, Animal Handling, Arcana, Athletics, Deception, History, Insight, Intimidation, Investigation, Medicine, Nature, Perception, Performance, Persuasion, Religion, Sleight of Hand, Stealth, Survival)
* Armor Class
* Initiative
* Speed
* Maximum HP
* Current HP
* Temporary HP
* Death Saves (0-3 success, 0-3 failure)
* Hit Dice
* Sttacks & Spellcasting (name, attack bonus, damage/type)
* Equipment
* Money (CP, SP, EP, GP, PP)
* Passive Wisdom (Perception)
* Proficiencies and Languages
* Personality Traits
* Ideals
* Bonds
* Flaws
* Features and Traits
* Age
* Height
* Weight
* Eye Color
* Skin Color
* Hair Color
* Character Appearance
* Character Backstory
* Allies and Organizations
* Treasure
* Spellcasting Ability
* Spell Save DC
* Spell Attack Bonus
* Levels 0-9 Spell Slots (total + expended)
* Spells (name, level, prepared?)

Due to the sheer amount of information, some of it may not be present during earlier builds, and might not be present at all in the final build.

In addition to users being able to create characters, they need to be able to edit their information, such as when they take damage or level up.

### Milestones
* Set up the models for the databases, based on a D&D character sheet. Not all the info will be displayed, just the most important parts.
* Set up the character pages, showing the information stored in the database
* Set up the user system, including mapping users to characters (can be tested with admin privileges)
* Set up a submission page that takes in a user's character's information, and stretching when necessary (like for spells and proficiencies)
