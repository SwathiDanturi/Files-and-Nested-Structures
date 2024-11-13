## Analysis Class Design Document
- Developer: Swathi Danturi
- Date: 11/11/2024

### freq_of_lang() Method Design
- `self` is the current instance of the class
- `self.devs` is the instance variable of the class
    - the elements of the list are dictionaries
    - each dictionary corresponds to a row in the text file
- define an accumulator `lang_freq` and initialize it to an empty dictionary
- iterate through each dictonary of the list `self.devs` using the iterable `dev_data`
- at each iteration:
    - get the `LanguageAdmired` string separated by `;` from `dev_data` using the same as key
    - split the above using `.split()` with `;` as delimited
    - assign the above list to `languages_admired`
    - iterate through each value `language` of the `languages_admired` using `for` loop
    - at each iteration:
        - check `language` should not equal `NA` using `if`:
            - `if` the `language` is not already in `lang_freq`:
                - initialize `lang_freq` of `language` to zero
            - increment the count of `lang_freq` of `language` by 1
- return `lang_freq`

### (replace with method name) Method Design
...

### (replace with method name) Method Design

