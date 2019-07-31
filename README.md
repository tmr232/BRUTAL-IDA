# BRUTAL IDA
## Block Redo & Undo To Achieve Legacy IDA

## The Problem

As we all know, IDA has no undo.
No undo - no surrender.

So naturally, IDA 7.3 adding undo functionality has ruined everyone's workflow.


### In The Media

- [IDA 7.3 Adds Undo][undo-added]
- [Undo Causes Massive Outcry][undo-outcry]
- [T-Shirt Line Destroyed][tshirts]


This will not stand.

## The Solution

BRUTAL IDA restores your original workflow by blocking the `undo` and `redo` keyboard shortcuts.

It comes in 2 modes:

- ![][ida6]: Block `undo` and `redo`
- ![][ida5]: Crash IDA on `undo` and `redo`

## Installation & Usage

It is recommended to install the plugin using the [IDA Plugin Loader](https://github.com/tmr232/ida-plugin-loader).
Just point it to the `brutal_ida.py` script.

Once installed, the plugin will add a toolbar to IDA:

![][toolbar]

Clicking the IDA icon will toggle between ![][ida5] and ![][ida6] modes. The default is ![][ida6].


[ida5]: BRUTAL-ICONS/BRUTAL_IDA5.png "5.x"
[ida6]: BRUTAL-ICONS/BRUTAL_IDA6.png "6.x"
[toolbar]: brutal_toolbar.png "BRUTAL IDA Toolbar"

[undo-added]: https://twitter.com/newsoft/status/1135417060907991040
[undo-outcry]: https://twitter.com/tmr232/status/1135869035806101505
[tshirts]: https://twitter.com/IgorSkochinsky/status/1135912157973893120