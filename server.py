from .vendor import Qt
from clacks.core.server import ServerBase


# ----------------------------------------------------------------------------------------------------------------------
class QtServerBase(Qt.QtCore.QObject, ServerBase):

    RespondRequested = Qt.QtCore.Signal(object, object, object, object, object)

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, identifier, **kwargs):
        Qt.QtCore.QObject.__init__(self)

        ServerBase.__init__(
            self,
            identifier=identifier,
            start_queue=False,
            threaded_digest=False,
        )

        # -- Qt redirect to prevent methods from being executed off the main thread.
        self.RespondRequested.connect(self._qt_respond)

        self.start_queue()

    # ------------------------------------------------------------------------------------------------------------------
    def _qt_respond(self, handler, connection, transaction_id, header_data, data):
        # type: (BaseRequestHandler, socket.socket, str, dict, dict) -> None
        ServerBase.__respond(self, handler, connection, transaction_id, header_data, data)

    # ------------------------------------------------------------------------------------------------------------------
    def __respond(self, handler, connection, transaction_id, header_data, data):
        # type: (BaseRequestHandler, socket.socket, str, dict, dict) -> None
        self.RespondRequested.emit(handler, connection, transaction_id, header_data, data)
