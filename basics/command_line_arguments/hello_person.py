def hello(name, lang):
    greetings = {
        "English" : "Hello",
        "Afrikaans" : "More",
        "German" : "Hallo",
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)
    
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description= "Provides personal greeting."
    )

    parser.add_argument(
        "-n", "--name",metavar="name", dest="firstname"
        ,required=True, help="The name of the person to greet."
        )
    
    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English", "Afrikaans", "German"],
        help="The language of the greeting."
    )

    args = parser.parse_args()
    
    hello(args.firstname, args.lang)
