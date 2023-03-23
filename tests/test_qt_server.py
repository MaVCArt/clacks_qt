import sys
import clacks
import unittest
import threading
import clacks_qt
from clacks_qt.vendor import Qt


# ----------------------------------------------------------------------------------------------------------------------
class TestQtServer(unittest.TestCase):

    # ------------------------------------------------------------------------------------------------------------------
    def test_qt_server(self):
        host, port = 'localhost', clacks.get_new_port('localhost')

        app = Qt.QtWidgets.QApplication(sys.argv)

        widget = Qt.QtWidgets.QLabel()
        widget.show()

        assert isinstance(threading.currentThread(), threading._MainThread)

        def foo(label):
            assert isinstance(threading.currentThread(), threading._MainThread)
            widget.setText(label)
            app.processEvents()

        server = clacks_qt.QtServerBase('UNITTEST')
        server.register_interface_by_key('standard')

        handler = clacks.SimpleRequestHandler(clacks.SimplePackageMarshaller())
        server.register_handler(host, port, handler)

        server.register_command('foo', foo)

        server.start(blocking=False)

        def run():
            proxy = clacks.ClientProxyBase((host, port), handler)
            proxy.register_interface_by_type('standard')
            for i in range(50):
                proxy.foo('bar %s' % i)
            app.quit()

        thread = threading.Thread(target=run)
        thread.setDaemon(True)
        thread.start()

        app.exec_()
