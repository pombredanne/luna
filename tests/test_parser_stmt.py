from luna.ast import *


def test_ass1(parse_stmt):
    assert Stmt(
        Assignment(
            Identifier('a'),
            Expr(
                Number('1'),
            ),
        ),
    ) == parse_stmt('a = 1')


def test_call1(parse_stmt):
    assert Stmt(
        Call(
            Identifier('f'),
            Args(
                Expr(
                    Number('1'),
                ),
                Expr(
                    Number('2'),
                ),
                Expr(
                    Number('3'),
                ),
            ),
        ),
    ) == parse_stmt('f(1, 2, 3)')


def test_if1(parse_stmt, parse_expr):
    assert Stmt(
        If(
            parse_expr('true'),
            Block(parse_stmt('print(x)')),
            None,
        ),
    ) == parse_stmt('if true then print(x) end')

def test_if2(parse_stmt, parse_expr):
    assert Stmt(
        If(
            parse_expr('true'),
            Block(parse_stmt('print(1)')),
            Block(parse_stmt('print(2)')),
        ),
    ) == parse_stmt('if true then print(1) else print(2) end')

def test_if3(parse_stmt, parse_expr):
    assert Stmt(
        If(
            parse_expr('true'),
            Block(parse_stmt('print(1)')),
            If(
                parse_expr('true'),
                Block(parse_stmt('print(2)')),
                If(
                    parse_expr('false'),
                    Block(parse_stmt('print(3)')),
                    Block(parse_stmt('print(4)')),
                ),
            ),
        ),
    ) == parse_stmt('''if true then print(1)
                    elseif true then print(2)
                    elseif false then print(3)
                    else print(4)
                    end''')


# broken
def test_repeat1(parse_stmt):
    assert Stmt(
        Repeat(
            Block(
                Stmt(Lazy()),
            ),
            Expr(Lazy()),
        ),
    ) == parse_stmt('repeat print(1) until true')


def test_while1(parse_stmt):
    assert Stmt(
        While(
            Expr(Lazy()),
            Block(
                Stmt(Lazy()),
            ),
        ),
    ) == parse_stmt('while true do print(1) end')
