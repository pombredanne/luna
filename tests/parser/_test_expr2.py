from luna.ast import *


def test_expr_unary1(parse_expr):
    assert Expr(
        UnaryOp(
            Operator('-'),
            Number('1'),
        ),
    ) == parse_expr('-1')

def test_expr_unary2(parse_expr):
    assert Expr(
        UnaryOp(
            Operator('not'),
            Expr(
                UnaryOp(
                    Operator('not'),
                    Boolean('true'),
                ),
            ),
        ),
    ) == parse_expr('not not true')


def test_expr_eq(parse_expr):
    assert Expr(
        BinOp(
            Boolean('true'),
            Operator('=='),
            Boolean('true'),
        ),
    ) == parse_expr('true == true')

def test_expr_neq(parse_expr):
    assert Expr(
        BinOp(
            Boolean('true'),
            Operator('~='),
            Boolean('true'),
        ),
    ) == parse_expr('true ~= true')


def test_expr_paren1(parse_expr):
    assert Expr(
        BinOp(
            Expr(
                BinOp(
                    Boolean('true'),
                    Operator('=='),
                    Boolean('true'),
                ),
            ),
            Operator('=='),
            Boolean('false'),
        ),
    ) == parse_expr('( true == true ) == false')

def test_expr_paren2(parse_expr):
    assert Expr(
        BinOp(
            Boolean('false'),
            Operator('=='),
            Expr(
                BinOp(
                    Boolean('true'),
                    Operator('=='),
                    Boolean('true'),
                ),
            ),
        ),
    ) == parse_expr('false == ( true == true )')


def test_expr_ternary1(parse_expr):
    assert Expr(
        BinOp(
            Expr(
                BinOp(
                    Number('2'),
                    Operator('-'),
                    Number('1'),
                ),
            ),
            Operator('-'),
            Number('3'),
        ),
    ) == parse_expr('2 - 1 - 3')

def test_expr_ternary2(parse_expr):
    assert Expr(
        BinOp(
            Number('2'),
            Operator('^'),
            Expr(
                BinOp(
                    Number('1'),
                    Operator('^'),
                    Number('3'),
                ),
            ),
        ),
    ) == parse_expr('2 ^ 1 ^ 3')

def test_expr_ternary3(parse_expr):
    assert Expr(
        BinOp(
            Expr(
                BinOp(
                    Number('4'),
                    Operator('=='),
                    Number('5'),
                ),
            ),
            Operator('=='),
            Number('9'),
        ),
    ) == parse_expr('4 == 5 == 9')


def test_expr_quaternary1(parse_expr):
    assert Expr(
        BinOp(
            Expr(
                BinOp(
                    Expr(
                        BinOp(
                            Boolean('true'),
                            Operator('=='),
                            Boolean('true'),
                        ),
                    ),
                    Operator('=='),
                    Boolean('true'),
                ),
            ),
            Operator('=='),
            Boolean('true'),
        ),
    ) == parse_expr('true == true == true == true')

def test_expr_quaternary2(parse_expr):
    assert Expr(
        BinOp(
            Expr(
                BinOp(
                    Boolean('true'),
                    Operator('=='),
                    Expr(
                        BinOp(
                            Boolean('true'),
                            Operator('=='),
                            Boolean('true'),
                        ),
                    ),
                ),
            ),
            Operator('=='),
            Boolean('true'),
        ),
    ) == parse_expr('true == (true == true) == true')


def test_expr_nums1(parse_expr):
    assert Expr(
        BinOp(
            Expr(
                BinOp(
                    Number('1'),
                    Operator('*'),
                    Number('2'),
                ),
            ),
            Operator('+'),
            Number('3'),
        ),
    ) == parse_expr('1 * 2 + 3')

def test_expr_nums2(parse_expr):
    assert Expr(
        BinOp(
            Number('1'),
            Operator('+'),
            Expr(
                BinOp(
                    Number('2'),
                    Operator('*'),
                    Number('3'),
                ),
            ),
        ),
    ) == parse_expr('1 + 2 * 3')

def test_expr_nums3(parse_expr):
    assert Expr(
        BinOp(
            Expr(
                UnaryOp(
                    Operator('-'),
                    Number('1'),
                ),
            ),
            Operator('+'),
            Number('1'),
        ),
    ) == parse_expr('-1 + 1')

def test_expr_nums4(parse_expr):
    assert Expr(
        BinOp(
            Expr(
                BinOp(
                    Number('7'),
                    Operator('+'),
                    Expr(
                        BinOp(
                            Number('5'),
                            Operator('*'),
                            Number('2'),
                        ),
                    ),
                ),
            ),
            Operator('+'),
            Number('3'),
        ),
    ) == parse_expr('7 + 5 * 2 + 3')

def test_expr_nums5(parse_expr):
    assert Expr(
        BinOp(
            Identifier('a'),
            Operator('+'),
            Number('1'),
        ),
    ) == parse_expr('a + 1')


def test_expr_call1(parse_expr):
    assert Expr(
        Call(
            Identifier('print'),
            Args(Lazy()),
        ),
    ) == parse_expr('print(x)')
