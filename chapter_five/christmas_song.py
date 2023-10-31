for day in range(1, 13):
    match day:
        case 1:
            print("\t\t\tOn the first day of christmas")
        case 2:
            print("\t\t\tOn the second day of christmas")
        case 3:
            print("\t\t\tOn the third day of christmas")
        case 4:
            print("\t\t\tOn the fourth day of christmas")
        case 5:
            print("\t\t\tOn the Fifth day of christmas")
        case 6:
            print("\t\t\tOn the Sixth day of christmas")
        case 7:
            print("\t\t\tOn the Seventh day of Christmas")
        case 8:
            print("\t\t\tOn the Eight day of Christmas")
        case 9:
            print("\t\t\tOn the Nine day of Christmas")
        case 10:
            print("\t\t\tOn the Tenth Day of Christmas")
        case 11:
            print("\t\t\tOn the Eleventh Day of christmas")
        case 12:
            print("\t\t\tOn the Twelfth day of Christmas")
    match day:
        case 12:
            print("""
                Twelve Drums Are Drumming
                Eleven Pipes are pipping
                Ten lord are leaping
                Nine ladies are Dancing
                Eight maids a-milking
                Seven swarms a-swimming
                Six geese a-laying
                Five golden rings
                Four calling birds
                Three French Hens
                Two Turtle doves and
                A partridge in a pear tree
                """)
        case 11:
            print("""
                Eleven Pipes are pipping
                Ten lord are leaping
                Nine ladies are Dancing
                Eight maids a-milking
                Seven swarms a-swimming
                Six geese a-laying
                Five golden rings
                Four calling birds
                Three French Hens
                Two Turtle doves and
                A partridge in a pear tree  
                """, end="\n\n")
        case 10:
            print("""
                Ten lord are leaping
                Nine ladies are Dancing
                Eight maids a-milking
                Seven swarms a-swimming
                Six geese a-laying
                Five golden rings
                Four calling birds
                Three French Hens
                Two Turtle doves and
                A partridge in a pear tree
                """, end="\n\n")
        case 9:
            print("""
                Nine ladies are Dancing
                Eight maids a-milking
                Seven swarms a-swimming
                Six geese a-laying
                Five golden rings
                Four calling birds
                Three French Hens
                Two Turtle doves and
                A partridge in a pear tree
                """, end="\n\n")
        case 8:
            print("""
                Eight maids a-milking
                Seven swarms a-swimming
                Six geese a-laying
                Five golden rings
                Four calling birds
                Three French Hens
                Two Turtle doves and
                A partridge in a pear tree
                """, end="\n\n")
        case 7:
            print("""
                Seven swarms a-swimming
                Six geese a-laying
                Five golden rings
                Four calling birds
                Three French Hens
                Two Turtle doves and
                A partridge in a pear tree
                """, end="\n\n")
        case 6:
            print("""
                Six geese a-laying
                Five golden rings
                Four calling birds
                Three French Hens
                Two Turtle doves and
                A partridge in a pear tree
                """, end="\n\n")
        case 5:
            print("""
                Five golden rings
                Four calling birds
                Three French Hens
                Two Turtle doves and
                A partridge in a pear tree
                """, end="\n\n")
        case 4:
            print("""
                Four calling birds
                Three French Hens
                Two Turtle doves and
                A partridge in a pear tree
                """, end="\n\n")
        case 3:
            print("""
                Three French Hens
                Two Turtle doves and
                A partridge in a pear tree
                """, end="\n\n")
        case 2:
            print("""
            Two Turtle doves and
            A partridge in a pear tree
            """, end="\n\n")
        case 1:
            print("\t\t\tA partridge tree in a pear tree", end="\n\n")