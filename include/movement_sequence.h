#ifndef MOVEMENT_SEQUENCE_H
#define MOVEMENT_SEQUENCE_H

struct MovementStep {
    enum Type { MOVE, LEFT_DOWN, LEFT_UP, WAIT };
    Type type;
    int x, y, delay_ms;
};

const MovementStep sequence[] = {
    {MovementStep::WAIT, 0, 0, 333},
    {MovementStep::WAIT, 0, 0, 6062},
    {MovementStep::LEFT_DOWN, 792, 856, 0},
    {MovementStep::WAIT, 0, 0, 16},
    {MovementStep::LEFT_UP, 792, 856, 0},
    {MovementStep::LEFT_DOWN, 792, 856, 0},
    {MovementStep::WAIT, 0, 0, 16},
    {MovementStep::LEFT_UP, 792, 856, 0},
    {MovementStep::WAIT, 0, 0, 3000},
    {MovementStep::LEFT_DOWN, 1425, 961, 0},
    {MovementStep::WAIT, 0, 0, 15},
    {MovementStep::LEFT_UP, 1425, 961, 0},
    {MovementStep::WAIT, 0, 0, 2578},
    {MovementStep::LEFT_DOWN, 1421, 957, 0},
    {MovementStep::LEFT_UP, 1421, 957, 0}
};

#endif

