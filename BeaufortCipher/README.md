# BEAUFORD CIPHER 

## Encryption

The Beauford Cipher just takes as imput a key and a text. 
By creating string of the alphabet:

```ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"```

You run a loop seaching for the index of each letter of the text and the key.
The cipher letter index comes from the expresion:

```c_ind = (k_ind - m_ind) mod 26```

Where,

- k_ind: is the index of the key letter 
- m_ind: is the index of the message letter

The key doesnt have to be the same value with the message. 
It is resuable meaning when the key runs out you start repeating it again.
The right index of the key can be calculated by the equation:

```k_ind = i mod (len_k)```

Where,

- i is the the index of the next letter in the message
- len_k is the length of the key

## Decryption

For Decryption is basically the same process:

``` m_ind = (k_ind - c_ind) mod 26 ```

Where, 

- k_ind: is the index value of the key
- c_ind: is the index value of the cipher message

Then by appending a list with the output you can then join it all together and 
have your decrypted text ready.


