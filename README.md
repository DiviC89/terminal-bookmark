# Terminal bookmarks (bm.py)

For quick and easy navigation around your terminal.
Install by adding the folder that contains the file to your env variables.

## bm bookmark

This will take your current working directory and save it with a tag.

Usage:

```
bm bookmark iWillRemember
```

## bm go

I didn't find a quick and easy way to take control of the terminal outside the script, so stdout is used to be able to pipe the output to cd and take you to where ever you like.

Usage:

```
bm go iWillRemember | cd
```

## bm list

List all saved bookmarks and paths

## bm remove

Removes a bookmark from the list.

Usage:

```
bm remove iWillRemember
```
