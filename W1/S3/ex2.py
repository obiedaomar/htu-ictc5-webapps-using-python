# Flow Control - Loops

# for loops

# Iterating over a list
my_numbers_list = [2, 4, 6, 8, 10, 12]

for number in my_numbers_list:
    print("The number %d is even." % number)


# Iterating over a sting

my_message = "Hello, Python!"

# my_message[0] --> H
# my_message[1] --> e
# my_message[2] --> l
# my_message[3] --> l
# my_message[4] --> o
# my_message[5] --> ,

for char in my_message:
    print("%s capitalized is: %s" % (char, char.capitalize()))


# Iterating over a dictionary

favorite_songs = {
    1: {"title": "Breathe", "artist": "Pink Floyd", "tags": ["Rock", "Electric Guitar"]},
    2: {"title": "November Rain", "artist": "Guns N' Roses", },
    3: {"title": "I Want To Break Free", "artist": "Queen"},
    4: {"title": "Don't Stop Me Now", "artist": "Queen", "tags": ["Rock", "Electric Guitar"]}
}

for song_id in favorite_songs:
    title = favorite_songs[song_id].get('title')
    artist = favorite_songs[song_id].get('artist')
    tags = favorite_songs[song_id].get('tags')

    # What would this print?
    print(f"'{title}' a great song by '{artist}'.")
    if tags:
        for tag in tags:
            print(f"The song {title} has the following tag: {tag}.")

    # A not so optimal alternative to the if / for / get above.
    # if 'tags' in favorite_songs[song_id].keys():
    #     for tag in favorite_songs[song_id]['tags']:
    #         print(f"The song {title} has the following tag: {tag}.")


# Iterating over a netsted data structure

squares = [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

for number, number_square in squares:
    # What would this print?
    print(f"The square of {number} is {number_square}.")

# while loops

# The horrible while loop

# while True:
#     pass  # Do nothing

# Infinite while loop
# i = 0
# while i < 0:
#     print("I will stop some time!")
#     i = i - 1


# While loop
i = 1
while i <= 5:
    print(f"i is currently: {i}")
    i = i + 1
