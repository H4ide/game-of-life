# Game of Life by John Conway

Welcome to the **Game of Life** project! This repository contains a Python implementation of John Conway's famous cellular automaton, the Game of Life. This project includes both a user guide and a programmer's guide to help you understand and interact with the game, as well as the source code for running the simulation.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Customization](#customization)
- [License](#license)

## Introduction

The **Game of Life** is a cellular automaton devised by British mathematician John Horton Conway in 1970. It consists of a grid of cells that evolve over time based on a set of rules. This simulation allows you to observe and interact with the evolution of these cells.

## Features

- Interactive simulation where you can change cell states.
- Visual representation of alive and dead cells.
- Pausing and resuming the simulation.
- Static and non-static cells for varied behaviors.
- Torus grid (edges wrap around).

## Installation

To run this project, you'll need to have Python and `pygame` installed on your machine.

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/game-of-life.git
    cd game-of-life
    ```

2. Install the required dependencies:
    ```bash
    pip install pygame
    ```

## Usage

To run the Game of Life simulation, execute the following command in your terminal:
```bash
python game_of_life.py
```
Follow the on-screen instructions to interact with the game.

## File Descriptions
- game_of_life.py: The main Python script that runs the Game of Life simulation. It includes the implementation of the game rules, user interaction, and display logic.

- User Guide to Game of Life.pdf: This document provides a detailed guide on how to use the Game of Life simulation, including controls and gameplay tips.

- Programmers Guide to Game Of Life.pdf: This document offers an overview of the program's structure, functionality, and instructions for making modifications or enhancements to the code.

## Customization
Feel free to modify the code to suit your preferences. Here are a few suggestions for customization:

- Grid Size: Change the WIDTH and HEIGHT constants in game_of_life.py to adjust the grid size.
- Cell Colors: Modify the RGB values of the color constants (COLOR_ALIVE_NOT_STATIC, COLOR_DEAD_NOT_STATIC, COLOR_ALIVE_STATIC, COLOR_DEAD_STATIC, COLOR_GRID) to customize cell colors.
- Update Frequency: Adjust the DELAY_MS constant to change the speed of the simulation.
- Additional Rules: Add or modify the rules in the game_of_life function to create new behaviors or patterns.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.MIT) file for more details.

## Contacts
Author: Iurii Koshelenko
[email](koshelenkoyura@gmail.com)
