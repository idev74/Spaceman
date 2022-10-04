Load-Word: 
   READ Word file 
   SELECT random word from the index 
   RETURN string
   SET f to OPEN words.txt file 
   READ Words.txt
   SET words_list to read f 
   CLOSE f
   SAVE words_list to separate each word by space 
   SET secret_world to a random word from words_list
   RETURN secret_word

Is_word_guessed:
   INPUTS secret_word & letters guessed
   DOWHILE word is not fully guessed 
   PROMPT user to select letters 
   DISPLAY unused letters 
   CHECK if letter is present in secret_word
   GET letters used
   IF all letters in the word guessed correctly THEN
   BOOL secret_word = True
   DISPLAY "Correct! Your word was: secret_word"
   ELSE
   SET BOOL = False
   DISPLAY "Please keep guessing"
   ENDIF
   ENDDO

Get_guessed_word:
   INPUTS secret_word & letters_guessed
   DOWHILE word is not fully guessed 
   PROMPT user to select letters 
   DISPLAY unused letters 
   Check if letter is present in secret_word
   GET letters used
   SAVE correctly guessed letters to letters_guessed 
   RETURN letters guessed correctly & the places not guessed correctly taken by 
   underscores
   DISPLAY the correctly done portion of the word and the rest with underscores
   SAVE correctly guessed letters to letters_guessed 
   ENDDO

Is_guess_in_word:
   INPUTS guess & secret_word
   DOWHILE word is not fully guessed 
   PROMPT user to select letters 
   DISPLAY unused letters 
   Check if letter is present in secret_word
   IF guessed letter is present in secret_word THEN
   BOOL secret_word = True
   RETURN BOOL
   ELSE
   SET BOOL = False
   DISPLAY "Please guess again"
   GET letters used
   SAVE correctly guessed letters to letters_guessed 
   RETURN letters guessed correctly & the places not guessed correctly taken by 
   underscores
   ENDDO

Spaceman:
   INPUTS secret_word
   START program