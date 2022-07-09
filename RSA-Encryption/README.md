# RSA-ENCRYPTION

## MODES

- Generate
- Encode 
- Decode

### GENERATE

``` RSAPython.py generate 4000 ```

The second argument you pass is the bounds for generating P and Q.

### ENCRYPT

``` RSAPython.py encrypt 62780327 7 "hi" ```

This Encrypts text with the settings:

> N = P*Q = 62780327
> e = 7
> text to be encrypted as "hi"

This outputs:

> 20530622

Which when decrypted is then decrypted into "hi".

### DECRYPT

``` RSAPython.py decrypt 62780327 17932663 "20530622" ```

This Decrypts text with settings:

> N = P*Q = 62780327
> d = 17932663
> encrypted text = 20530622

This outputs:

>HI

The text was sucessfully decrypted.

## PROCESS OF CREATING THE VARIABLES

### THE VARIABLE P

P is a random large interger prime.
It is randomly generated

### THE VARIABLE Q 

Q is a random large interger prime.
It is randomly generated with a value different than P

### THE VARIABLE N

N is the sum of the primes P and Q. N is the main number
used for Encrypting and Decrypting.

### THE VARIABLE e

- e is an integer between 1 and Φ(N)
- e is not a divisor of N
- e is a coprime to N

#### Function Φ(N)

Euler's totient function counts the positive integers up to a given integer n that are relatively prime to n.
Phi is a multiplicative function this means that if gcd(m, n) = 1, then φ(m) φ(n) = φ(mn)

Because P and Q are prime then Φ(P) = P - 1 and Φ(Q) = Q - 1
and because Φ(Ν) = Φ(PxQ) = Φ(P)xΦ(Q) = (Q-1)x(P-1)

### THE VARIABLE d

d is the a number that satisfies the following solution:

1 = (d*e) mod N

Then the selection of variables is complete and we can fully encrpypt and decrypt.

## THE PROCESS OF ENCRYPTION 

The message is firstly turned into numbers meaning:

> A = 0
> B = 1
> ....
> Z = 25
> ' ' = 26

Then an array is created with all the numbers of a word and they are all encrypted seperately.
For example:

``` "test" = ["t","e","s","t"] = ["20","4","19","20"] ```

Then every letter is encrypted on its own using the following equation:

> encrypted_message = (number)^e mod N

Then the encrypted array would be joined together to form a string of encrypted lettes.

## THE PROCESS OF DECRYPTION

The encrypted message if firstly separated depending on the spaces. The spaces represent a new letter.
Meaning "8000 64 6859 8000" represents 4 encrypted letters.

Then "8000 64 6859 8000" is turned into:

```"8000 64 6859 8000" = ["8000", "64", "6859", "8000"] ```

Then every encrypted letter gets decrypted using the following equation:

> decrypted_message = (encrypted_message)^d mod N

Then the decrypted array would be turned back to numbers between 0-25 which would be then turned into letters.
Meaning:

``` ["8000", "64", "6859", "8000"] => ["20","4","19","20"] => ['T', 'E', 'S','T'] => TEST ```

# THE FULL PROCESS

## ENCRYPTION
```MESSAGE => ["M","E","S","S","A","G","E"] => ["13", "4", "19", "19", "0","4"] => [ENCRPYTED ARRAY]```

## DECRPYPTION
```[ENCRYPTED ARRAY] => ["13", "4", "19", "19", "0","4"] => ["M","E","S","S","A","G","E"] => MESSAGE ```

#### CREATED AND EDITED BY SYKEPHASIS
