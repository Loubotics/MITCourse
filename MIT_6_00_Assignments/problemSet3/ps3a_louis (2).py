ó
6$0Qc           @   s  d  d l  Z  d  d l Z d  d l Z d Z d Z d Z i d d 6d d 6d d	 6d
 d 6d d 6d d 6d
 d 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d  6d d! 6d d" 6d d# 6d d$ 6d d% 6Z d& Z d'   Z d(   Z	 d)   Z
 d*   Z d+   Z d,   Z d-   Z d.   Z d/   Z d0   Z e d1 k re   Z e e  e e d  d  n  d S(2   iÿÿÿÿNt   aeiout   bcdfghjklmnpqrstvwxyzi   i   t   ai   t   bt   ci   t   dt   ei   t   ft   gt   ht   ii   t   ji   t   kt   lt   mt   nt   ot   pi
   t   qt   rt   st   tt   ut   vt   wt   xt   yt   zs	   words.txtc          C   s^   d GHt  t d d  }  g  } x' |  D] } | j | j   j    q$ Wd Gt |  Gd GH| S(   s¯   
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    s   Loading word list from file...R   i    s     s   words loaded.(   t   opent   WORDLIST_FILENAMEt   appendt   stript   lowert   len(   t   inFilet   wordlistt   line(    (    s1   E:\MIT_6_00_Assignments\problemSet3\ps3a_louis.pyt
   load_words   s    c         C   s5   i  } x( |  D]  } | j  | d  d | | <q W| S(   sï   
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    i    i   (   t   get(   t   sequencet   freqR   (    (    s1   E:\MIT_6_00_Assignments\problemSet3\ps3a_louis.pyt   get_frequency_dict+   s    
c         C   sj   |  } | } d } x" | D] } | t  | j   7} q W| t |  } t |  d k rf | d 7} n  | S(   sª  
    Returns the score for a word. Assumes the word is a
    valid word.

	The score for a word is the sum of the points for letters
	in the word multiplied by the length of the word, plus 50
	points if all n letters are used on the first go.

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    i    i   i2   (   t   SCRABBLE_LETTER_VALUESR    R!   (   t   wordR   t	   workingOnt
   numLetterst   scoreR   (    (    s1   E:\MIT_6_00_Assignments\problemSet3\ps3a_louis.pyt   get_word_scoreA   s    c         C   s;   x3 |  j    D]% } x t |  |  D]
 } | Gq$ Wq WHd S(   s  
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    N(   t   keyst   range(   t   handt   letterR   (    (    s1   E:\MIT_6_00_Assignments\problemSet3\ps3a_louis.pyt   display_hand^   s
    c         C   s±   i  } |  d } xJ t  |  D]< } t t j d t t   } | j | d  d | | <q WxM t  | |   D]< } t t j d t t   } | j | d  d | | <qm W| S(   sS  
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    i   i    i   (   R1   t   VOWELSt   randomt	   randrangeR!   R&   t
   CONSONANTS(   R   R2   t
   num_vowelsR
   R   (    (    s1   E:\MIT_6_00_Assignments\problemSet3\ps3a_louis.pyt	   deal_handt   s    
c         C   s1   |  j    } x | D] } | | c d 8<q W| S(   sÌ  
    Assumes that 'hand' has all the letters in word.
	In other words, this assumes that however many times
	a letter appears in 'word', 'hand' has at least as
	many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    i   (   t   copy(   R2   R+   t   workingHandR   (    (    s1   E:\MIT_6_00_Assignments\problemSet3\ps3a_louis.pyt   update_hand   s    c         C   se   | j    } |  | k r t SxB |  D]: } | | k r9 t S| | d k rM t S| | c d 8<q# Wt S(   s  
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    i    i   (   R;   t   Falset   True(   R+   R2   t	   word_listR<   R   (    (    s1   E:\MIT_6_00_Assignments\problemSet3\ps3a_louis.pyt   is_valid_word©   s    c         C   s+   d } x |  j    D] } | | 7} q W| S(   Ni    (   t   values(   R2   t   handlenR   (    (    s1   E:\MIT_6_00_Assignments\problemSet3\ps3a_louis.pyt   calculate_handlenÃ   s    c         C   s½   d } |  j    } x t |  d k r¯ d GHt |  t d  } | d k rR Pn  t | | |  sl d GHq t | |  } t | t |   } | | 7} d | | | f GHq Wd G| GHd S(	   s;  
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      
    i    s   Current hand: s8   Enter word, or a "." to indicate that you are finished: t   .s+   That is not a valid word. Enter a new word!s'   "%s" earned %d points. Total: %d pointss   The total score is: N(   R;   RD   R4   t	   raw_inputRA   R=   R/   R!   (   R2   R@   t   totalR<   t   nextWordR.   (    (    s1   E:\MIT_6_00_Assignments\problemSet3\ps3a_louis.pyt	   play_handÍ   s    

c         C   s   t  t  } xo t r} t d  } | d k rI t  t  } t | |   q | d k re t | |   q | d k ru Pq d GHq Wd GHd S(   s§  
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    sI   Enter n to deal a new hand, r to replay the last hand, or e to end game: R   R   R   s   Invalid command.s   Thanks for playing. Bye now!N(   R:   t	   HAND_SIZER?   RF   RI   (   R@   R2   t   choice(    (    s1   E:\MIT_6_00_Assignments\problemSet3\ps3a_louis.pyt	   play_game  s    		t   __main__(   R6   t   stringt   permR5   R8   RJ   R*   R   R%   R)   R/   R4   R:   R=   RA   RD   RI   RL   t   __name__R@   t	   get_perms(    (    (    s1   E:\MIT_6_00_Assignments\problemSet3\ps3a_louis.pyt   <module>   s,   ¹								
	7	!	
