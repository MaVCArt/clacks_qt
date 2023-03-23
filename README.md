clacks_qt
=========

Extension library for the Clacks framework that provides qt-specific utilities like a thread-safe, qt event-driven
server class.

Qt Server
---------

The Qt Server implementation makes use of a clever trick with `Qt` Signals, to create a server that will work inside
applications that are otherwise not friendly to threads. A typical example of this would be Unreal Engine, Maya or 3ds
Max, which can technically run threads in their python interpreters, but start to act up if that thread attempts to
anything to the main thread. This is also common behaviour in Qt Applications.

Signals solve this problem, as `QThreads` and thread workers don't actually run in a separate thread; they run in the
main thread, but Qt ensures they don't block it.

This type of structure allows us to run the logistics of the server (I/O, digest, marshalling) on a real thread,
while the non-thread-safe behaviour is handled on the main thread itself.
