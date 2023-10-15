# Battleship Game - State Tracker 

## Design Insights

#### **Board Representation and Data Structure**:
The game board is implemented using a dictionary (`self.grid`) where grid coordinates (tuples) map to ship objects. Consider a scenario where two ships, one of length 3 and another of length 2, are positioned on the board; one horizontally from (2, 3) and another vertically from (4, 5). The board representation might be:
```
{
    (2,3): <Ship Object 1>,
    (3,3): <Ship Object 1>,
    (4,3): <Ship Object 1>,
    (4,5): <Ship Object 2>,
    (4,6): <Ship Object 2>
}
```
This design provides quick checks to see if a spot on the board has a ship or is empty.

#### **Readability**:
For clarity, the `Board` class breaks down larger functions like `place_ship` into smaller, focused methods. This makes the code easier to understand and the flow more straightforward.

#### **Maintainability**: 
Detailed commits, each tackling a specific task or issue, help keep the project easy to update and track. Additionally, the use of Poetry ensures consistent dependency management, streamlining the setup process and ensuring that the project runs smoothly across different environments.

#### **Testability**:
The project uses both unit and BDD tests to thoroughly check the game's basic mechanics. This broad testing approach is seen throughout the commit history, showing the depth of the quality checks.

#### **Extensibility**:
The clear roles between the `Board`, `Ship`, and `Player` classes highlight the flexibility of the design. This structure helps with adding more advanced game features later on.

### Player Class and "Pass Through" Methods:

Right now, the `Player` class might seem to just pass commands to the `Board` class. But as the game grows, the `Player` class will handle more player-specific tasks and strategies. For example, guiding player moves, managing input/output, and adding unique player strategies. The current "pass-through" methods pave the way for these additions, making sure game mechanics and player actions stay separate.

## How To Run

For BDD tests:
```
poetry run behave
```

For unit tests:
```
poetry run python -m unittest discover tests
```

## Commit History:

The commit messages show the step-by-step TDD approach. While the commits are detailed for this project to show the development process, I would group changes in larger commits as part of a usual project.

## Future Extensions

The basic Battleship rules are set. From here, we can add more game features like player turns, terminal-based prompts, and even computer opponents. 
