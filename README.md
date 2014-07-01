# ForceClose

ForceClose is a [Sublime Text][] plugin that adds the ability to close a tab without prompting to save changes.

[Sublime Text]: http://www.sublimetext.com

## Why

Sublime Text has a built-in command to close a view: `close_by_index`. However, it will prompt to save changes if they exist. What if you don't care?

## Use

Right-click a tab and select `Force Close`.

- If the tab has never been saved, the changes are discarded and the tab is closed.
- If the tab has unsaved changes, the tab is saved and closed.
- If no changes exist, the tab is closed.

Alternatively, you can send the command `force_close_tab` to a `sublime.Window` object with the arguments `group` and `index` for the tab you want closed. If not supplied, the currently active view will be closed.

## Compatibility

ForceClose is only officially supported in Sublime Text 3. It may work with older versions but I haven't tried. Use at your own risk. Worst case scenario, you can't force close a tab. Honestly, that's less destructive than actually getting it to work.
