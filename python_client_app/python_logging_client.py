from python_client_library.logging_functions import login, start_run, log, upload_file, finish_run


def main():
    print("Starting main ... ")
    logged_in = login('user1', 'psw1')
    if logged_in:
        print("Logged in successfully.")
    else:
        print("Login failed.")
        exit()

    start_run("t1")

    log("starting program execution", "test")
    
    log("test msg 1", "test")
    
    upload_file('./python_client_app/weights.txt',".chp")
    upload_file('./python_client_app/python_logging_client.py', "code")
    upload_file('./python_client_app/labels.txt',"labels")

    log("finishing program execution", "test")
    finish_run()


main()
