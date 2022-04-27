# #Weekly 20
## Introducing the Times Table Tool! (TTT)

For my submission for #Weekly 20, I present to you the
TTT (Times Table Tool).

I tried my best to make the tool the best to make up for the minimal Fibbo Prime program.

This introduces new features which is a setup up from the table management in the Character Sort Tool. Now instead of telling you in a list how good this tool is, I will tell you with *words*.

## Intutive Features

Why hassle with renaming, deleting, and creating CSVs when TTTWorkspace can do it for you?

TTTWorkspace manages the files and directory. Currently the only
limitation is that it will only access the TTTWorkspace file and
export files to the TTTWorkspace folder's parent directory.

TTTWorkspace's GUI is a step up from the Character Sort Tool by
adding new and improved GUI menus.

We still have the normal menus:

TTTWORKSPACE MENU BUTTON
TTTWORKSPACE MENU INPUT

But now we have:

TTTWORKSPACE MENU CHOOSER

This new menu improves the accesibility by preventing errors and
bugs which can confuse users.

Plus, TTTWorkspace automatically does the work for you. With
TTTWizard, create new tables without hassle, and delete faster
than the speed of light in the Table Manager.

TTTWorkspace is simple, easy to use. If you like typing, edit your
configuration file and set `view="compact"`. This turns your view
into a basic type terminal, which isn't the best for everyone.

## File Management Features

TTTWorkspace allows you to handle your files bugfree. For example,
the configuration file has a list of files which it knows those
exist (unless the user interferes with the directory, so make sure
you update the `files` key if you add or remove files.), so it should
lead to a bugfree experience (as long as there is no user interference).

TTTWorkspace also allows for variety. Export your tables as a JSON or
CSV, or if you want to go experimental, export your table as a python file. This feature is only available for compact view. Distinct Values
is only exportable as JSON right now through cozy view.

## Speeed Mode

You heard that right - it's called *speeed* mode. Why hassle with tables when you can take a shortcut? 
You did come here for "Distinct Values" anyways.
Speeed Mode was inspired by almost all of this month's weeklys.
Program Speed is important, no one can wait 3 years for a program
to find the 15 prime if it's already solved. Speeed Mode doesn't
have the same features as TTTWorkspace, but is much faster in the
case that it doesn't have to make and store a table.
Now please note that this doesn't make the program much faster, but
makes it more efficent.

## Some Misc Features

- Alphanumerical checks - Fixes many filename issues, integer processing issues, and more.
- Color variety - Now much more pleasing to the eye!

## Some Issues

I've already tested this for bugs. The only issues you'll ever come
across is that the table or distinct values don't fit the display
and wrap, which isn't a big deal.

Another "issue" (I guess you could say), is that the compact view 
management isn't the same as the cozy view. I actually scrapped
the "compact" view and called it that. This is why the cozy view has 
different features compared to the compact view. I decided not to
move the "export as python" feature as it uses `str` which isn't reliable.

If TTTWorkspace bugs, you may have interfered with the TTTWorkspace 
directory. Make sure the `files` value in `config.toml` is updated 
with all of the directory's files. TTTWorkspace does not support 
subdirectories.

# Thanks for using the Times Table Tool
