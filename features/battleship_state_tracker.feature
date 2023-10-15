Feature: Battleship Board

  Scenario: Placing a horizontal ship on the board
    Given a battleship board of size 10 by 10
    When I place a ship of size 4 horizontally at position 3,4
    Then the ship should occupy positions from 3,4 to 6,4

  Scenario: Placing a vertical ship on the board
    Given a battleship board of size 10 by 10
    When I place a ship of size 3 vertically at position 2,3
    Then the ship should occupy positions from 2,3 to 2,5

  Scenario: Attacking a position with no ship
    Given a battleship board of size 10 by 10
    When I attack position 5,5
    Then the result should be a miss

  Scenario: Attacking a position with a ship
    Given a battleship board of size 10 by 10
    And a ship of size 3 horizontally at position 2,3
    When I attack position 2,3
    Then the result should be a hit

  Scenario: Player loses when all their ships are sunk
    Given a battleship board of size 10 by 10
    And a player for the board
    And a ship of size 3 horizontally at position 2,3
    And a ship of size 2 vertically at position 4,4
    And a ship of size 4 horizontally at position 6,6
    When all ships are attacked and sunk
    Then the player should lose the game

  Scenario: Player does not lose if not all ships are sunk
    Given a battleship board of size 10 by 10
    And a player for the board
    And a ship of size 3 horizontally at position 2,3
    And a ship of size 2 vertically at position 4,4
    When the ship at position 2,3 is sunk
    Then the player should not lose the game