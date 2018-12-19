# pluralize

This is my simple solution to the common issue of formatting numbers into sentences such that making them plural is a nessecity. While you could easily use an if statement, this allows for much more use cases. It all started with [this](https://stackoverflow.com/questions/53589770/making-sentence-word-plural-based-on-value) question on stackoverflow.

**Output a simple number** (deleted) **to user readable format**

deleted = 2

**Desired output**

"2 entries were removed"

**The old way of getting this output**

`print(f'Done! {deleted} entr{"y was" if deleted == 1 else "ies were"} removed.')`

*or*

`print(f"{deleted} {(plural, singular)[abs(num) == 1]}")`

With **pluralize**

```
import pluralize

deleted = pluralize(deleted, singular="entry", plural="entries")
print(f"{deleted} were removed")```
