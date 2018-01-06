# Editor Components

## *Event Listener*

An editor backend which is obsessive-compulsive about logging all interesting activity and preserving it.
A fast/reliable server which logs all activity with low latency.
- All mouse activity
- All keyboard activity
- All microphone activity
- Other input device activity

Event listener should also listen to other events:
- All configuration events
- - this is how you would register :q to be the exit command for example.
- Module/plugin load events 

## Event Record

The event record is very generic. It has the following:
1. Start Time (t) -> Unix-time of event (64 bit)
1. Command Namespace Size (fs) -> Size of command family record (64 bit)
1. Command Namespace (f) -> Variable length string namespace. Cannot be empty.
2. Command Size (cs) -> Size of command (64 bit)
3. Command (c) -> Variable length string command. Cannot be empty.
4. Payload Size (ps) -> Size of payload (64 bit)
4. Payload (v) -> Variable length string payload. Can be empty.

## Default Events (in namespace 'root')
1. Start
1. Stop
1. Kill
1. Register namespace [payload: module]
### Create a New Event Type

## *Event Processors*

A set of modules which subscribe to events and/or event streams and evaluate them as commands.

### Event Logger
By default there should be an event logger which logs every event in a permanent store.
Event loggers should be of the following types:

1. *Full logger to file*: Logs to a text logfile in the current folder.
2. *Log to async dump*: Logs to a an async store in realtime or in burst mode. 

### *Editor View*

At any point in time each text/document has a:
- Full Document Dditing History (of all events captured by the event listener)
- Document History (snapshots of the text at regular intervals)
- Current Document (full text)
- Current Portal View (multiple) - this is what shows up on the screen