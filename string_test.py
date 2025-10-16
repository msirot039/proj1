print("Enter Text: ")
str = input()
    
for a in range(len(str)):
    match str[a]:
        case "a" :
            print(f" {str[a]} - Vowel")
        case "e" :
            print(f" {str[a]} - Vowel")
        case "i" :
            print(f" {str[a]} - Vowel")
        case "o" :
            print(f" {str[a]} - Vowel")
        case "u" :
            print(f" {str[a]} - Vowel")
        case _ :
            print(f" {str[a]} - Consonant")
