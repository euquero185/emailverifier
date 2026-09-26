import time
import sys

print("-" * 120)
print("Email verifier by Euquero185")
print("-" * 120)
print("Welcome to the Email verifier")
print("This program does not verify whether an email exists. It only performs basic format validation.")

def program():

    while True:

        user = input("Please enter your language (Supported Languages: English, Portuguese) >>> ").strip().lower()
        if user == "english": #<-----English Version
            email = input("Please enter your email address >>> ").strip()
            def english_verify():
                if (
                        "@" in email
                        and "." in email
                        and email.count("@") == 1
                        and not email.startswith("@")
                        and not email.endswith(".")
                ):
                    print("Email is Valid")
                else:
                    print(" Email is not Valid")

            english_verify()

        elif user == "portuguese":
            email = input("Por favor, insira o seu endereço de email >>> ")
            def portuguese_verify():
                if (
                    "@" in email
                    and "." in email
                    and email.count("@") == 1
                    and not email.startswith("@")
                    and not email.endswith(".")
                ):
                    print("Email é válido")
                else:
                    print("Email é inválido")

            portuguese_verify()

        def end():
            if user == "english":
                def english_end():
                    user_end = input("Would you like to continue?(y/n) >>> ").strip().lower()
                    if user_end == "y":
                        print("Restarting Program...")
                        time.sleep(3) 
                    if user_end == "n":
                        print("Closign Program...")
                        print("Thanks for trying the email verifier!")
                        time.sleep(2)
                        sys.exit()
                english_end()

            if user == "portuguese":
                def portuguese_end():
                    user_end = input("Gostaria de continuar? (s/n) >>> ").strip().lower()
                    if user_end == "s":
                        print("A reinicar programa...")
                        time.sleep(3)
                    if user_end == "n":
                        print("A fechar o programa:")
                        print("Obrigado por experimentar o verificador de email!")
                        time.sleep(2)
                        sys.exit()
                portuguese_end()
        end()

program()
