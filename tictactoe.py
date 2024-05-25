BOARD_TEMPLATE = [
    [" ",  "|", " ", "|", " "],
    ["-",  "|", " ", "|", "-"],
    [" ",  "|", " ", "|", " "],
]

def draw():
    for row in BOARD_TEMPLATE:
        print("".join(row))

def main():
    draw()

if __name__ == "__main__":
    main()