from behave import given, when, then
from src.board import Board
from src.player import Player
from src.ship import Ship


def sanitise_orientation(orientation):
    if orientation == 'horizontally':
        return 'horizontal'
    elif orientation == 'vertically':
        return 'vertical'
    else:
        return orientation


@given('a battleship board of size 10 by 10')
def step_given_board(context):
    context.board = Board()


@given(u'a ship of size {size:d} {orientation} at position {x:d},{y:d}')
def step_given_ship(context, size, orientation, x, y):
    orientation = sanitise_orientation(orientation)
    ship = Ship(size, orientation)
    context.board.place_ship(ship, (x, y))


@when('I place a ship of size {size:d} {orientation} at position {x:d},{y:d}')
def step_place_ship(context, size, orientation, x, y):
    orientation = sanitise_orientation(orientation)
    ship = Ship(size, orientation)
    context.board.place_ship(ship, (x, y))
    context.ship = ship


@then('the ship should occupy positions from {start_x:d},{start_y:d} to {end_x:d},{end_y:d}')
def step_ship_occupy_positions(context, start_x, start_y, end_x, end_y):
    ship = context.ship
    assert context.board.get_ship_at((start_x, start_y)) == ship
    assert context.board.get_ship_at((end_x, end_y)) == ship


@when('I attack position {x:d},{y:d}')
def step_attack_position(context, x, y):
    context.attack_result = context.board.attack((x, y))


@then('the result should be a {result}')
def step_attack_result(context, result):
    assert context.attack_result == result


@when('all ships are attacked and sunk')
def step_attack_all_ships(context):
    for position in context.board.grid.keys():
        context.board.attack(position)


@then('the player should lose the game')
def step_player_should_lose(context):
    assert context.player.has_lost() is True, "Expected the player to have lost"


@then('the player should not lose the game')
def step_player_should_not_lose(context):
    assert context.player.has_lost() is False, "Expected the player to not have lost"


@given(u'a player for the board')
def step_given_player_for_board(context):
    context.player = Player(context.board)


@when(u'the ship at position {x:d},{y:d} is sunk')
def step_sink_specific_ship(context, x, y):
    ship = context.board.get_ship_at((x, y))
    for _ in range(ship.length):
        context.board.attack((x, y))
        if ship.orientation == 'horizontal':
            x += 1
        else:
            y += 1
