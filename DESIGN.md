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

### lang_histogram() Method Design
- `self` is the current instance of the class
- `self.devs` is the instance variable of the class
    - the elements of the list are dictionaries
    - each dictionary corresponds to a row in the text file
- define an accumulator `lang_histo` and initialize it to an empty dictionary
- call `freq_of_lang` method using the class instance `self`
- assign the return value of it to the variable `lang_freq`
- `lang_freq` contains key-value pairs of language-frequency
- using `for` loop iterate through the items of `lang_freq` with `lang,freq` as iterators
- at each iteration:
    - check if `freq` is in `lang_histo`
        - if not, then initialize `freq` of `lang_histo` to an empty list
    - append `lang` to `lang_histo` at the key `freq`

### (replace with method name) Method Design

