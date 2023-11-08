# Value vs Reference

## Post sprint evaluation

Below are a series of scenarios and questions designed to make you _think_ and _engage_ more actively with the content you have been working with. An essential prerequisite to writing any good code is being able to learn well and thoroughly - and in order to do this you need to interrogate what you are learning properly. Thinking critically is something we are going to encourage you to do from the very beginning and these questions are designed to help you with the process of rigorous analytical thinking.

These questions are _not_ part of an assessment and nor or are they an attempt to trip you up or to catch you out. A well posed question ( we hope ) is one that is designed to make you think. And if you are struggling to answer the questions below - well, that's good, it means you are on the verge of learning something new!

---

### Scenario 1

```py
phone_book = {
  'cat': '0731415926',
  'joe': '0727182920',
  'simon': '079012312',
}

user_name = 'cat'
phone_number = phone_book.get("user_name")

print(f'Ahh hello there {user_name}, looks like your phone number is {phone_book.get("user_name")}')
```

After running the above snippet, the following is printed to the console:

`Ahh hello there tom, looks like your phone number is None`

Ooops, looks like the `phone_number` isn't being printed, instead we're getting back `None`.

Can you work out how to fix this issue so the actual `phone_number` is printed?

---

### Scenario 2

```py
def test_value_vs_reference():
    num_list = [1, 2, 3]
    assert num_list is [1, 2, 3]

def test_value_vs_reference():
    num_list = [1, 2, 3]
    assert num_list == [1, 2, 3]

```

Just 1 of the test cases above will **pass** ✅ and another will **fail** ❌ - can you explain which way around it will be and _critically_ why?

---

### Scenario 3

```py
jumbled_alpha = ['b', 'c', 'a', 'd']

def sort_list(str_list):
    str_list.sort()
    return str_list

sorted_alpha = sort_list(jumbled_alpha)

print(sorted_alpha == jumbled_alpha)
```

You embark upon the task of implementing a function that can sort a list of items into alphabetical order. At the end there is a `print` with a `==` comparison between `sorted_alpha` and `jumbled_alpha`

What will be printed when this print runs - `True` or `False` ?
OK so there is a fifty-fifty chance of guessing the correct answer in the above scenario, can you justify your answer.

**See if you can go through the code line by line to work it out.**

### Scenario 4

```py
people = [
  {'name': 'alex'},
  {'name': 'chon'},
  {'name': 'danika'},
  {'name': 'kyle'}
]

def add_job(people_list):
    people_copy = people_list.copy()

    for person in people_copy:
        person['job'] = 'tutor'
    return people_copy

add_job(people)

print(people)
```

What will the above `print` print out ? Give reasons for your answer

---

### Scenario 5

```py
def format_people(empty_list):
    if empty_list is []:
        return []
    else:
        # do other formatting logic here...
```

Above shows the beginnings of someone's implementation for a function called `format_people`. However, when invoked like this:

```py
format_people([])
```

they find that the first `if` block is **not** being executed. Can you work out what is going on here ?

---