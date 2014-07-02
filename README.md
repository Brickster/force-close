# ForceClose

ForceClose is a [Sublime Text][] plugin that adds the ability to close a tab without prompting to save changes.

[Sublime Text]: http://www.sublimetext.com

## Why

Sublime Text has a built-in command to close a view: `close_by_index`. However, it will prompt to save changes if they exist. What if you don't care?

## Use

Right-click a tab and select `Force Close`.

Alternatively, you can send the command `force_close_by_index` to a `sublime.Window` object with the arguments `group` and `index` for the tab you want closed. If not supplied, the currently active view will be closed.

## Settings

`save_when_possible`: if true, unsaved changes are kept; else, they are discarded. This only applies to views that are not orphans.  
`save_orphaned_views`: if true, an orphaned view's file is recreated; else, the view is discarded.

## Compatibility

ForceClose is only officially supported in Sublime Text 3. It may work with older versions but I haven't tried. Use at your own risk. Worst case scenario, you can't force close a tab. Honestly, that's less destructive than actually getting it to work.

## Terminology

**Orphan**: a view whose undyling file is missing. Eligibility for being missing includes having been deleted or moved. If a file has never existed for the view, it cannot be an orphan.
