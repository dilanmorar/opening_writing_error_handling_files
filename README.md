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

## try: except: finally:
These blocks of code are used in conjunction to error handle
```buildoutcfg
try:
    block of code
except <exception> as place_holder :
    block of code
    print('place_holder')
finally:
    block of code
```
### Using open() and with()
When using open you need to cloe the files you actually open.

you can skip this step by using 'with'
```buildoutcfg
with open(<file>, <option>) as <place_holder>:
    <place_holder>.readlines()

```


### Exceptions 
These occur when an error occurs 