from pysm import State, StateMachine, Event

on = State('on')
off = State('off')

sm = StateMachine('sm')
sm.add_state(on, initial=True)
sm.add_state(off)

action_one_called = False
action_two_called = False

def action_one(state, event):
    global action_one_called
    action_one_called = True

def action_two(state, event):
    global action_two_called
    action_two_called = True


sm.add_transition(on, off, events=['off'], actions=[action_one, action_two])
sm.add_transition(off, on, events=['on'])

sm.initialize()


def test():
    global action_one_called, action_two_called
    assert sm.state == on
    sm.dispatch(Event('off'))
    assert sm.state == off
    assert action_one_called == True
    assert action_two_called == True
    sm.dispatch(Event('on'))
    assert sm.state == on

