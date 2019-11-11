# Smart Tab Control for Kitty

[Kitty][kitty] is a fast GPU-based terminal emulator.

[kitty]: https://sw.kovidgoyal.net/kitty


This kitten lets you bind keys to either control tabs in Kitty
or pass them through to a program running in a Kitty window,
depending on whether you, in fact, have any Kitty tabs.


## Why would you want that?

You can use Kitty on its own, and have multiple tabs.
In this case, you want to bind easy keys
such as <kbd>Alt</kbd>+<kbd>1</kbd>…<kbd>0</kbd>
to switch Kitty tabs.

Alternatively, you can run a terminal multiplexer such as `tmux` in Kitty,
perhaps because you want to preserve your session and access it over SSH.
In this case, you want those same keys to switch `tmux` windows.


# Minimum requirements

Kitty 0.13.0 or higher.


# Installation

* Copy or symlink `smart_tab.py`
  into your Kitty configuration directory
  (`~/.config/kitty`).

* Edit your `kitty.conf` to add some key shortcuts.

* Restart Kitty.


# Configuring shortcuts

In all cases, the last argument is a key to send to the active window
if the current OS window has only a single tab.
If there are two or more tabs,
all arguments except the last are executed as a Kitty command.

All the snippets below are only examples.
You should choose keys to suit your personal style.

Note that you can use other Kitty commands,
but the choice whether to perform the command
or send the key to the application
will depend on whether you have tabs in the current OS window.

## Next tab

```
map ctrl+page_down  kitty smart_tab.py  next_tab  ctrl+page_down
```

## Previous tab

```
map ctrl+page_up  kitty smart_tab.py  previous_tab  ctrl+page_up
```

## New tab

```
map ctrl+shift+t  kitty smart_tab.py  new_tab  alt+shift+t
```

Note that in this example the key sent to the application is different.
This is because terminal emulators typically cannot express
a <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>letter</kbd> combination.

## Close tab

```
map ctrl+shift+w  kitty smart_tab.py  close_tab  alt+shift+w
```

## Move tab forward

```
map ctrl+shift+page_down  kitty smart_tab.py  move_tab_forward  ctrl+shift+page_down
```

## Move tab backward

```
map ctrl+shift+page_up  kitty smart_tab.py  move_tab_backward  ctrl+shift+page_up
```

## Set tab title

```
map ctrl+shift+f2  kitty smart_tab.py  set_tab_title  ctrl+shift+f2
```

## Go to tab

```
map alt+1  kitty smart_tab.py  goto_tab 1  alt+1
map alt+2  kitty smart_tab.py  goto_tab 2  alt+2
…
map alt+9  kitty smart_tab.py  goto_tab 9  alt+9
map alt+0  kitty smart_tab.py  goto_tab 10  alt+0
```
