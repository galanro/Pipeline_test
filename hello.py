import hello

def test_say_hello():
    assert hello.say_hello() == "Hello, World!"

def say_hello():
    return "Hello, World!"
