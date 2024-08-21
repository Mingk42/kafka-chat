from kchat.cli import ping

def test_ping():
    rst=ping()
    print("\ntest::: assert rst==\"pong\"" )
    assert rst=="pong"
