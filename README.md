# Opening, Writing and Error Handling 

Topics covered:
- open()
- try and except
- with and finally
- exceptions and error handling
```buildoutcfg
All that can go wrong, will go wrong - Mr. Murphy
```

## Error handling
Means assuming things will break, and handling errors when they do.
Providing adequate feedback whiling failing with grace.

When you handle your errors, your code can continue to run. 
Which is a good thing.

## Definitions

## try: except:
These blocks of code are used in conjunction to error handle
```buildoutcfg
try:
    block of code
except <exception> as place_holder :
    block of code
    print('place_holder')
```

### Exceptions 
These occur when an error occurs 