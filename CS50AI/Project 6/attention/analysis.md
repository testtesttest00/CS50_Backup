# Analysis

## Layer 2, Head 2

Each word token pays attention to the proceeding token
Except for the CLS and SEP tokens that pay attention to the CLS token

Example Sentences:
- [MASK] you
- i [MASK] you
- i just had [MASK] and it felt so good
- i have [MASK] with you and it feels so good

## Layer 2, Head 5

Each word token pays attention to the preceeding token
Except for the CLS and SEP tokens that pay attention to the CLS token

Example Sentences:
- i [MASK] you
- [MASK] you
- i just had [MASK] and it felt so good
- i have [MASK] with you and it feels good

## Layer 8, Head 1

The words from the half of the prose before the conjunction word "and" pay attention to each other.
Words after the "and" pay attention to "and".

Example Sentences:
- i just had [MASK] and it felt so good
- i have [MASK] with you and it feels good

### Sentences used:
1. [MASK] you
2. i [MASK] you
3. i just had [MASK] and it felt so good
4. i have [MASK] with you and it feels good
